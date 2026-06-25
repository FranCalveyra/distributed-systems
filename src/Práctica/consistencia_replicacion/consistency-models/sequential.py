"""
El ejemplo clásico (Tanenbaum) de consistencia secuencial que aparece en
`replicacion.md`:

    P1: x <- 1; print(y, z)
    P2: y <- 1; print(x, z)
    P3: z <- 1; print(x, y)

Con x=y=z=0 al inicio. Cada proceso siempre escribe ANTES de leer las otras
dos variables (eso es orden de programa, invariante).

La teórica afirma 2 cosas concretas, que este script verifica por fuerza
bruta enumerando TODOS los entrelazados posibles que respetan el orden de
programa de cada proceso:
1. Hay exactamente 90 entrelazados válidos (de los 720 = 6! que habría sin
   la restricción de orden de programa).
2. Ninguno de esos 90 puede producir la firma "000000" (los 3 procesos
   leyendo 0 para ambas variables ajenas), porque eso requeriría un ciclo
   imposible en el orden total.

Cómo correr:
    python3 sequential.py
"""
from itertools import permutations

# Cada proceso: (nombre_var_que_escribe, vars_que_lee_en_orden)
PROCESSES = [
    ("P1", "x", ("y", "z")),
    ("P2", "y", ("x", "z")),
    ("P3", "z", ("x", "y")),
]


def interleavings(seqs: list[list[tuple[str, str]]]):
    """Genera todos los entrelazados de varias secuencias preservando el
    orden interno de cada una. Para 3 secuencias de largo 2, da 6!/(2!2!2!)=90."""
    if all(not s for s in seqs):
        yield []
        return
    for i, s in enumerate(seqs):
        if not s:
            continue
        head, *rest = s
        new_seqs = seqs[:i] + [rest] + seqs[i + 1:]
        for tail in interleavings(new_seqs):
            yield [head] + tail


def build_programs():
    """Cada proceso tiene 2 operaciones: ('W', proc, var, valor) y ('R', proc, vars)."""
    programs = []
    for name, write_var, read_vars in PROCESSES:
        programs.append([
            ("W", name, write_var, 1),
            ("R", name, read_vars),
        ])
    return programs


def execute(sequence) -> str:
    """Ejecuta un entrelazado completo y devuelve la 'firma' de lo impreso,
    concatenando lo que leyó cada proceso en el orden P1,P2,P3."""
    state = {"x": 0, "y": 0, "z": 0}
    printed = {}
    for op in sequence:
        if op[0] == "W":
            _, _, var, val = op
            state[var] = val
        else:
            _, proc, read_vars = op
            printed[proc] = tuple(state[v] for v in read_vars)
    return "".join(str(v) for proc in ("P1", "P2", "P3") for v in printed[proc])


def main():
    programs = build_programs()
    total = 0
    signatures = set()
    for seq in interleavings(programs):
        total += 1
        signatures.add(execute(seq))

    print(f"Entrelazados válidos respetando orden de programa: {total}")
    print(f"(la teórica dice 90 de los 720 = 6! totales sin esa restricción)\n")

    print(f"Firmas distintas observadas: {len(signatures)}")
    print("¿Apareció la firma imposible '000000'?", "000000" in signatures)
    print(
        "\n'000000' es imposible porque requeriría que CADA print ocurra antes\n"
        "de las escrituras de los otros 2 procesos, lo cual forma un ciclo en\n"
        "el orden total (P3 antes que W_x, W_x antes que R_P1 [orden de programa],\n"
        "R_P1 antes que W_y, W_y antes que R_P2 [orden de programa], R_P2 antes\n"
        "que W_x... contradicción)."
    )

    print("\nAlgunas firmas válidas de ejemplo:", sorted(signatures)[:5])


if __name__ == "__main__":
    main()
