// Algoritmo Bully para elección de coordinador.
//
// Reglas (de la teórica):
//   - El coordinador es, por convención, el nodo con el ID más grande.
//   - Cuando un nodo detecta que el coordinador no responde, inicia una
//     elección: manda ELECTION a todos los nodos con ID MAYOR al suyo.
//   - Si ninguno responde, el que inició la elección gana y se anuncia
//     COORDINATOR a todos.
//   - Si alguno responde ALIVE, ese nodo (de ID mayor) se hace cargo de
//     seguir el proceso (inicia su propia elección contra los que sean
//     mayores que él).
//   - Quien recibe un ELECTION de un nodo con ID menor responde ALIVE y, si
//     no estaba ya en medio de una elección propia, arranca la suya.
//
// Simulamos la CAÍDA DEL COORDINADOR simplemente no levantando su goroutine:
// nadie le puede pedir nada, y como los sends son no bloqueantes (ver
// sendNonBlocking), el resto del sistema no se cuelga esperándolo.
package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

const numNodes = 5 // IDs 0..4. El nodo 4 es el coordinador inicial... hasta que se cae.

type msgType int

const (
	msgElection msgType = iota
	msgAlive
	msgCoordinator
)

type message struct {
	kind msgType
	from int
}

type node struct {
	id       int
	inbox    chan message
	peers    []chan message
	aliveCh  chan struct{}
	coordCh  chan int
	electing bool
	mu       sync.Mutex
}

func (n *node) log(format string, args ...any) {
	fmt.Printf("[node %d] "+format+"\n", append([]any{n.id}, args...)...)
}

// sendNonBlocking simula que mandarle un mensaje a un nodo caído no bloquea
// al emisor: si el canal del destino está lleno o nadie lo está leyendo
// (porque ese nodo nunca arrancó), el envío simplemente se descarta.
func sendNonBlocking(ch chan message, msg message) {
	select {
	case ch <- msg:
	default:
	}
}

func (n *node) listen() {
	for msg := range n.inbox {
		switch msg.kind {
		case msgElection:
			n.log("recibe ELECTION de nodo %d (menor), responde ALIVE", msg.from)
			sendNonBlocking(n.peers[msg.from], message{kind: msgAlive, from: n.id})
			n.maybeStartElection()
		case msgAlive:
			select {
			case n.aliveCh <- struct{}{}:
			default:
			}
		case msgCoordinator:
			n.log("recibe anuncio: el nuevo coordinador es el nodo %d", msg.from)
			select {
			case n.coordCh <- msg.from:
			default:
			}
		}
	}
}

func (n *node) maybeStartElection() {
	n.mu.Lock()
	if n.electing {
		n.mu.Unlock()
		return
	}
	n.electing = true
	n.mu.Unlock()

	go n.startElection()
}

func (n *node) higherPeers() []int {
	var higher []int
	for i := n.id + 1; i < len(n.peers); i++ {
		higher = append(higher, i)
	}
	return higher
}

func (n *node) becomeCoordinator() {
	n.log("nadie respondió por encima de mí: ME CONVIERTO EN COORDINADOR")
	for i, peer := range n.peers {
		if i == n.id {
			continue
		}
		sendNonBlocking(peer, message{kind: msgCoordinator, from: n.id})
	}
}

func (n *node) startElection() {
	defer func() {
		n.mu.Lock()
		n.electing = false
		n.mu.Unlock()
	}()

	higher := n.higherPeers()
	n.log("detecta caída del coordinador, inicia ELECTION contra nodos %v", higher)

	if len(higher) == 0 {
		n.becomeCoordinator()
		return
	}

	for _, h := range higher {
		sendNonBlocking(n.peers[h], message{kind: msgElection, from: n.id})
	}

	select {
	case <-n.aliveCh:
		n.log("recibió ALIVE de algún nodo mayor, espera su anuncio de coordinador")
		select {
		case <-n.coordCh:
			// ya logueado en listen()
		case <-time.After(300 * time.Millisecond):
			n.log("nunca llegó el anuncio del coordinador (¿también se cayó?), debería reintentar")
		}
	case <-time.After(150 * time.Millisecond):
		n.becomeCoordinator()
	}
}

func main() {
	inboxes := make([]chan message, numNodes)
	for i := range numNodes {
		inboxes[i] = make(chan message, numNodes*2)
	}

	nodes := make([]*node, numNodes)
	for i := range numNodes {
		nodes[i] = &node{
			id:      i,
			inbox:   inboxes[i],
			peers:   inboxes,
			aliveCh: make(chan struct{}, numNodes),
			coordCh: make(chan int, numNodes),
		}
	}

	crashedCoordinator := numNodes - 1
	fmt.Printf("Coordinador inicial: nodo %d. Simulamos que se cae (nunca arranca su goroutine).\n\n", crashedCoordinator)

	for i, n := range nodes {
		if i == crashedCoordinator {
			continue // el coordinador está caído: no escucha, no responde.
		}
		go n.listen()
	}

	// Todos los nodos vivos detectan, casi al mismo tiempo (con jitter), que
	// el coordinador no responde -- como pasaría con un timeout de heartbeat.
	var wg sync.WaitGroup
	for i, n := range nodes {
		if i == crashedCoordinator {
			continue
		}
		wg.Add(1)
		go func(n *node) {
			defer wg.Done()
			time.Sleep(time.Duration(rand.Intn(20)) * time.Millisecond)
			n.maybeStartElection()
			time.Sleep(500 * time.Millisecond) // deja correr la elección
		}(n)
	}
	wg.Wait()

	fmt.Println("\nElección terminada. El nodo con mayor ID entre los vivos (nodo 3) debería ser el nuevo coordinador.")
}
