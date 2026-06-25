# Raft (toy) — Elección de líder + Heartbeats

**Go**, con concurrencia real (goroutines + timers) porque el corazón de Raft son los **timeouts** y eso necesita tiempo real corriendo, no un loop secuencial.

> Este ejemplo implementa **solo** elección de líder y heartbeats. **No** incluye replicación de log — eso ya es un Trabajo Práctico en sí mismo. Sirve para entender la parte de consenso/coordinación que menciona `tolerancia.md`, no como una implementación completa de Raft.

## De la teórica

> "Raft: fail-noisy (la caída es detectada correctamente en algún momento)... funciona por términos: ventanas de tiempo en las que hay a lo sumo un líder. Ningún nodo tiene jerarquía, solo se determina por quién pide ser coordinador."

A diferencia de **Bully** (coordinador = mayor ID, siempre determinístico), en Raft cualquier nodo puede proponerse candidato — gana el que junte mayoría de votos primero, y eso depende del **timing**, no de un ID fijo.

## Reglas implementadas

- Cada nodo es `Follower`, `Candidate` o `Leader`.
- Un `Follower` sin heartbeat dentro de su timeout (**aleatorio**, 200-400ms, justamente para que no todos arranquen elección al mismo tiempo) se vuelve `Candidate`: sube su término, se vota a sí mismo, pide voto a todos.
- Gana mayoría simple → `Leader`. Manda heartbeats cada 50ms.
- Cualquier nodo que vea un término mayor al propio (en un voto o un heartbeat) se vuelve `Follower` inmediatamente.

## Cómo correr

```bash
go run .
# o con el detector de race conditions:
go run -race .
```

## Qué hace el programa

1. Arrancan 5 nodos. Se resuelve una elección inicial.
2. A los 700ms, identifica al líder actual y lo **mata** (deja de responder a cualquier RPC).
3. A los 1400ms, corta todo y muestra el estado final de los 5 nodos.

## Qué observar

- Solo gana **un** candidato por término — el resto pierde la elección (votos < mayoría) y vuelve a `Follower`.
- Después de matar al líder, los followers dejan de recibir heartbeats, su timeout vence, y arranca una **nueva elección** con un término más alto.
- El nodo caído queda congelado en su último término conocido, mientras el resto avanza.

## Bug real que encontramos haciendo este ejemplo

La primera versión reseteaba el timer del nodo usando el **rol viejo** (antes de correr la elección), así que un nodo que ganaba la elección igual esperaba un timeout largo de elección antes de mandar su primer heartbeat — dejando una ventana donde los followers, sin enterarse de que ya había líder, arrancaban su propia elección. La métrica reveladora: ningún log de *"reconoce a nodo X como líder"* aparecía hasta mucho después de la primera elección. El fix: re-chequear el rol **después** de correr la elección y, si ganó, mandar el heartbeat ya mismo en lugar de esperar al próximo tick del timer.
