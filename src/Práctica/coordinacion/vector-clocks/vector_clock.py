"""
Relojes de vectores: resuelven la limitación de los relojes de Lamport
(escalares) para determinar causalidad real entre eventos, sin importar
cuántos procesos haya ni cuántas interacciones.

Cada proceso mantiene un vector con UNA posición por proceso del sistema.
Al enviar un mensaje, viaja el vector completo del emisor. Al recibir,
el receptor incrementa SU posición y toma el máximo componente a componente
con el vector recibido.

Comparación (de la teórica):
    V1 > V2  si  para todo i: V1[i] >= V2[i]  Y  existe j: V1[j] > V2[j]

Si V1 > V2 → el evento de V1 pudo haber sido causado por el de V2 (sucede-después).
Si ni V1 > V2 ni V2 > V1 → son CONCURRENTES (igual que en Git: un conflicto real
que hay que resolver arbitrariamente).

Cómo correr:
    python3 vector_clock.py
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class VectorEvent:
    process: str
    vector: tuple[int, ...]
    description: str


def compare(v1: tuple[int, ...], v2: tuple[int, ...]) -> str:
    """Devuelve 'before', 'after' o 'concurrent'."""
    if all(a <= b for a, b in zip(v1, v2)) and any(a < b for a, b in zip(v1, v2)):
        return "before"
    if all(a >= b for a, b in zip(v1, v2)) and any(a > b for a, b in zip(v1, v2)):
        return "after"
    if v1 == v2:
        return "equal"
    return "concurrent"


class Process:
    def __init__(self, name: str, index: int, n_processes: int):
        self.name = name
        self.index = index
        self.vector = [0] * n_processes
        self.history: list[VectorEvent] = []

    def local_event(self, description: str) -> VectorEvent:
        self.vector[self.index] += 1
        return self._record(description)

    def send(self, description: str) -> VectorEvent:
        return self.local_event(description)

    def receive(self, sender_vector: tuple[int, ...], description: str) -> VectorEvent:
        self.vector[self.index] += 1
        # max componente a componente: absorbo todo lo que el emisor ya sabía.
        self.vector = [max(local, remote) for local, remote in zip(self.vector, sender_vector)]
        return self._record(description)

    def _record(self, description: str) -> VectorEvent:
        event = VectorEvent(self.name, tuple(self.vector), description)
        self.history.append(event)
        return event


def main():
    # 3 procesos: P0, P1, P2. Cada vector tiene 3 posiciones, una por proceso.
    p0 = Process("P0", index=0, n_processes=3)
    p1 = Process("P1", index=1, n_processes=3)
    p2 = Process("P2", index=2, n_processes=3)

    a = p0.local_event("P0 escribe x=1")
    b = p0.send("P0 manda su vector a P1")
    c = p1.receive(b.vector, "P1 recibe de P0")

    # Mientras tanto, P2 hace algo totalmente propio, sin comunicarse con nadie.
    d = p2.local_event("P2 escribe y=5 (sin relación con P0/P1)")

    e = p1.send("P1 manda su vector a P2")
    f = p2.receive(e.vector, "P2 recibe de P1")

    print("Eventos y sus vectores [P0, P1, P2]:")
    for label, ev in [
        ("a (P0 local)", a), ("b (P0 envía)", b), ("c (P1 recibe)", c),
        ("d (P2 local, independiente)", d), ("e (P1 envía)", e), ("f (P2 recibe)", f),
    ]:
        print(f"  {label:<32} -> {ev.vector}")

    print()
    print(f"a vs c -> {compare(a.vector, c.vector)} (a se mandó como mensaje hasta c: a -> c)")
    print(f"a vs d -> {compare(a.vector, d.vector)} (P0 y P2 nunca se hablaron: son concurrentes)")
    print(f"d vs f -> {compare(d.vector, f.vector)} (mismo proceso P2, d ocurrió antes que f: d -> f)")
    print(f"c vs f -> {compare(c.vector, f.vector)} (c -> e por ser mismo proceso P1, e -> f por mensaje: c -> f)")

    # Conflicto real, igual que un merge de Git: 2 escrituras concurrentes
    # sobre el mismo dato, sin que ninguna sea causa de la otra.
    print("\nConflicto tipo Git (2 escrituras concurrentes sobre el mismo objeto):")
    write_from_p0 = p0.local_event("P0 escribe campo.valor = 'rojo' (sin saber de P2)")
    write_from_p2 = p2.local_event("P2 escribe campo.valor = 'azul' (sin saber de P0)")
    resultado = compare(write_from_p0.vector, write_from_p2.vector)
    print(f"  {write_from_p0.vector} vs {write_from_p2.vector} -> {resultado}")
    print("  Ninguno es causa del otro: hay que resolver el conflicto arbitrariamente")
    print("  (last-write-wins, merge manual, vector con ambos valores, etc).")


if __name__ == "__main__":
    main()
