# Guía Consistencia y Replicación
### Ejercicio 1
¿Por qué replicar?

### Respuesta
Para aumentar la confiabilidad del sistema (ej: replicas un servicio, cosa de que si se cae, el sistema sigue funcionando porque lo reemplazas por su réplica), o para aumentar su rendimiento (ej: replicas un servicio y usas un Load Balancer cosa de que si se llena la instancia principal, redirigis el tráfico a la réplica, pudiendo atender más solicitudes).

### Ejercicio 2
¿Qué problema puede ocurrir cuando se tienen múltiples copias?

### Respuesta
Yace el problema inherente de mantener la consistencia de las copias, y la coherencia entre las mismas, justamente.

### Ejercicio 3
¿Existe alguna relación entre la replicación y la escalabilidad? Explicar.

### Respuesta
Colocar copias de datos cerca de los procesos que los usan puede mejorar el rendimiento mediante la reducción del tiempo de acceso. Y entonces se resuelven problemas de escalabilidad.

Sumado a eso, mantener varias copias consistentes puede estar sujeto a problemas de escalabilidad. Entre más copias quiero mantener, más complicado se vuelve mantenerlas consistentes.

### Ejercicio 4
Defina brevemente qué es un modelo de consistencia.

### Respuesta
Es un contrato entre los procesos y el almacén de datos. Son las "normas" que se van a respetar entre los procesos y el data store para asegurar un cierto tipo de consistencia

### Ejercicio 5
En general, ¿en qué se diferencian los modelos de consistencia centrados en datos de aquellos modelos de consistencia centrados en el cliente?

### Respuesta
La consistencia centrada en datos intenta mantener la consistencia de todo el sistema para todos los clientes por igual, es decir, la _consistencia de todos los datos_, mientras que la centrada en el cliente trata de que el cliente que consulta el data store vea algo consistente **para él**, no importa si para otros clientes es inconsistente.

### Ejercicio 6
##### Actividad no obligatoria:
Actividad de tutorial guiado para el desarrollo de un smart contract en Ethereum “Pet Shop Tutorial”.
1. Ingresar al siguiente link, el cual tiene las instrucciones para seguir el tutorial para desarrollar tu primer “Smart Contract” en Ethereum:
   1. [https://archive.trufflesuite.com/guides/pet-shop/](https://archive.trufflesuite.com/guides/pet-shop/)
2. En este tutorial guiado, encontrarás las herramientas: node, git, ganache y los comandos node para descargar el box “pet shop tutorial” con la estructura de directorio lista para empezar a programar.
3. Te dejamos los siguientes links que también están en el tutorial guiado, para instalar las herramientas. Si ya tenés node y git instalados, no necesitás instalarlos otra vez.
 - [Node](https://nodejs.org/en/)
 - [GIT](https://git-scm.com/)
 - [Ganache](https://archive.trufflesuite.com/ganache/) 
   - Sirve para crear una Blockchain Ethereum interna (solo para desarrollo local y pruebas) 
4. Realizá el tutorial solo hasta el testing del smart contract en Ethereum. Corré los test, y observá los resultados en Ganache

### Respuesta
<!-- TODO: implementarlo -->
[Link a la implementación](https://github.com/FranCalveyra/distributed-systems/tree/main/src/Pr%C3%A1ctica/consistencia_replicacion/pet-shop-tutorial)
