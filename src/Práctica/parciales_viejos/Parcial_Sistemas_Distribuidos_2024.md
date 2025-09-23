# Parcial 1 2024
1. En los sistemas distribuidos generalmente se consideran las capas del stack OSI:
   - a. Capa de enlace
   - b. Capa física
   - c. Capa de red
   - d. Capa de transporte/sesión/presentación y aplicación

2. El protocolo "Transmission Control Protocol" se usa en los S.D porque permite:
   - a. Minimizar el número de paquetes que se envían por las redes
   - b. Minimizar la latencia en las comunicaciones
   - c. Disminuir los errores en las comunicaciones
   - d. Garantizar la seguridad

3. Cuando se menciona que un middleware puede ser usado por muchas aplicaciones diferentes, esto implica:
   - a. Los protocolos de la capa física no son necesarios.
   - b. Tener la capacidad de poder usar/integrar distintos tipos de protocolos
   - c. Las aplicaciones deben usar los mismos protocolos de comunicación
   - d. Los sistemas donde se ejecutan esas aplicaciones tienen la misma capacidad y tipo

4. Cuando se trabaja con un protocolo `host-to-host` se establece una comunicación entre:
   - a. Distintos protocolos
   - b. Distintas aplicaciones
   - c. Sistemas operativos del mismo o diferentes tipos
   - d. Middlewares

5. Una comunicación síncrona implica
   - a. Establecer 3 momentos o etapas: envío, entrega y procesamiento
   - b. Evitar la espera de la respuesta del servidor o del cliente
   - c. Contar con sistemas de almacenamiento que registren el estado y datos de la comunicación
   - d. Que las comunicaciones sean obligatoriamente persistentes

6. Para el esquema de comunicación cliente/servidor se establecen:
   - a. Comunicaciones persistentes
   - b. Comunicaciones síncronas
   - c. Comunicaciones transitorias
   - d. Bloqueos durante la comunicación de parte del cliente y no del servidor

7. Una comunicación persistente y asíncrona implica
   - a. Gestión de colas de mensajes
   - b. Dependencias de aplicaciones intermedias que aseguren la tolerancia a fallas
   - c. Modelo Cliente/Servidor
   - d. Bloqueo para espera de confirmación de envío o recepción

8. RPC involucra:
   - a. Comunicación síncrona
   - b. Sockets
   - c. Gestión de conversión o adaptación de las funciones invocadas
   - d. No se permite el uso de variables globales

9.  MPI involucra:
   - a.  Intercambio de objetos
   - b.  Gestión de MQ (colas de mensajes)
   - c.  Ejecución de tareas en varios cores y/o computadoras
   - d.  Comunicaciones síncronas o asíncronas

10. Una comunicación asíncrona persistente incluye:
    - a.  Intercambio de mensajes
    - b.  Middlewares para la gestión de mensajes
    - c.  Buffers para la comunicación
    - d.  Operaciones básicas para el envío y recepción

11. El intercambio de mensajes basado en brokers:
    - a.  Se usa para aplicaciones homogéneas
    - b.  Se usa en modelos Pub/Sub
    - c.  Se usa para aplicaciones heterogéneas
    - d.  La gestión de MQ se realiza en nodos que se comunican

12. Para establecer un envío multicast:
    - a.  Solo se pueden usar arquitecturas de computadoras en forma de árbol
    - b.  Siempre se requiere un sistema de routing
    - c.  Es posible aumentar la latencia por saturación de los canales de comunicación
    - d.  Se necesita comunicación directa entre nodos

13. Un esquema de comunicación basado en flooding:
    - a.  Es más eficiente mientras más nodos contenga la red
    - b.  Siempre debe contener nodos edge
    - c.  El envío de mensajes se hace solo al nodo más cercano
    - d.  Se seleccionan los vecinos según el desempeño de la comunicación entre nodos

14. Un sistema distribuido centralizado
    - a.  Usa varios nodos centrales para controlar las comunicaciones
    - b.  Usa una estructura en malla para establecer las comunicaciones
    - c.  No es un sistema distribuido
    - d.  La centralización se basa en la forma en cómo se estructura la red de comunicación

