"""
Simulación de relojes lógicos de Lamport y la relación happens-before.

Reglas de Lamport (de la teórica):
1. Si A y B ocurren en el MISMO proceso y A pasa antes que B, entonces A -> B.
2. Si A es el envío de un mensaje y B es su recepción en otro proceso,
   entonces A -> B (no se puede recibir antes de enviar).
3. happens-before es transitivo.
4. Si ni A -> B ni B -> A, A y B son CONCURRENTES.

Cada proceso mantiene un contador (su reloj lógico). Al enviar un mensaje viaja
el timestamp del emisor; el receptor ajusta su reloj a max(local, recibido) + 1.
Esto es justamente lo que garantiza la regla 2: nunca se puede "recibir antes
de enviar".

Cómo correr:
    python3 lamport.py
"""
from dataclasses import dataclass, field


@dataclass
class Event:
    process: str
    timestamp: int
    description: str


@dataclass
class Process:
    name: str
    clock: int = 0
    history: list[Event] = field(default_factory=list)

    def local_event(self, description: str) -> Event:
        self.clock += 1
        event = Event(self.name, self.clock, description)
        self.history.append(event)
        return event

    def send(self, description: str) -> Event:
        """Un envío es un evento local más: se le adjunta el timestamp actual."""
        return self.local_event(description)

    def receive(self, sender_timestamp: int, description: str) -> Event:
        """Regla 2: el reloj se ajusta para garantizar que receive > send."""
        self.clock = max(self.clock, sender_timestamp) + 1
        event = Event(self.name, self.clock, description)
        self.history.append(event)
        return event


def happens_before(a: Event, b: Event) -> bool:
    """Condición NECESARIA (no suficiente) de happens-before con reloj escalar:
    si a -> b, entonces timestamp(a) < timestamp(b). Lo inverso no vale siempre
    (por eso los relojes de vectores resuelven mejor la causalidad real)."""
    return a.timestamp < b.timestamp


def main():
    p1, p2, p3 = Process("P1"), Process("P2"), Process("P3")

    # P3 hace algo propio ANTES de recibir nada de P1/P2: no tiene relación
    # causal con lo que hagan los otros dos todavía.
    e0 = p3.local_event("trabaja en su propia tarea, sin relación con P1/P2")

    # P1 hace algo local, después le manda un mensaje a P2.
    e1 = p1.local_event("trabaja en su tarea")
    e2 = p1.send("manda mensaje M1 a P2")

    # P2 estaba en otra cosa, recibe M1 y ajusta su reloj.
    e3 = p2.local_event("trabaja en otra tarea")
    e4 = p2.receive(e2.timestamp, "recibe M1 de P1")

    # P2 le reenvía la posta a P3.
    e5 = p2.send("manda mensaje M2 a P3")
    e6 = p3.receive(e5.timestamp, "recibe M2 de P2")

    eventos = [
        ("P3: trabaja (independiente)", e0),
        ("P1: trabaja", e1), ("P1: envía M1", e2),
        ("P2: trabaja", e3), ("P2: recibe M1", e4), ("P2: envía M2", e5),
        ("P3: recibe M2", e6),
    ]

    print("Timeline de eventos (proceso, timestamp lógico):")
    for label, ev in eventos:
        print(f"  {label:<28} -> ({ev.process}, {ev.timestamp})")

    print()
    print(f"e2 -> e4 (M1 enviado antes de recibido)? {happens_before(e2, e4)}")
    print(f"e5 -> e6 (M2 enviado antes de recibido)? {happens_before(e5, e6)}")
    print(f"e1 -> e6 (transitividad: P1 trabajó antes de que P3 reciba M2)? {happens_before(e1, e6)}")
    print(
        f"e0 y e1 son concurrentes (ninguno -> el otro, no hay mensaje que los conecte): "
        f"{not happens_before(e0, e1) and not happens_before(e1, e0)}"
    )


if __name__ == "__main__":
    main()
