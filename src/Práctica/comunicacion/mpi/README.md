# MPI — Message Passing Interface

Dos ejemplos mínimos de MPI usando [`mpi4py`](https://mpi4py.readthedocs.io/) (bindings de Python sobre una implementación MPI real).

Elegimos **Python por legibilidad**: el código se lee casi como pseudocódigo y deja a la vista lo único que importa acá — el patrón de comunicación. En producción MPI se usa con C/C++/Fortran sobre supercomputadoras, pero los conceptos (rank, contexto compartido, operaciones colectivas y punto a punto) son idénticos.

## Idea central

Todos los procesos corren **el mismo programa**, arrancan y terminan **en simultáneo** y comparten un **mismo contexto** (`MPI.COMM_WORLD`). Lo único que distingue a un proceso de otro es su **rank** (su id). Por convención, el rank `0` es el "padre" que suele generar y repartir la data.

Esto matchea lo que dice la teórica: MPI es transparente para el usuario (no programás sockets a mano), pero a cambio exige un entorno homogéneo y no tolera fallas — si un proceso muere, muere todo.

## Ejemplos

| Archivo | Patrón | Qué muestra |
|---------|--------|-------------|
| `scatter_reduce.py` | Colectivo | El padre reparte chunks (`scatter`) y agrega resultados (`reduce`) |
| `ring.py` | Punto a punto | `send` / `recv` bloqueantes pasando un token en anillo |

## Prerrequisitos

`mpi4py` necesita una implementación de MPI instalada en el sistema.

```bash
# macOS
brew install open-mpi

# Debian/Ubuntu
sudo apt install -y libopenmpi-dev openmpi-bin

# luego, los bindings de Python
pip install -r requirements.txt
```

## Cómo correr

`mpirun -np N` lanza `N` procesos del mismo script.

```bash
# Colectivo: scatter + reduce con 4 procesos
mpirun -np 4 python3 scatter_reduce.py

# Punto a punto: token en anillo con 4 procesos
mpirun -np 4 python3 ring.py
```

### Salida esperada (`scatter_reduce.py`, 4 procesos)

```
[rank 0] (padre) data completa: [1, 2, ..., 20]
[rank 0] chunk=[1, 5, 9, 13, 17] -> suma parcial=45
[rank 1] chunk=[2, 6, 10, 14, 18] -> suma parcial=50
[rank 2] chunk=[3, 7, 11, 15, 19] -> suma parcial=55
[rank 3] chunk=[4, 8, 12, 16, 20] -> suma parcial=60
[rank 0] (padre) suma total = 210 (esperado 210)
```

> El orden de las líneas intermedias puede variar: los procesos imprimen en paralelo.
