# Parcial 1 2024
1. En los sistemas distribuidos generalmente se consideran las capas del stack OSI:
   1. Capa de enlace
   2. Capa física
   3. Capa de red
   4. Capa de transporte/sesión/presentación y aplicación
2. El protocolo "Transmission Control Protocol" se usa en los S.D porque permite:
   1. Minimizar el número de paquetes que se envían por las redes
   2. Minimizar la latencia en las comunicaciones
   3. Disminuir los errores en las comunicaciones
   4. Garantizar la seguridad
3. Cuando se menciona que un middleware puede ser usado por muchas aplicaciones diferentes, esto implica:
   1. Los protocolos de la capa física no son necesarios.
   2. Tener la capacidad de poder usar/integrar distintos tipos de protocolos
   3. Las aplicaciones deben usar los mismos protocolos de comunicación
   4. Los sistemas donde se ejecutan esas aplicaciones tienen la misma capacidad y tipo
4. Cuando se trabaja con un protocolo `host-to-host` se establece una comunicación entre:
   1. Distintos protocolos
   2. Distintas aplicaciones
   3. Sistemas operativos del mismo o diferentes tipos
   4. Middlewares
5. Una comunicación síncrona implica
   1. Establecer 3 momentos o etapas: envío, entrega y procesamiento
   2. Evitar la espera de la respuesta del servidor o del cliente
   3. Contar con sistemas de almacenamiento que registren el estado y datos de la comunicación
   4. Que las comunicaciones sean obligatoriamente persistentes
6. Para el esquema de comunicación cliente/servidor se establecen:
   1. Comunicaciones persistentes
   2. Comunicaciones síncronas
   3. Comunicaciones transitorias
   4. Bloqueos durante la comunicación de parte del cliente y no del servidor
7. Una comunicación persistente y asíncrona implica
   1. Gestión de colas de mensajes
   2. Dependencias de aplicaciones intermedias que aseguren la tolerancia a fallas
   3. Modelo Cliente/Servidor
   4. Bloqueo para espera de confirmación de envío o recepción
8. RPC involucra:
   1. Comunicación síncrona
   2. Sockets
   3. Gestión de conversión o adaptación de las funciones invocadas
   4. No se permite el uso de variables globales
9. MPI involucra:
   1.  Intercambio de objetos
   2.  Gestión de MQ (colas de mensajes)
   3.  Ejecución de tareas en varios cores y/o computadoras
   4.  Comunicaciones síncronas o asíncronas
10. Una comunicación asíncrona persistente incluye:
    1.  Intercambio de mensajes
    2.  Middlewares para la gestión de mensajes
    3.  Buffers para la comunicación
    4.  Operaciones básicas para el envío y recepción
11. El intercambio de mensajes basado en brokers:
    1.  Se usa para aplicaciones homogéneas
    2.  Se usa en modelos Pub/Sub
    3.  Se usa para aplicacioens heterogéneas
    4.  La gestión de MQ se realiza en nodos que se comunican
12. Para establecer un envío multicast:
    1.  Solo se pueden usar arquitecturas de computadoras en forma de árbol
    2.  Siempre se requiere un sistema de routing
    3.  Es posible aumentar la latencia por saturación de los canales de comunicación
    4.  Se necesita comunicación directa entre nodos
13. Un esquema de comunicación basado en flooding:
    1.  Es más eficiente mientras más nodos contenga la red
    2.  Siempre debe contener nodos edge
    3.  El envío de mensajes se hace solo al nodo más cercano
    4.  Se seleccionan los vecinos según el desempeño de la comunicación entre nodos
14. Un sistema distribuido centralizado
    1.  Usa varios nodos centrales para controlar las comunicaciones
    2.  Usa una estructura en malla para establecer las comunicaciones
    3.  No es un sistema distribuido
    4.  La centralización se basa en la forma en cómo se estructura la red de comunicación
15. ¿Qué significa que un sistema distribuido es un sistema informático en red en el que los procesos y recursos están suficientemente distribuidos entre varias computadoras?
    1.  Que todos los procesos pertenecen a diferentes computadoras
    2.  Que todos los recursos están en diferentes computadoras
    3.  Que algunos de los procesos y recursos están en diferentes computadoras o dispositivos
    4.  Que una computadora ejecute un solo proceso o contenga un solo recurso
16. El escalamiento en un S.D depende de:
    1.  Los protocolos de comunicación que se usen
    2.  De las aplicaciones que se usen
    3.  Del tipo de usuario que se considere
    4.  De las APIs con las que se cuente
17. La distribución lógica y física considera:
    1.  La forma en que las organizaciones (individuos) participan
    2.  Las aplicaciones utilizadas
    3.  El tipo de red utilizado
    4.  Los protocolos de comunicación
18. Cuando las aplicaciones son independientes a los algoritmos
    1.  Se pueden usar diferentes arquitecturas de computadoras para el mismo algoritmo
    2.  Todos los algoritmos son independientes a todas las aplicaciones
    3.  Todas las aplicaciones son independientes de cualquier algoritmo
    4.  Un algoritmo puede ser implementado en diferentes aplicaciones
19. La transparencia en la distribución implica:
    1.  Tener un middleware
    2.  Tener una sola aplicación que le permita al usuario integrar todos los recursos y procesos, en una única interfaz visual.
    3.  Que el usuario no conozca los detalles de la forma en que se comunican los procesos
    4.  Que el usuario administre cada recurso de forma transparente
20. Para distinguir entre la latencia y las fallas, se puede usar:
    1.  El tiempo como única métrica de detección
    2.  Protocolos que usen estrategias de confirmación de recepción de mensajes
    3.  Un registro de los tiempos de respuesta
    4.  Un tiempo máximo de espera
