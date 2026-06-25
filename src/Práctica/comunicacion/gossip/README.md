# Gossip, Broadcasting y Multicasting

Dos simulaciones en **Python puro** (sin dependencias) de cómo se propaga información en una overlay network. Acá la legibilidad es todo: estos temas son algorítmicos, así que el código se lee como el pseudocódigo de la teórica y mapea 1:1 con `clase_3.md`.

## Ejemplos

| Archivo | Tema | Qué muestra |
|---------|------|-------------|
| `epidemic.py` | Protocolos epidémicos / anti-entropía | Compara `push`, `pull` y `push-pull` por rondas |
| `flooding.py` | Broadcasting por flooding | Costo lineal (árbol) vs cuadrático (grafo completo) |

## `epidemic.py` — protocolos epidémicos

Un nodo arranca con un update nuevo (el "paciente cero") y se propaga por **rondas**. En cada ronda cada nodo elige un peer al azar e intercambian:

- **push**: el infectado empuja el update al peer.
- **pull**: el nodo le pide al peer; si el peer lo tiene, se contagia.
- **push-pull**: ambas.

La conclusión que demuestra: **push-pull converge en menos rondas**. `push` se frena cuando ya casi todos están infectados (es raro que justo elija a uno susceptible); `pull` y `push-pull` no, porque los pocos susceptibles que quedan tienen alta chance de toparse con un infectado.

```bash
python3 epidemic.py
```

## `flooding.py` — broadcasting

Cada nodo reenvía el mensaje a todos sus vecinos menos a quien se lo mandó, y descarta lo ya visto. Se cuenta la cantidad de **envíos** (link stress) según la topología:

- **línea / árbol** → los envíos crecen **lineal** (n-1, una vez por arista).
- **grafo completo** → crecen **cuadrático** (~n²).

Por eso, para hacer broadcasting eficiente, conviene construir una overlay con forma de árbol (idealmente un *Minimal Spanning Tree*, como menciona la teórica al hablar de *tree cost*).

```bash
python3 flooding.py
```

## Relación con la teoría

- **Multicasting** = mandar a un subconjunto de nodos (no a todos). Se modela teniendo *multicast groups* y haciendo broadcasting dentro del grupo.
- **Broadcasting** = mandar a todos. El flooding es el mecanismo base.
- **Gossiping / rumor spreading** = variante epidémica donde un nodo, al contactar a otro que ya tenía el update, puede volverse *removido* con probabilidad `P_stop`. Rápido, pero **no garantiza** que todos reciban el update (a cambio, es mucho más difícil saturar la red).
