"""
Simulación de un protocolo epidémico (anti-entropía) para propagar un update.

Modela los roles que vimos en la teórica:
- Infectado:   tiene el update y lo intenta compartir.
- Susceptible: todavía no lo tiene.

Y compara las tres estrategias de intercambio por rondas. En cada ronda, cada
nodo elige un peer al azar e intercambian según la estrategia:

- push:      si YO estoy infectado, contagio al peer.
- pull:      si el PEER está infectado, me contagio.
- push-pull: ambas (la mejor empíricamente).

Por qué push se vuelve lento: conforme crecen los infectados, baja la
probabilidad de que un infectado justo elija a un susceptible. Pull (y push-pull)
escalan mejor porque los susceptibles que quedan tienen cada vez más chances de
toparse con un infectado.

Cómo correr:
    python3 epidemic.py
"""
import random


def simulate(n_nodes: int, strategy: str, seed: int | None = None) -> tuple[int, list[int]]:
    """Devuelve (rondas_hasta_converger, historia_de_infectados_por_ronda)."""
    rng = random.Random(seed)
    infected = [False] * n_nodes
    infected[0] = True  # paciente cero

    rounds = 0
    history = [1]
    while not all(infected):
        rounds += 1
        # Snapshot del estado al INICIO de la ronda: los contagios de esta ronda
        # no deben cascadear dentro de la misma ronda.
        snapshot = infected[:]
        for i in range(n_nodes):
            j = rng.randrange(n_nodes)
            if j == i:
                continue
            if strategy in ("push", "push-pull") and snapshot[i]:
                infected[j] = True
            if strategy in ("pull", "push-pull") and snapshot[j]:
                infected[i] = True
        history.append(sum(infected))

        if rounds > n_nodes * 20:  # red de seguridad
            break

    return rounds, history


def main():
    n = 1000
    print(f"Propagando un update entre {n} nodos (paciente cero = nodo 0)\n")
    print(f"{'estrategia':>10} | {'rondas':>6} | infectados por ronda (primeras 8)")
    print("-" * 60)
    for strat in ("push", "pull", "push-pull"):
        rounds, history = simulate(n, strat, seed=42)
        preview = ", ".join(str(x) for x in history[:8])
        print(f"{strat:>10} | {rounds:>6} | {preview}, ...")

    print(
        "\npush-pull converge en menos rondas: combina lo mejor de empujar y tirar."
    )


if __name__ == "__main__":
    main()
