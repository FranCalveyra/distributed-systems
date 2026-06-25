# Relojes de Vectores

Python puro. Resuelve la limitación de los [relojes de Lamport](../lamport-clocks/): con un reloj escalar, `timestamp(a) < timestamp(b)` no garantiza causalidad real. Con un **vector** (una posición por proceso) sí se puede determinar con certeza si dos eventos están causalmente relacionados o son concurrentes.

## Regla de comparación (de la teórica)

Sean `V1` y `V2` dos vectores:

```
V1 > V2  si  para todo i: V1[i] >= V2[i]  Y  existe al menos un j: V1[j] > V2[j]
```

- `V1 > V2` → el evento de V1 pudo haber sido causado por el de V2.
- Ni `V1 > V2` ni `V2 > V1` → **concurrentes**.

## Cómo correr

```bash
python3 vector_clock.py
```

## Qué muestra

1. **Causalidad transitiva por mensajes**: P0 → P1 → P2, encadenado.
2. **Concurrencia real**: dos procesos que nunca se comunicaron directa ni indirectamente.
3. **Conflicto tipo Git**: dos escrituras concurrentes sobre el mismo dato (`campo.valor`), donde ninguna es causa de la otra. El reloj de vectores te dice que **hay** un conflicto — pero no te dice cómo resolverlo. Eso queda en manos de la aplicación (last-write-wins, merge manual, etc), tal como menciona la teórica al compararlo con el manejo de conflictos en un VCS.

## Por qué no alcanza con Lamport

Con un escalar, dos eventos sin relación causal pueden terminar con timestamps ordenados "por casualidad" (coincidencia numérica), y el escalar no te deja distinguir eso de una causalidad real. El vector sí, porque guarda el conocimiento causal completo de cada proceso en el momento del evento.
