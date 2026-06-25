"""
Chord: Distributed Hash Table (DHT) basada en un anillo, el "representante
típico" de los sistemas de naming basados en DHT que menciona la teórica.

Idea central:
- Tanto nodos como claves se hashean al MISMO espacio circular de 2^m IDs
  (consistent hashing). Una clave la "posee" el primer nodo cuyo ID es >= al
  hash de la clave, recorriendo el anillo en sentido horario.
- Cada nodo mantiene una FINGER TABLE de tamaño m: finger[i] apunta al
  sucesor de (node.id + 2^i) mod 2^m.
- Gracias a que los saltos del finger table crecen exponencialmente, una
  búsqueda resuelve en O(log N) saltos en vez de caminar el anillo nodo por
  nodo (que sería O(N)).

Este ejemplo es Python por legibilidad: lo que importa entender es la
estructura (anillo + finger table) y el algoritmo de lookup, no concurrencia.

Cómo correr:
    python3 chord.py
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

M = 8           # bits del espacio de IDs -> anillo de 2^8 = 256 posiciones
RING_SIZE = 2 ** M


def chord_hash(key: str) -> int:
    """Consistent hashing: SHA-1 truncado a M bits."""
    digest = hashlib.sha1(key.encode()).digest()
    return int.from_bytes(digest, "big") % RING_SIZE


def in_interval(x: int, a: int, b: int) -> bool:
    """¿x está en (a, b] dando la vuelta en el anillo si hace falta?"""
    if a < b:
        return a < x <= b
    return x > a or x <= b  # el intervalo "da la vuelta" por el 0


@dataclass
class ChordNode:
    node_id: int
    finger: list[int] = field(default_factory=list)  # finger[i] = id del nodo sucesor
    successor: int = 0


def build_ring(node_ids: list[int]) -> dict[int, ChordNode]:
    sorted_ids = sorted(node_ids)
    nodes = {nid: ChordNode(node_id=nid) for nid in sorted_ids}

    def successor_of(target: int) -> int:
        """Primer node_id >= target, dando la vuelta si ninguno lo es."""
        for nid in sorted_ids:
            if nid >= target:
                return nid
        return sorted_ids[0]  # da toda la vuelta

    for nid in sorted_ids:
        node = nodes[nid]
        node.successor = successor_of((nid + 1) % RING_SIZE)
        for i in range(M):
            start = (nid + 2 ** i) % RING_SIZE
            node.finger.append(successor_of(start))

    return nodes


def closest_preceding_finger(nodes: dict[int, ChordNode], node_id: int, key_id: int) -> int:
    """Busca, de atrás para adelante en la finger table, el salto más grande
    que sigue estando estrictamente entre node_id y key_id."""
    node = nodes[node_id]
    for finger_id in reversed(node.finger):
        if in_interval(finger_id, node_id, key_id) and finger_id != key_id:
            return finger_id
    return node_id  # no hay mejor salto: hay que ir al sucesor directo


def find_successor(nodes: dict[int, ChordNode], start_id: int, key_id: int) -> tuple[int, int]:
    """Devuelve (nodo_responsable, cantidad_de_saltos) para `key_id`."""
    current = start_id
    hops = 0
    while True:
        node = nodes[current]
        if in_interval(key_id, current, node.successor):
            return node.successor, hops
        nxt = closest_preceding_finger(nodes, current, key_id)
        if nxt == current:
            return node.successor, hops + 1  # fallback: no se pudo achicar más
        current = nxt
        hops += 1


def linear_lookup(nodes: dict[int, ChordNode], start_id: int, key_id: int) -> int:
    """Lookup ingenuo, saltando de sucesor en sucesor (O(N)) -- solo para comparar."""
    current = start_id
    hops = 0
    while not in_interval(key_id, current, nodes[current].successor):
        current = nodes[current].successor
        hops += 1
    return hops + 1


def main():
    # 8 nodos distribuidos arbitrariamente en el anillo de 256 posiciones.
    node_ids = [3, 30, 65, 110, 150, 190, 215, 250]
    nodes = build_ring(node_ids)

    print(f"Anillo Chord: {len(node_ids)} nodos en un espacio de {RING_SIZE} IDs\n")
    for nid in sorted(nodes):
        print(f"  nodo {nid:>3} -> sucesor {nodes[nid].successor:>3} | finger[0..{M-1}] = {nodes[nid].finger}")

    print("\nBuscando claves desde el nodo 3:")
    claves = ["foo.txt", "bar.pdf", "distributed-systems", "chord-paper-2001"]
    for clave in claves:
        key_id = chord_hash(clave)
        responsable, saltos_chord = find_successor(nodes, start_id=3, key_id=key_id)
        saltos_lineales = linear_lookup(nodes, start_id=3, key_id=key_id)
        print(
            f"  '{clave}' -> hash={key_id:>3} -> responsable=nodo {responsable:>3} "
            f"| saltos con finger table: {saltos_chord} | saltos lineales: {saltos_lineales}"
        )

    print(
        f"\nCon {len(node_ids)} nodos, log2({len(node_ids)}) ≈ {len(node_ids).bit_length() - 1}: "
        "el finger table resuelve en muchos menos saltos que caminar el anillo nodo por nodo."
    )


if __name__ == "__main__":
    main()
