"""
Ejemplo de operaciones colectivas en MPI: scatter + reduce.

Modela el patrón clásico HPC y lo que dice la teórica:
- El nodo de rango 0 es el "padre": genera la data.
- Reparte (scatter) un pedazo a cada proceso.
- Cada proceso computa una suma parcial sobre su pedazo.
- El padre junta todas las parciales con un reduce (SUM).

Todos los procesos corren ESTE MISMO archivo, en simultáneo y bajo un mismo
contexto (COMM_WORLD). Lo que los diferencia es su `rank`.

Cómo correr (con 4 procesos):
    mpirun -np 4 python3 scatter_reduce.py
"""
from mpi4py import MPI

ROOT = 0


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()   # id del proceso dentro del contexto
    size = comm.Get_size()   # cantidad total de procesos

    if rank == ROOT:
        data = list(range(1, 21))  # 1..20
        print(f"[rank {rank}] (padre) data completa: {data}")
        # Partimos en `size` pedazos lo más parejos posible (round-robin).
        chunks = [data[i::size] for i in range(size)]
    else:
        data = None
        chunks = None

    # scatter: cada proceso recibe SU pedazo. El padre se queda con chunks[0].
    my_chunk = comm.scatter(chunks, root=ROOT)
    partial = sum(my_chunk)
    print(f"[rank {rank}] chunk={my_chunk} -> suma parcial={partial}")

    # reduce: el padre agrega todas las parciales aplicando SUM.
    total = comm.reduce(partial, op=MPI.SUM, root=ROOT)

    if rank == ROOT:
        print(f"[rank {rank}] (padre) suma total = {total} (esperado {sum(data)})")


if __name__ == "__main__":
    main()
