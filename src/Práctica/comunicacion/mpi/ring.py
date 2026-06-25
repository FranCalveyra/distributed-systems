"""
Ejemplo de comunicación punto a punto en MPI: pasaje de token en anillo.

Un token arranca en el rango 0 y viaja 0 -> 1 -> 2 -> ... -> (size-1) -> 0.
Cada proceso lo recibe de su antecesor, lo incrementa y se lo manda al sucesor.
Cuando vuelve al 0, debería valer `size` (cada nodo sumó 1).

Demuestra `send` / `recv` bloqueantes: el recv se queda esperando hasta que el
mensaje llega, igual que en los sockets, pero acá la comunicación es transparente
porque MPI maneja el transporte.

Cómo correr (con 4 procesos):
    mpirun -np 4 python3 ring.py
"""
from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    nxt = (rank + 1) % size
    prev = (rank - 1) % size

    if rank == 0:
        token = 0
        comm.send(token, dest=nxt)             # arranca el anillo
        token = comm.recv(source=prev)         # espera a que dé la vuelta completa
        print(f"[rank {rank}] el token volvió con valor {token} (esperado {size})")
    else:
        token = comm.recv(source=prev)         # bloquea hasta recibir del anterior
        token += 1
        print(f"[rank {rank}] recibí token={token - 1}, lo paso a rank {nxt} como {token}")
        comm.send(token, dest=nxt)


if __name__ == "__main__":
    main()
