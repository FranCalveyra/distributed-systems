# Modelos de Consistencia — Secuencial vs Causal

Dos scripts en **Python puro** (legibilidad ante todo, es conceptual). Ambos verifican por código afirmaciones concretas de `replicacion.md`, no solo las ilustran.

## `sequential.py` — el ejemplo clásico de Tanenbaum

```
P1: x <- 1; print(y, z)
P2: y <- 1; print(x, z)
P3: z <- 1; print(x, y)
```

Enumera **por fuerza bruta** todos los entrelazados que respetan el orden de programa de cada proceso (escritura antes que lectura), y verifica dos afirmaciones de la teórica:

1. Hay exactamente **90** entrelazados válidos (de los 720 = 6! totales sin esa restricción).
2. La firma **"000000"** (los 3 procesos leyendo 0 en ambas variables ajenas) es **imposible** — lo prueba intentando las 90 combinaciones y confirmando que ninguna la produce.

```bash
python3 sequential.py
```

## `causal_vs_sequential.py` — dónde se separan los dos modelos

Un escenario mínimo con 3 escrituras:
- `w1` (proceso A escribe x)
- `w2` (proceso B, **después de leer w1**, escribe y) → `w1 -> w2` causalmente
- `w3` (proceso C escribe z **sin relación** con A ni B) → concurrente con ambas

Dos réplicas aplican los updates en **distinto orden** (`[w1,w2,w3]` vs `[w3,w1,w2]`). El script verifica:

- **Consistencia causal**: solo exige que `w1` aparezca antes que `w2` en cada réplica. ✅ Se cumple en ambas.
- **Consistencia secuencial**: exige que TODAS las réplicas tengan el mismo orden total, sin importar causalidad. ❌ No se cumple, porque difieren en dónde cae `w3`.

```bash
python3 causal_vs_sequential.py
```

## La conclusión que importa

La consistencia causal es **estrictamente más permisiva** que la secuencial: todo lo que es secuencialmente consistente también es causalmente consistente, pero no al revés. Causal solo le importa el orden de lo que está relacionado por causa-efecto; a secuencial le importa el orden de **todo**, incluso lo concurrente.