15. ¿Qué significa que un sistema distribuido es un sistema informático en red en el que los procesos y recursos están suficientemente distribuidos entre varias computadoras?
    - a.  Que todos los procesos pertenecen a diferentes computadoras
    - b.  Que todos los recursos están en diferentes computadoras
    - c.  Que algunos de los procesos y recursos están en diferentes computadoras o dispositivos
    - d.  Que una computadora ejecute un solo proceso o contenga un solo recurso

16. El escalamiento en un S.D depende de:
    - a.  Los protocolos de comunicación que se usen
    - b.  De las aplicaciones que se usen
    - c.  Del tipo de usuario que se considere
    - d.  De las APIs con las que se cuente

17. La distribución lógica y física considera:
    - a.  La forma en que las organizaciones (individuos) participan
    - b.  Las aplicaciones utilizadas
    - c.  El tipo de red utilizado
    - d.  Los protocolos de comunicación

18. Cuando las aplicaciones son independientes a los algoritmos
    - a.  Se pueden usar diferentes arquitecturas de computadoras para el mismo algoritmo
    - b.  Todos los algoritmos son independientes a todas las aplicaciones
    - c.  Todas las aplicaciones son independientes de cualquier algoritmo
    - d.  Un algoritmo puede ser implementado en diferentes aplicaciones

19. La transparencia en la distribución implica:
    - a.  Tener un middleware
    - b.  Tener una sola aplicación que le permita al usuario integrar todos los recursos y procesos, en una única interfaz visual.
    - c.  Que el usuario no conozca los detalles de la forma en que se comunican los procesos
    - d.  Que el usuario administre cada recurso de forma transparente

20. Para distinguir entre la latencia y las fallas, se puede usar:
    - a.  El tiempo como única métrica de detección
    - b.  Protocolos que usen estrategias de confirmación de recepción de mensajes
    - c.  Un registro de los tiempos de respuesta
    - d.  Un tiempo máximo de espera

21. Entre las similitudes entre políticas y mecanismos están
    - a.  La política y el mecanismo proviene de una decisión organizacional
    - b.  La forma de implementación
    - c.  Se usan como conceptos análogos
    - d.  Ninguna de las anteriores

22. Cuando un S.D permite agregar dominios de forma transparente al usuario se está refiriendo a:
    - a.  Escalabilidad administrativa
    - b.  Escalabilidad geográfica
    - c.  Escalabilidad de procesos
    - d.  Todas las anteriores

23. Entre las semejanzas entre un S.D y uno paralelo están:
    - a.  Tener diferentes clocks
    - b.  Tener el mismo clock
    - c.  Tener múltiples procesadores o cores en una o varias computadoras
    - d.  Tener procesadores de alto rendimiento en todos los sistemas

24. La memoria virtual sirve para:
    - a.  Implementar memoria compartida
    - b.  Extender la capacidad real de la memoria física
    - c.  Virtualizar el almacenamiento secundario
    - d.  Todas las anteriores

25. Un S.D local o clúster cuenta con:
    - a.  Un mismo clock para todos los nodos
    - b.  Un clock diferente para c/nodo
    - c.  Un nodo coordinador
    - d.  Distribución de datos y/o instrucciones

26. En un S.D se usa una arquitectura multicapa para:
    - a.  Disminuir la cantidad de protocolos de comunicación
    - b.  Descomponer el proceso de comunicación en tareas más simples
    - c.  Aumentar el grado de confiabilidad en las comunicaciones
    - d.  Tener un mejor control en el manejo de errores

27. En una arquitectura orientada o basada en objetos:
    - a.  Un objeto representa un solo nodo o computadora en el sistema
    - b.  Un dispositivo en el sistema puede manejar varios objetos
    - c.  La estrategia es distribuir las tareas entre objetos independientemente de los nodos del sistema
    - d.  Un objeto puede resolver una única tarea particular solamente

28. En una arquitectura REST se busca:
    - a.  Disminuir la cantidad de tipos de operaciones para facilitar la integración entre nodos en el sistema
    - b.  Los recursos son manejados y controlados de forma compartida
    - c.  Los recursos están distribuidos y se acceden a través de protocolos compatibles con REST
    - d.  Ninguna de las anteriores

