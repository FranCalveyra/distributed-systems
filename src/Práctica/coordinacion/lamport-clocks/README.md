# Relojes Lógicos de Lamport

Simulación en **Python** (legibilidad ante todo, es puramente algorítmico) de las 4 reglas de happens-before de Lamport:

1. Mismo proceso, A antes que B → A → B
2. A = envío de mensaje, B = su recepción → A → B (nunca se recibe antes de enviar)
3. Transitividad: A → B y B → C ⟹ A → C
4. Si ni A → B ni B → A, son **concurrentes**

## La regla clave

Cuando un proceso **recibe** un mensaje, ajusta su reloj con:

```python
self.clock = max(self.clock, sender_timestamp) + 1
```

Esto es lo que **garantiza matemáticamente** la regla 2: como mínimo el reloj del receptor queda en `sender_timestamp + 1`, así que el timestamp de la recepción siempre es mayor al del envío.

## Cómo correr

```bash
python3 lamport.py
```

## Qué muestra la salida

- `P1 → P2 (M1)` y `P2 → P3 (M2)`: dos envíos/recepciones que cumplen la regla 2.
- Transitividad: como P1 hizo algo antes de mandar M1, y ese mensaje encadena hasta que P3 recibe M2, el evento original de P1 **happens-before** la recepción en P3 — aunque P1 y P3 nunca se hablaron directamente.
- Un evento de P3 *antes* de recibir cualquier mensaje de la cadena: no tiene relación causal con el primer evento de P1, así que son **concurrentes**.

## Limitación de los relojes escalares

`timestamp(a) < timestamp(b)` es **necesario pero no suficiente** para `a → b`: puede haber dos eventos sin relación causal real cuyos timestamps escalares igual queden ordenados por casualidad. Por eso, cuando se necesita causalidad precisa con muchos procesos, se usan [relojes de vectores](../vector-clocks/) en su lugar.
