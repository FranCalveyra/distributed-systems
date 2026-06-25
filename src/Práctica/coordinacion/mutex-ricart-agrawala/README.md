# Exclusión Mutua Distribuida — Ricart-Agrawala

Implementación en **Go**, usando goroutines como procesos y channels como el canal de mensajes. Acá la concurrencia real importa — channels y goroutines modelan mensaje-pasaje genuino, a diferencia de un loop secuencial que solo simula la idea.

Es la variante **optimizada con timestamps** que menciona la teórica (no la original de "pedile permiso a todos y si uno dice no, no accedés").

## Algoritmo

Para acceder al recurso, un nodo manda `REQUEST(id, timestamp)` a todos los demás. Cada nodo que recibe un request resuelve uno de 3 escenarios:

1. **No quiere el recurso** → responde `OK` ya.
2. **Ya lo tiene** (`HELD`) → encola el mensaje, no responde todavía.
3. **Lo quiere pero no lo tiene** → compara `(timestamp, id)`. Gana el más chico. Si gana el que pide, `OK`; si pierde, se encola.

Un nodo entra a la sección crítica recién cuando recibió `OK` de **todos**. Al salir, responde `OK` a todo lo que había encolado.

## Por qué Go y no Python

Cada nodo es una **goroutine** que solo toca su propio estado (clock, cola de diferidos) — nunca memoria compartida con otro nodo. La comunicación es 100% por channels, así que no hace falta mutex para proteger ese estado. Es la forma más directa de mapear "procesos que se mandan mensajes" a código real y concurrente, no a un `for` que simula turnos.

## Verificación de exclusión mutua

El código incluye un `csGuard` (un contador atómico) que es **independiente del algoritmo**: si dos nodos entraran a la sección crítica al mismo tiempo, hace `panic`. Está ahí solo para verificar que el protocolo cumple su promesa, no es parte de Ricart-Agrawala.

## Cómo correr

```bash
go run .
```

## Qué observar en la salida

- Los nodos arrancan con un pequeño *stagger* aleatorio para generar contención real con timestamps distintos.
- Vas a ver nodos que **encolan** requests de otros por tener prioridad, y luego les responden `OK` recién al salir de la sección crítica.
- Al final: *"Todos los nodos accedieron al recurso sin violar la exclusión mutua."* — si hubiera una violación, el programa habría hecho `panic` antes de llegar ahí.

## Problema conocido (de la teórica)

Si un nodo se cae mientras otros esperan su `OK`, **el resto se bloquea para siempre** — el algoritmo no tiene mecanismo de timeout ni de detección de fallas. Ese es justo el motivo por el que en sistemas reales se combina con [detección de fallas](../../tolerancia/raft-toy/) (heartbeats, timeouts).
