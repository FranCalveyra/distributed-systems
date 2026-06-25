# Two-Phase Commit (2PC)

**Python**, simulación secuencial y síncrona — el protocolo en sí no necesita concurrencia real para entenderse, así que priorizamos legibilidad.

De `tolerancia.md`: *"Commit distribuido y atómico... involucra 1 coordinador y N participantes. Complicado hacerlo en ciertos casos distintos a una base de datos. En la práctica es un problema más que una solución."*

## El escenario del ejemplo de la teórica

*"Reservar hotel y vuelo"* — ¿cómo aseguro que se haga todo o nada? Acá se extiende a hotel + auto + vuelo.

## Protocolo

**Fase 1 — PREPARE (votación)**: el coordinador le pregunta a cada participante si puede comprometerse a la operación. Cada uno responde `YES` o `NO` (en la vida real, acá reserva el recurso con un lock, sin liberar nada todavía).

**Fase 2 — DECIDE**:
- Si **todos** votaron `YES` → el coordinador manda `COMMIT` a todos.
- Si **alguno** votó `NO` → el coordinador manda `ABORT` a todos.

Es **todo o nada**: no hay escenario donde algunos participantes commiteen y otros no.

## Cómo correr

```bash
python3 two_phase_commit.py
```

## Qué muestra

Dos escenarios con los mismos 3 participantes (hotel, auto, vuelo):
1. **Todos disponibles** → `COMMIT` en los tres.
2. **El vuelo no tiene asientos** → `ABORT` en los tres, incluso en los que sí podían reservar.

## Por qué la teórica dice que "en la práctica es un problema más que una solución"

2PC es **bloqueante**: si el coordinador se cae después de la fase de PREPARE pero antes de mandar la decisión, los participantes quedan con el lock tomado **indefinidamente**, sin saber si deben comprometer o abortar. Por eso en sistemas reales se prefieren **compensaciones** (deshacer una operación ya hecha, no es un rollback) en lugar de 2PC — ver el ejemplo de Despegar.com en `tolerancia.md`: reservás el hotel, el pasaje ya está commiteado, y si el hotel falla mandás un mail o hacés un contramovimiento en lugar de intentar un commit atómico distribuido.
