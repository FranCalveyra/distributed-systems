# Chord — Distributed Hash Table

**Python**, porque acá lo que importa es la estructura de datos y el algoritmo de lookup, no concurrencia real. Chord es "el representante típico" de sistemas de naming basados en DHT que menciona la teórica (junto a otros sistemas de la última década).

## Idea central

- Nodos y claves se hashean al **mismo espacio circular** de `2^m` IDs (consistent hashing). Acá se usa SHA-1 truncado a `m=8` bits → anillo de 256 posiciones.
- Una clave la **posee** el primer nodo cuyo ID es `>=` al hash de la clave, recorriendo el anillo en sentido horario (su *sucesor*).
- Cada nodo mantiene una **finger table** de tamaño `m`: `finger[i]` apunta al sucesor de `(node.id + 2^i) mod 2^m`. Como los saltos crecen exponencialmente, una búsqueda resuelve en **O(log N)** en vez de caminar el anillo nodo por nodo (`O(N)`).

## Cómo correr

```bash
python3 chord.py
```

## Qué muestra la salida

- El anillo completo con el sucesor y la finger table de cada uno de los 8 nodos.
- Para cada clave de ejemplo: a qué nodo la asigna el hashing, y la comparación de saltos entre:
  - **Lookup con finger table** (el real de Chord): 1-2 saltos.
  - **Lookup lineal** (ir de sucesor en sucesor sin atajos): 3-6 saltos.

Con 8 nodos, `log2(8) = 3` — el finger table efectivamente acota la búsqueda a ese orden, mientras que el lookup lineal escala con la cantidad total de nodos.

## Relación con la teoría

- Esto resuelve el problema que tienen el **flat naming** simple y el **forwarding pointers**: no hay un único punto de entrada ni cadenas largas que haya que recorrer secuencialmente.
- A diferencia de DNS (jerárquico, con nombres legibles para humanos), Chord resuelve **identificadores planos** — el "cómo resolver un identificador en la dirección de la entidad asociada" que menciona `naming.md` antes de introducir DHTs.