21. Entre las similitudes entre políticas y mecanismos están
    1.  La política y el mecanismo proviene de una decisión organizacional
    2.  La forma de implementación
    3.  Se usan como conceptos análogos
    4.  Ninguna de las anteriores
22. Cuando un S.D permite agregar dominios de forma transparente al usuario se está refiriendo a:
    1.  Escalabilidad administrativa
    2.  Escalabilidad geográfica
    3.  Escalabilidad de procesos
    4.  Todas las anteriores
23. Entre las semejanzas entre un S.D y uno paralelo están:
    1.  Tener diferentes clocks
    2.  Tener el mismo clock
    3.  Tener múltiples procesadores o cores en una o varias computadoras
    4.  Tener procesadores de alto rendimiento en todos los sistemas
24. La memoria virtual sirve para:
    1.  Implementar memoria compartida
    2.  Extender la capacidad real de la memoria física
    3.  Virtualizar el almacenamiento secundario
    4.  Todas las anteriores
25. Un S.D local o clúster cuenta con:
    1.  Un mismo clock para todos los nodos
    2.  Un clock diferente para c/nodo
    3.  Un nodo coordinador
    4.  Distribución de datos y/o instrucciones
26. En un S.D se usa una arquitectura multicapa para:
    1.  Disminuir la cantidad de protocolos de comunicación
    2.  Descomponer el proceso de comunicación en tareas más simples
    3.  Aumentar el grado de confiabilidad en las comunicaciones
    4.  Tener un mejor control en el manejo de errores
27. En una arquitectura orientada o basada en objetos:
    1.  Un objeto representa un solo nodo o computadora en el sistema
    2.  Un dispositivo en el sistema puede manejar varios objetos
    3.  La estrategia es distribuir las tareas entre objetos independientemente de los nodos del sistema
    4.  Un objeto puede resolver una única tarea particular solamente
28. En una arquitectura REST se busca:
    1.  Disminuir la cantidad de tipos de operaciones para facilitar la integración entre nodos en el sistema
    2.  Los recursos son manejados y controlados de forma compartida
    3.  Los recursos están distribuidos y se acceden a través de protocolos compatibles con REST
    4.  Ninguna de las anteriores
29. En un S.D una interfaz permite
    1.  Comunicación entre aplicaciones del mismo tipo
    2.  Comunicación entre aplicaciones de distinto tipo
    3.  Comunicación entre dispositivos iguales
    4.  Comunicación entre dispositivos diferentes
30. Entre las ventajas de tener un coordinador en un S.D están:
    1.  Aumentar el control de la comunicación entre nodos
    2.  Aumentar la seguridad del sistema
    3.  Aumentar la coherencia de datos
    4.  Evitar SPoFs (Single Points of Failure)
31. En cuanto a un middleware, se puede afirmar:
    1.  Que es un intermediario entre HW y SW.
    2.  Que es un sistema compuesto por varias aplicaciones
    3.  Que es un sistema que ofrece al usuario la capacidad de uso de diferentes sistemas operativos
    4.  Todas las anteriores
32. Un wrapper siempre usa:
    1.  Un nodo broker que intermedia entre aplicaciones que no están diseñadas para la comunicación entre nodos o dispositivos
    2.  Un hardware o software intermediario entre aplicaciones que carecen de APIs para proveer interacción con otros nodos
    3.  Una capa de software adicional que le permite a una aplicación interactuar con otra
    4.  Una capa de hardware adicional que le permite a un nodo interactuar con otro
33. Un modelo cliente/servidor puede ser considerado como:
    1.  Una arquitectura descentralizada
    2.  Una arquitectura descentralizada
    3.  Un modelo diseñado para la comunicación entre varios nodos clientes y varias réplicas de un servidor.
    4.  Un modelo diseñado para proveer servicios a varios nodos clientes
34. En cuanto a una arquitectura NFS:
    1.  Se la puede considerar P2P
    2.  Se puede considerar un modelo cliente/servidor de uso particular
    3.  Se le puede considerar un modelo en capas
    4.  Todas las anteriores
35. Un sistema P2P desestructurado se usa para:
    1.  Conformar un anillo de comunicación entre nodos para tomar una decisión entre los mismos
    2.  Seleccionar un nodo líder o coordinador
    3.  Sincronizar el tiempo entre todos los nodos
    4.  Todas las anteriores
36. Un sistema de Cloud Computing ofrece servicios:
    1.  Orientados a Infraestructura
    2.  Orientados a Middleware
    3.  Orientados a Software
    4.  Orientados a Plataforma
37. Los sistemas edge:
    1.  Son estructurados en forma de hipercubos o mallas
    2.  El nivel de latencia es alto, el nivel de confiabilidad y seguridad es bajo
    3.  Son estructurados en forma de anillo
    4.  Ninguna de las anteriores
38. Para un sistema basado en blockchain
    1.  Se usan cadenas de bloques independientes y totalmente diferentes en varios nodos
    2.  Procura mantener una sola versión válida de la cadena de bloques distribuida (replicada)
    3.  Un nodo coordinador decide sobre la validez de los bloques en la cadena
    4.  Se hacen réplicas de la cadena de bloque en diferentes nodos
39. Se puede afirmar que un proceso y un thread
    1.  Pueden ejecutar un mismo programa
    2.  Son conceptos totalmente separados
    3.  Los threads representan varias ejecuciones de un mismo proceso
    4.  Un proceso puede compartir sus recursos entre los threads del mismo proceso
40. Un S.D tiene entre sus objetivos principales
    1.  Disminuir la latencia en la ejecución de un thread
    2.  Aumentar el rendimiento de aplicaciones no paralelizables
    3.  Mejorar la performance de la ejecución de tareas
    4.  Aumentar la capacidad de cómputo y almacenamiento