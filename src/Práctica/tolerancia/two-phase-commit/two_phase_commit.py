"""
Two-Phase Commit (2PC): commit distribuido y atómico con 1 coordinador y N
participantes (de `tolerancia.md`: "Complicado hacerlo en ciertos casos
distintos a una base de datos... en la práctica es un problema más que una
solución").

Fase 1 (VOTE): el coordinador manda PREPARE a todos los participantes. Cada
uno responde YES (puede comprometerse a hacer commit) o NO (tiene que abortar,
ej: no tiene los recursos, hay un conflicto, etc).

Fase 2 (DECIDE):
- Si TODOS votaron YES -> el coordinador manda COMMIT a todos.
- Si AL MENOS UNO votó NO -> el coordinador manda ABORT a todos.

Es secuencial y síncrono (no necesita concurrencia real para demostrar la
lógica), así que Python alcanza y sobra para que se lea claro.

Cómo correr:
    python3 two_phase_commit.py
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Participant:
    name: str
    will_vote_yes: bool
    committed: bool = False
    aborted: bool = False

    def prepare(self) -> bool:
        """Fase 1: vota. En la vida real acá se reserva el recurso (lock)
        sin liberar nada todavía, justo para poder cumplir si el coordinador
        después manda COMMIT."""
        vote = self.will_vote_yes
        print(f"  [{self.name}] vota {'YES' if vote else 'NO'}")
        return vote

    def commit(self) -> None:
        self.committed = True
        print(f"  [{self.name}] aplica COMMIT (libera el lock, persiste el cambio)")

    def abort(self) -> None:
        self.aborted = True
        print(f"  [{self.name}] aplica ABORT (libera el lock, descarta el cambio)")


class Coordinator:
    def __init__(self, participants: list[Participant]):
        self.participants = participants

    def run_transaction(self) -> bool:
        print("FASE 1 — PREPARE (pidiendo voto a todos los participantes):")
        votes = [p.prepare() for p in self.participants]
        all_yes = all(votes)

        print(f"\nDecisión: {'COMMIT' if all_yes else 'ABORT'} "
              f"({'todos votaron YES' if all_yes else 'al menos uno votó NO'})\n")

        print("FASE 2 — DECIDE:")
        for p in self.participants:
            if all_yes:
                p.commit()
            else:
                p.abort()

        return all_yes


def main():
    print("=== Escenario 1: reservar hotel + auto + vuelo (todos disponibles) ===\n")
    participantes_ok = [
        Participant("hotel", will_vote_yes=True),
        Participant("auto", will_vote_yes=True),
        Participant("vuelo", will_vote_yes=True),
    ]
    resultado = Coordinator(participantes_ok).run_transaction()
    print(f"\nResultado: {'COMMIT exitoso, todo reservado' if resultado else 'ABORT, nada se reservó'}")

    print("\n" + "=" * 60 + "\n")

    print("=== Escenario 2: mismo caso, pero el vuelo ya no tiene asientos ===\n")
    participantes_fail = [
        Participant("hotel", will_vote_yes=True),
        Participant("auto", will_vote_yes=True),
        Participant("vuelo", will_vote_yes=False),  # sin disponibilidad
    ]
    resultado = Coordinator(participantes_fail).run_transaction()
    print(f"\nResultado: {'COMMIT exitoso, todo reservado' if resultado else 'ABORT, nada se reservó (todo o nada)'}")


if __name__ == "__main__":
    main()
