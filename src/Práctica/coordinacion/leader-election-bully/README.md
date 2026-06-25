# Algoritmo Bully

**Go**, igual que [Ricart-Agrawala](../mutex-ricart-agrawala/): procesos concurrentes reales (goroutines) que se mandan mensajes por channels, no un loop que simula turnos.

## Algoritmo

- El coordinador es, por convención, el nodo con **ID más grande**.
- Cuando un nodo detecta que el coordinador no responde, manda `ELECTION` a todos los nodos con ID **mayor** al suyo.
  - Si nadie responde → se convierte en coordinador y anuncia `COORDINATOR` a todos.
  - Si alguno responde `ALIVE` → ese nodo de ID mayor se hace cargo de seguir el proceso.
- Quien recibe un `ELECTION` de un nodo menor responde `ALIVE` y, si no estaba ya en medio de una elección propia, arranca la suya (contra los que son mayores que él).

## Cómo se simula la caída del coordinador

El nodo con mayor ID (el coordinador inicial) **nunca arranca su goroutine** — no escucha ni responde nada. Los `send` a su canal son no bloqueantes (`sendNonBlocking`, con `select`/`default`), así que el resto del sistema no se cuelga esperando una respuesta que nunca va a llegar. Es la forma más simple de modelar un timeout de heartbeat sin implementar heartbeats de verdad.

## Cómo correr

```bash
go run .
```

## Qué observar

- Los nodos vivos detectan la caída casi en simultáneo (con jitter), como pasaría con un timeout de heartbeat real.
- Vas a ver nodos de ID bajo mandar `ELECTION` contra varios nodos mayores, recibir `ALIVE` de algunos, y quedarse esperando el anuncio de coordinador en lugar de proclamarse ellos mismos.
- El nodo con mayor ID entre los vivos es el único que no recibe `ALIVE` de nadie (porque no hay nadie por encima, salvo el coordinador caído) y se proclama coordinador.

## Lo que el ejemplo NO cubre (por simplicidad)

- **Reintentos**: si el nodo que iba a ser coordinador también se cae en medio del proceso, en este ejemplo solo se loguea el problema, no se reintenta la elección.
- **Algoritmo del anillo**: usa el mismo concepto (elegir por ID más grande) pero con una topología de anillo en lugar de "preguntale a todos los mayores". No lo separamos en otro ejemplo porque el patrón de fondo es idéntico — lo que cambia es la topología de mensajes, no la lógica de decisión.
