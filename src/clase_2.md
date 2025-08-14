# Clase 2
Un sistema distribuido es uno que involucra varios dispositivos que se comunican a través de la red, y trabajan en conjunto con tal de lograr un objetivo en común.

**¿Qué diferencia tiene respecto a un sistema paralelo/concurrente?**
- Los distribuidos involucran diferentes dispositivos, mientras que los concurrentes son parte del mismo dispositivo.
- Los distribuidos están "un nivel por encima".
- Un sistema distribuido (SD), al contrario de un sistema paralelo (memoria compartida + clock único), tiene distintos clocks (ergo noción del tiempo). Más específicamente, cada nodo tiene su propio clock.

**¿Qué problemas podemos llegar a tener?**
- Saber quién llegó primero a realizar una solicitud.
  - Un nodo puede tener un registro de un mensaje en tal hora, y que otro tenga el mismo, pero sin considerar la latencia que hay entre nodos por su distancia.

En SDs, siempre terminamos haciendo estimaciones en cuanto al tiempo, como en Análisis Numérico.

## Un sistema distribuido puede ser...
- **Centralizado**: el control lo tiene un ente central.
  - Depende organizativamente de una cierta toma de decisiones.
  - Depende de quién toma la decisión, no cómo se toma a nivel de hardware.
  - A pesar de haber varias instancias o un cluster de nodos, se puede dar el caso en el que tomen la decisión de manera autónoma, sin pedirle permiso a otros.
- **Descentralizado**: el control se distribuye entre varios nodos.
  - Las decisiones las toman varios nodos.
  - Surgen nuevos problemas, como qué esquema de votación se implementa.

Esta clasificación depende de:
- Donde guardo los datos
- Cómo se distribuye el control y gestión de los datos
- Ubicación de los nodos

La distribución del sistema **siempre debe ser transparente**. La forma de actuar con el sistema debe ser la misma, independientemente de dónde me encuentre.