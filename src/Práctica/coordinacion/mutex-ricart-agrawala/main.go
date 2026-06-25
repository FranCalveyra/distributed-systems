// Algoritmo de Ricart-Agrawala (la variante optimizada con timestamps, no la
// original) para exclusión mutua distribuida.
//
// Reglas (de la teórica):
//   - Para acceder al recurso, un nodo manda REQUEST(id, timestamp) a TODOS
//     los demás (incluso a sí mismo, conceptualmente).
//   - Cada nodo que recibe un REQUEST responde según 3 escenarios:
//     1. No quiere el recurso             -> responde OK
//     2. Ya lo tiene (HELD)               -> encola el mensaje, no responde
//     3. Lo quiere pero no lo tiene aún   -> compara timestamps: gana el más
//     chico (con el ID como desempate). Si gana el remitente, OK; si no,
//     encola.
//   - Un nodo entra a la sección crítica recién cuando recibió OK de TODOS.
//
// Se modela cada nodo como una goroutine independiente que sólo se comunica
// por channels (mensajes), nunca con memoria compartida directa — así el
// estado de cada nodo (clock, cola de diferidos) sólo lo toca su propia
// goroutine y no hace falta mutex para esa parte.
package main

import (
	"fmt"
	"math/rand"
	"sync"
	"sync/atomic"
	"time"
)

const numNodes = 5

type msgType int

const (
	request msgType = iota
	reply
)

type message struct {
	kind      msgType
	from      int
	timestamp int
}

// less determina quién "gana" comparando (timestamp, id) -- exactamente el
// criterio de desempate que describe la teórica.
func less(tsA, idA, tsB, idB int) bool {
	if tsA != tsB {
		return tsA < tsB
	}
	return idA < idB
}

type node struct {
	id            int
	clock         int
	inbox         chan message
	peers         []chan message // canal de inbox de cada otro nodo
	wanting       bool
	holding       bool
	myTS          int
	deferred      []int
	repliesNeeded int
}

// csGuard detecta violaciones de exclusión mutua de forma INDEPENDIENTE del
// algoritmo, solo para verificar que el protocolo funciona.
var csGuard atomic.Int32

func (n *node) log(format string, args ...any) {
	prefix := fmt.Sprintf("[node %d] ", n.id)
	fmt.Printf(prefix+format+"\n", args...)
}

func (n *node) broadcastRequest() {
	n.clock++
	n.myTS = n.clock
	n.wanting = true
	n.repliesNeeded = numNodes - 1
	n.log("quiere el recurso, manda REQUEST(ts=%d)", n.myTS)
	for i, peer := range n.peers {
		if i == n.id {
			continue
		}
		peer <- message{kind: request, from: n.id, timestamp: n.myTS}
	}
}

func (n *node) enterCriticalSection(wg *sync.WaitGroup) {
	n.holding = true
	n.wanting = false

	inUse := csGuard.Add(1)
	if inUse > 1 {
		panic("VIOLACIÓN DE EXCLUSIÓN MUTUA: más de un nodo en la sección crítica")
	}

	n.log("ENTRA a la sección crítica (ts=%d)", n.myTS)
	time.Sleep(time.Duration(20+rand.Intn(30)) * time.Millisecond) // trabajo simulado
	n.log("SALE de la sección crítica")

	csGuard.Add(-1)
	n.holding = false

	// Al salir, responde OK a todo lo que quedó diferido.
	for _, peerID := range n.deferred {
		n.peers[peerID] <- message{kind: reply, from: n.id}
	}
	n.deferred = nil

	wg.Done()
}

func (n *node) run(wg *sync.WaitGroup) {
	// Stagger inicial para que las requests no salgan todas en el mismo
	// instante y se vea contención real con distintos timestamps.
	time.Sleep(time.Duration(rand.Intn(15)) * time.Millisecond)
	n.broadcastRequest()

	for msg := range n.inbox {
		switch msg.kind {
		case request:
			n.clock = max(n.clock, msg.timestamp) + 1

			switch {
			case n.holding:
				n.log("tiene el recurso, encola REQUEST de nodo %d", msg.from)
				n.deferred = append(n.deferred, msg.from)
			case n.wanting && less(n.myTS, n.id, msg.timestamp, msg.from):
				n.log("está pidiendo y tiene prioridad sobre nodo %d, encola", msg.from)
				n.deferred = append(n.deferred, msg.from)
			default:
				n.log("responde OK a nodo %d", msg.from)
				n.peers[msg.from] <- message{kind: reply, from: n.id}
			}

		case reply:
			n.repliesNeeded--
			n.log("recibió OK de nodo %d (faltan %d)", msg.from, n.repliesNeeded)
			if n.repliesNeeded == 0 {
				n.enterCriticalSection(wg)
				return // este ejemplo: cada nodo pide el recurso una sola vez
			}
		}
	}
}

func main() {
	nodes := make([]*node, numNodes)
	inboxes := make([]chan message, numNodes)
	for i := range numNodes {
		inboxes[i] = make(chan message, numNodes*2)
	}
	for i := range numNodes {
		nodes[i] = &node{id: i, inbox: inboxes[i], peers: inboxes}
	}

	var wg sync.WaitGroup
	wg.Add(numNodes)
	for _, n := range nodes {
		go n.run(&wg)
	}
	wg.Wait()
	fmt.Println("\nTodos los nodos accedieron al recurso sin violar la exclusión mutua.")
}
