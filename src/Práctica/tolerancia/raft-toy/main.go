// Versión mínima de Raft: SOLO elección de líder + heartbeats.
// NO incluye replicación de log (eso sería un TP en sí mismo).
//
// De la teórica (tolerancia.md): Raft tolera fallas fail-noisy (la caída se
// detecta correctamente, aunque no instantáneamente) y funciona por TÉRMINOS:
// ventanas de tiempo en las que hay a lo sumo un líder. Ningún nodo tiene
// jerarquía fija; el coordinador se determina por elección, no por ID como
// en Bully.
//
// Reglas implementadas:
//   - Cada nodo es Follower, Candidate o Leader.
//   - Un Follower que no recibe heartbeat dentro de su timeout (aleatorio,
//     para evitar que todos arranquen elección al mismo tiempo) se vuelve
//     Candidate, sube su término, se vota a sí mismo y pide votos a todos.
//   - Gana quien consiga mayoría simple de votos en ese término.
//   - El líder manda heartbeats periódicos; cualquier nodo que vea un
//     término mayor al propio se vuelve Follower inmediatamente.
package main

import (
	"fmt"
	"math/rand"
	"sync"
	"sync/atomic"
	"time"
)

type role int

const (
	follower role = iota
	candidate
	leader
)

func (r role) String() string {
	return [...]string{"FOLLOWER", "CANDIDATE", "LEADER"}[r]
}

const (
	heartbeatInterval  = 50 * time.Millisecond
	minElectionTimeout = 200 * time.Millisecond
	maxElectionTimeout = 400 * time.Millisecond
)

type requestVoteArgs struct {
	term        int
	candidateID int
}

type requestVoteReply struct {
	term        int
	voteGranted bool
}

type appendEntriesArgs struct {
	term     int
	leaderID int
}

type appendEntriesReply struct {
	term    int
	success bool
}

type node struct {
	id    int
	peers []*node

	mu       sync.Mutex
	term     int
	votedFor int
	state    role

	crashed atomic.Bool
	resetCh chan struct{}
}

func newNode(id int) *node {
	return &node{id: id, votedFor: -1, resetCh: make(chan struct{}, 1)}
}

func (n *node) log(format string, args ...any) {
	fmt.Printf("[node %d] "+format+"\n", append([]any{n.id}, args...)...)
}

func (n *node) signalReset() {
	select {
	case n.resetCh <- struct{}{}:
	default:
	}
}

func randomElectionTimeout() time.Duration {
	span := maxElectionTimeout - minElectionTimeout
	return minElectionTimeout + time.Duration(rand.Int63n(int64(span)))
}

// requestVote: llamada "RPC" (en este ejemplo, una llamada a método directa,
// no por red, para no meter sockets/gRPC y enfocarnos en la lógica de Raft).
func (n *node) requestVote(args requestVoteArgs) requestVoteReply {
	if n.crashed.Load() {
		return requestVoteReply{} // el nodo caído simplemente no responde
	}
	n.mu.Lock()
	defer n.mu.Unlock()

	if args.term < n.term {
		return requestVoteReply{term: n.term, voteGranted: false}
	}
	if args.term > n.term {
		n.term = args.term
		n.state = follower
		n.votedFor = -1
	}
	if n.votedFor == -1 || n.votedFor == args.candidateID {
		n.votedFor = args.candidateID
		n.signalReset()
		return requestVoteReply{term: n.term, voteGranted: true}
	}
	return requestVoteReply{term: n.term, voteGranted: false}
}

func (n *node) appendEntries(args appendEntriesArgs) appendEntriesReply {
	if n.crashed.Load() {
		return appendEntriesReply{}
	}
	n.mu.Lock()
	defer n.mu.Unlock()

	if args.term < n.term {
		return appendEntriesReply{term: n.term, success: false}
	}
	if n.state != follower || args.term > n.term {
		n.log("reconoce a nodo %d como líder del término %d", args.leaderID, args.term)
	}
	n.term = args.term
	n.state = follower
	n.signalReset()
	return appendEntriesReply{term: n.term, success: true}
}

