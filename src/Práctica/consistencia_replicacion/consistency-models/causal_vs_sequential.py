"""
Demuestra la diferencia central entre consistencia secuencial y causal:

- Secuencial: TODOS los procesos deben ver el MISMO orden total de TODAS
  las operaciones (no importa si están relacionadas causalmente o no).
- Causal: solo las escrituras CAUSALMENTE relacionadas deben verse en el
  mismo orden en todos lados. Las escrituras CONCURRENTES (sin relación de
  causa-efecto) pueden verse en órdenes distintos en réplicas distintas.

Escenario:
  - Proceso A escribe x=1                              (w1)
  - Proceso B LEE x=1 (se entera de w1) y después escribe y=2 (w2)
    => w1 -> w2 (relación causal: B escribió w2 sabiendo de w1)
  - Proceso C escribe z=3 (w3), sin haber leído nada de A ni B
    => w3 es CONCURRENTE con w1 y w2 (no hay relación causal)

Dos réplicas reciben los updates en orden distinto:
  - Réplica 1: w1, w2, w3
  - Réplica 2: w3, w1, w2

Cómo correr:
    python3 causal_vs_sequential.py
"""

# Cada escritura es un id. causal_deps describe pares (a, b) donde a -> b.
CAUSAL_DEPS = [("w1", "w2")]  # w1 happens-before w2; w3 no tiene relación con nadie

REPLICA_1 = ["w1", "w2", "w3"]
REPLICA_2 = ["w3", "w1", "w2"]


def is_causally_consistent(replica_order: list[str], causal_deps: list[tuple[str, str]]) -> bool:
    """Toda escritura `a` que causalmente precede a `b` debe aparecer antes
    que `b` en CADA réplica. No importa dónde caigan las concurrentes."""
    position = {op: i for i, op in enumerate(replica_order)}
    return all(position[a] < position[b] for a, b in causal_deps)


def is_sequentially_consistent(replicas: list[list[str]]) -> bool:
    """Condición (suficiente, y la más simple de verificar): todas las
    réplicas deben coincidir en el MISMO orden total para TODAS las
    operaciones, relacionadas causalmente o no."""
    return all(replica == replicas[0] for replica in replicas[1:])


def main():
    print(f"Réplica 1 aplica: {REPLICA_1}")
    print(f"Réplica 2 aplica: {REPLICA_2}")
    print(f"Dependencia causal conocida: w1 -> w2 (w3 es concurrente con ambas)\n")

    causal_r1 = is_causally_consistent(REPLICA_1, CAUSAL_DEPS)
    causal_r2 = is_causally_consistent(REPLICA_2, CAUSAL_DEPS)
    print(f"¿Réplica 1 respeta causalidad (w1 antes que w2)? {causal_r1}")
    print(f"¿Réplica 2 respeta causalidad (w1 antes que w2)? {causal_r2}")

    secuencial = is_sequentially_consistent([REPLICA_1, REPLICA_2])
    print(f"\n¿Ambas réplicas tienen EXACTAMENTE el mismo orden total? {secuencial}")

    print(
        "\nConclusión: el sistema ES causalmente consistente (w1 -> w2 se respeta\n"
        "en todos lados), pero NO ES secuencialmente consistente (las réplicas\n"
        "discrepan sobre dónde cae w3, que es concurrente). Esto es exactamente\n"
        "lo que permite la consistencia causal y prohíbe la secuencial: las\n"
        "escrituras concurrentes pueden verse en orden distinto según el lugar."
    )


if __name__ == "__main__":
    main()