29. En un S.D una interfaz permite
    - a.  Comunicación entre aplicaciones del mismo tipo
    - b.  Comunicación entre aplicaciones de distinto tipo
    - c.  Comunicación entre dispositivos iguales
    - d.  Comunicación entre dispositivos diferentes

30. Entre las ventajas de tener un coordinador en un S.D están:
    - a.  Aumentar el control de la comunicación entre nodos
    - b.  Aumentar la seguridad del sistema
    - c.  Aumentar la coherencia de datos
    - d.  Evitar SPoFs (Single Points of Failure)

31. En cuanto a un middleware, se puede afirmar:
    - a.  Que es un intermediario entre HW y SW.
    - b.  Que es un sistema compuesto por varias aplicaciones
    - c.  Que es un sistema que ofrece al usuario la capacidad de uso de diferentes sistemas operativos
    - d.  Todas las anteriores

32. Un wrapper siempre usa:
    - a.  Un nodo broker que intermedia entre aplicaciones que no están diseñadas para la comunicación entre nodos o dispositivos
    - b.  Un hardware o software intermediario entre aplicaciones que carecen de APIs para proveer interacción con otros nodos
    - c.  Una capa de software adicional que le permite a una aplicación interactuar con otra
    - d.  Una capa de hardware adicional que le permite a un nodo interactuar con otro

33. Un modelo cliente/servidor puede ser considerado como:
    - a.  Una arquitectura descentralizada
    - b.  Una arquitectura centralizada
    - c.  Un modelo diseñado para la comunicación entre varios nodos clientes y varias réplicas de un servidor.
    - d.  Un modelo diseñado para proveer servicios a varios nodos clientes

34. En cuanto a una arquitectura NFS:
    - a.  Se la puede considerar P2P
    - b.  Se puede considerar un modelo cliente/servidor de uso particular
    - c.  Se le puede considerar un modelo en capas
    - d.  Todas las anteriores

35. Un sistema P2P desestructurado se usa para:
    - a.  Conformar un anillo de comunicación entre nodos para tomar una decisión entre los mismos
    - b.  Seleccionar un nodo líder o coordinador
    - c.  Sincronizar el tiempo entre todos los nodos
    - d.  Todas las anteriores

36. Un sistema de Cloud Computing ofrece servicios:
    - a.  Orientados a Infraestructura
    - b.  Orientados a Middleware
    - c.  Orientados a Software
    - d.  Orientados a Plataforma

37. Los sistemas edge:
    - a.  Son estructurados en forma de hipercubos o mallas
    - b.  El nivel de latencia es alto, el nivel de confiabilidad y seguridad es bajo
    - c.  Son estructurados en forma de anillo
    - d.  Ninguna de las anteriores

38. Para un sistema basado en blockchain
    - a.  Se usan cadenas de bloques independientes y totalmente diferentes en varios nodos
    - b.  Procura mantener una sola versión válida de la cadena de bloques distribuida (replicada)
    - c.  Un nodo coordinador decide sobre la validez de los bloques en la cadena
    - d.  Se hacen réplicas de la cadena de bloques en diferentes nodos

39. Se puede afirmar que un proceso y un thread
    - a.  Pueden ejecutar un mismo programa
    - b.  Son conceptos totalmente separados
    - c.  Los threads representan varias ejecuciones de un mismo proceso
    - d.  Un proceso puede compartir sus recursos entre los threads del mismo proceso

40. Un S.D tiene entre sus objetivos principales
    - a.  Disminuir la latencia en la ejecución de un thread
    - b.  Aumentar el rendimiento de aplicaciones no paralelizables
    - c.  Mejorar la performance de la ejecución de tareas
    - d.  Aumentar la capacidad de cómputo y almacenamiento

---

## Mis Respuestas

### Pregunta 1
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 2
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 3
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 4
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 5
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 6
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 7
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 8
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 9
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 10
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 11
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 12
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 13
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 14
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 15
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 16
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 17
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 18
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 19
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 20
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 21
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 22
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 23
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 24
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 25
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 26
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 27
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 28
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 29
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 30
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 31
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 32
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 33
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 34
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 35
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 36
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 37
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 38
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 39
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 

### Pregunta 40
**Respuesta:** ( ) a. ( ) b. ( ) c. ( ) d. \
**Justificación:** 
