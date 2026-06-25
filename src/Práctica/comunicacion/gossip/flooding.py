"""
Broadcasting por flooding sobre una overlay network (un grafo).

Regla del flooding (de la teórica):
- Cada nodo reenvía el mensaje recibido a TODOS sus vecinos, excepto al que se
  lo mandó.
- Se evita reenviar mensajes ya vistos (tracking por nodo) para no inundar al
  infinito.

Medimos la cantidad de ENVÍOS (transmisiones por un link). La teórica dice:
- En un árbol: orden lineal en la cantidad de nodos.
- En un grafo completamente conectado: orden cuadrático.
Este script lo muestra con números.

Cómo correr:
    python3 flooding.py
"""
from collections import deque


def flood(graph: dict[int, list[int]], source: int) -> tuple[int, set[int]]:
    """Propaga desde `source`. Devuelve (cantidad_de_envíos, nodos_alcanzados)."""
    seen = {source}
    sends = 0
    # cada item: (nodo_que_reenvía, de_quién_lo_recibió)
    queue = deque([(source, None)])
    while queue:
        node, came_from = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == came_from:
                continue          # no se lo devuelvo a quien me lo mandó
            sends += 1            # se transmite por este link (cuenta para link stress)
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, node))
    return sends, seen


def make_line(n: int) -> dict[int, list[int]]:
    """Grafo en línea 0-1-2-...-(n-1). Es un árbol (sin ciclos)."""
    g: dict[int, list[int]] = {i: [] for i in range(n)}
    for i in range(n - 1):
        g[i].append(i + 1)
        g[i + 1].append(i)
    return g


def make_complete(n: int) -> dict[int, list[int]]:
    """Grafo completamente conectado: todos con todos."""
    return {i: [j for j in range(n) if j != i] for i in range(n)}


def main():
    print(f"{'topología':>16} | {'nodos':>5} | {'envíos':>6} | {'alcanzados':>10}")
    print("-" * 50)
    for n in (4, 8, 16):
        for name, graph in (
            ("línea (árbol)", make_line(n)),
            ("completo", make_complete(n)),
        ):
            sends, reached = flood(graph, source=0)
            print(f"{name:>16} | {n:>5} | {sends:>6} | {len(reached):>10}/{n}")
        print("-" * 50)

    print(
        "\nEn la línea los envíos crecen lineal (n-1, una vez por arista del árbol);\n"
        "en el completo, cuadrático (~n²). Por eso para broadcasting conviene\n"
        "una overlay con forma de árbol."
    )


if __name__ == "__main__":
    main()