func (n *node) startElection() {
	n.mu.Lock()
	if n.crashed.Load() {
		n.mu.Unlock()
		return
	}
	n.term++
	n.state = candidate
	n.votedFor = n.id
	term := n.term
	n.mu.Unlock()

	n.log("timeout sin heartbeat, inicia ELECCIÓN para el término %d", term)

	votes := int32(1) // se vota a sí mismo
	var wg sync.WaitGroup
	for _, peer := range n.peers {
		wg.Add(1)
		go func(peer *node) {
			defer wg.Done()
			reply := peer.requestVote(requestVoteArgs{term: term, candidateID: n.id})
			if reply.voteGranted && reply.term == term {
				atomic.AddInt32(&votes, 1)
			}
		}(peer)
	}
	wg.Wait()

	majority := (len(n.peers)+1)/2 + 1
	n.mu.Lock()
	defer n.mu.Unlock()
	if n.state == candidate && n.term == term && int(votes) >= majority {
		n.state = leader
		n.log("GANÓ la elección del término %d con %d/%d votos -> ES LÍDER", term, votes, len(n.peers)+1)
	} else if n.state == candidate {
		n.log("perdió la elección del término %d (%d/%d votos)", term, votes, len(n.peers)+1)
		n.state = follower
	}
}

func (n *node) sendHeartbeats() {
	n.mu.Lock()
	term := n.term
	n.mu.Unlock()

	for _, peer := range n.peers {
		go func(peer *node) {
			reply := peer.appendEntries(appendEntriesArgs{term: term, leaderID: n.id})
			if reply.term > term {
				n.mu.Lock()
				if n.term < reply.term {
					n.term = reply.term
					n.state = follower
				}
				n.mu.Unlock()
			}
		}(peer)
	}
}

func (n *node) run(stop <-chan struct{}) {
	timer := time.NewTimer(randomElectionTimeout())
	defer timer.Stop()

	for {
		select {
		case <-stop:
			return
		case <-n.resetCh:
			timer.Reset(randomElectionTimeout())
		case <-timer.C:
			n.mu.Lock()
			currentRole := n.state
			n.mu.Unlock()

			if n.crashed.Load() {
				timer.Reset(randomElectionTimeout())
				continue
			}

			if currentRole != leader {
				n.startElection() // puede convertir a este nodo en líder
			}

			n.mu.Lock()
			becameLeader := n.state == leader
			n.mu.Unlock()

			if becameLeader {
				// Manda el primer heartbeat YA, no esperando un timeout de
				// elección viejo -- si no, los followers arrancan su propia
				// elección antes de enterarse de que ya hay líder.
				n.sendHeartbeats()
				timer.Reset(heartbeatInterval)
			} else {
				timer.Reset(randomElectionTimeout())
			}
		}
	}
}

func (n *node) snapshot() (role, int) {
	n.mu.Lock()
	defer n.mu.Unlock()
	return n.state, n.term
}

const numNodes = 5

func main() {
	nodes := make([]*node, numNodes)
	for i := range numNodes {
		nodes[i] = newNode(i)
	}
	for _, n := range nodes {
		for _, peer := range nodes {
			if peer.id != n.id {
				n.peers = append(n.peers, peer)
			}
		}
	}

	stop := make(chan struct{})
	for _, n := range nodes {
		go n.run(stop)
	}

	time.Sleep(700 * time.Millisecond)

	leaderID := -1
	for _, n := range nodes {
		if r, _ := n.snapshot(); r == leader {
			leaderID = n.id
		}
	}
	fmt.Printf("\n--- Líder actual: nodo %d. Lo matamos para forzar una nueva elección. ---\n\n", leaderID)
	nodes[leaderID].crashed.Store(true)

	time.Sleep(700 * time.Millisecond)
	close(stop)

	fmt.Println("\n--- Estado final ---")
	for _, n := range nodes {
		r, term := n.snapshot()
		crashed := ""
		if n.crashed.Load() {
			crashed = " (CAÍDO)"
		}
		fmt.Printf("nodo %d: %s, término %d%s\n", n.id, r, term, crashed)
	}
}
