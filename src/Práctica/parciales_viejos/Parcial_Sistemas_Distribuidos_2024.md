# Parcial 1 2024
1. En los sistemas distribuidos generalmente se consideran las capas del stack OSI:
   - [ ] a. Capa de enlace
   - [ ] b. Capa física
   - [x] c. Capa de red
   - [x] d. Capa de transporte/sesión/presentación y aplicación

   **Justificación:** 

2. El protocolo "Transmission Control Protocol" se usa en los S.D porque permite:
   - [ ] a. Minimizar el número de paquetes que se envían por las redes
   - [ ] b. Minimizar la latencia en las comunicaciones
   - [x] c. Disminuir los errores en las comunicaciones
   - [ ] d. Garantizar la seguridad

   **Justificación:** 

3. Cuando se menciona que un middleware puede ser usado por muchas aplicaciones diferentes, esto implica:
   - [ ] a. Los protocolos de la capa física no son necesarios.
   - [x] b. Tener la capacidad de poder usar/integrar distintos tipos de protocolos
   - [ ] c. Las aplicaciones deben usar los mismos protocolos de comunicación
   - [ ] d. Los sistemas donde se ejecutan esas aplicaciones tienen la misma capacidad y tipo

   **Justificación:** 

4. Cuando se trabaja con un protocolo `host-to-host` se establece una comunicación entre:
   - [ ] a. Distintos protocolos
   - [ ] b. Distintas aplicaciones
   - [x] c. Sistemas operativos del mismo o diferentes tipos
   - [ ] d. Middlewares

   **Justificación:** 

5. Una comunicación síncrona implica
   - [x] a. Establecer 3 momentos o etapas: envío, entrega y procesamiento
   - [ ] b. Evitar la espera de la respuesta del servidor o del cliente
   - [x] c. Contar con sistemas de almacenamiento que registren el estado y datos de la comunicación
   - [ ] d. Que las comunicaciones sean obligatoriamente persistentes

   **Justificación:** "almacenamiento" no implica que haya persistencia de la comunicación. Puede quedar en memoria y luego esfumarse.

6. Para el esquema de comunicación cliente/servidor se establecen:
   - [x] a. Comunicaciones persistentes
   - [x] b. Comunicaciones síncronas
   - [x] c. Comunicaciones transitorias
   - [x] d. Bloqueos durante la comunicación de parte del cliente y no del servidor

   **Justificación:** si bien son cosas típicas del modelo cliente/servidor, no necesariamente lo van a incluir siempre

7. Una comunicación persistente y asíncrona implica
   - [x] a. Gestión de colas de mensajes
   - [ ] b. Dependencias de aplicaciones intermedias que aseguren la tolerancia a fallas
   - [ ] c. Modelo Cliente/Servidor
   - [ ] d. Bloqueo para espera de confirmación de envío o recepción

   **Justificación:** No necesariamente tienen que **asegurar** la tolerancia a fallas, mucho menos ser parte del modelo cliente servidor. Puede haber un esquema Pub/Sub donde ningún nodo es un servidor, y las colas de mensajería administran los mensajes enviados en este tipo de comunicación. Como es asíncrona, no hay bloqueo por espera de confirmación de envío ni recepción

8. RPC involucra:
   - [x] a. Comunicación síncrona
   - [x] b. Sockets
   - [x] c. Gestión de conversión o adaptación de las funciones invocadas
   - [ ] d. No se permite el uso de variables globales

   **Justificación:** Permiten el uso de variables globales, justamente, teniendo referencias a objetos.

9.  MPI involucra:
    - [ ] a. Intercambio de objetos
    - [x] b. Gestión de MQ (colas de mensajes)
    - [x] c. Ejecución de tareas en varios cores y/o computadoras
    - [x] d. Comunicaciones síncronas o asíncronas

    **Justificación:** MPI permite sincronización de tareas ejecutadas en varios dispositivos, pero no la ejecución en sí

10. Una comunicación asíncrona persistente incluye:
    - [x] a.  Intercambio de mensajes
    - [x] b.  Middlewares para la gestión de mensajes
    - [x] c.  Buffers para la comunicación
    - [x] d.  Operaciones básicas para el envío y recepción

    **Justificación:** Si se quiere asincronismo y persistencia, necesariamente tiene que haber un buffer de comunicación, que puede ser interpretado de alguna manera como middleware. Las otras 2 son básicas de cualquier tipo de comunicación.

11. El intercambio de mensajes basado en brokers:
    - [ ] a.  Se usa para aplicaciones homogéneas
    - [x] b.  Se usa en modelos Pub/Sub
    - [x] c.  Se usa para aplicaciones heterogéneas
    - [ ] d.  La gestión de MQ se realiza en nodos que se comunican

    **Justificación:** Los brokers siguen como capa de abstracción de alguna manera. Justamente las colas de mensajería son procesos/nodos aparte de los nodos que quieren comunicarse. Si la aplicación es homogénea, ¿para qué querés una cola de mensajería?

12. Para establecer un envío multicast:
    - [ ] a.  Solo se pueden usar arquitecturas de computadoras en forma de árbol
    - [ ] b.  Siempre se requiere un sistema de routing
    - [x] c.  Es posible aumentar la latencia por saturación de los canales de comunicación
    - [ ] d.  Se necesita comunicación directa entre nodos

    **Justificación:** No siempre tienen que ser arquitecturas en forma de árbol. El enrutamiento se requiere si la arquitectura es de tipo mesh

13. Un esquema de comunicación basado en flooding:
    - [x] a.  Es más eficiente mientras más nodos contenga la red
    - [ ] b.  Siempre debe contener nodos edge
    - [ ] c.  El envío de mensajes se hace solo al nodo más cercano
    - [x] d.  Se seleccionan los vecinos según el desempeño de la comunicación entre nodos

    **Justificación:** Flooding toma un nodo, ese nodo le envía mensajes a todos sus vecinos excepto a quien le haya mandado el mensaje, lo cual está directamente relacionado con el desempeño de la red

14. Un sistema distribuido centralizado
    - [ ] a.  Usa varios nodos centrales para controlar las comunicaciones
    - [ ] b.  Usa una estructura en malla para establecer las comunicaciones
    - [ ] c.  No es un sistema distribuido
    - [x] d.  La centralización se basa en la forma en cómo se estructura la red de comunicación

    **Justificación:** No necesariamente van a usar varios nodos centrales, no es condición necesaria. La estructura en malla no tiene nada que ver. Justamente es un sistema distribuido.

15. ¿Qué significa que un sistema distribuido es un sistema informático en red en el que los procesos y recursos están suficientemente distribuidos entre varias computadoras?
    - [ ] a.  Que todos los procesos pertenecen a diferentes computadoras
    - [ ] b.  Que todos los recursos están en diferentes computadoras
    - [x] c.  Que algunos de los procesos y recursos están en diferentes computadoras o dispositivos
    - [ ] d.  Que una computadora ejecute un solo proceso o contenga un solo recurso

    **Justificación:** 

16. El escalamiento en un S.D depende de:
    - [x] a.  Los protocolos de comunicación que se usen
    - [x] b.  De las aplicaciones que se usen
    - [ ] c.  Del tipo de usuario que se considere
    - [x] d.  De las APIs con las que se cuente

    **Justificación:** Del tipo de usuario no depende en absoluto, pero sí de su cantidad. Es decir, la escala depende mucho del tráfico y uso del sistema.

17. La distribución lógica y física considera:
    - [x] a.  La forma en que las organizaciones (individuos) participan
    - [x] b.  Las aplicaciones utilizadas
    - [x] c.  El tipo de red utilizado
    - [x] d.  Los protocolos de comunicación

    **Justificación:** 

18. Cuando las aplicaciones son independientes a los algoritmos
    - [x] a.  Se pueden usar diferentes arquitecturas de computadoras para el mismo algoritmo
    - [ ] b.  Todos los algoritmos son independientes a todas las aplicaciones
    - [ ] c.  Todas las aplicaciones son independientes de cualquier algoritmo
    - [x] d.  Un algoritmo puede ser implementado en diferentes aplicaciones

    **Justificación:** 

19. La transparencia en la distribución implica:
    - [x] a.  Tener un middleware
    - [ ] b.  Tener una sola aplicación que le permita al usuario integrar todos los recursos y procesos, en una única interfaz visual.
    - [x] c.  Que el usuario no conozca los detalles de la forma en que se comunican los procesos
    - [ ] d.  Que el usuario administre cada recurso de forma transparente

    **Justificación:** 

20. Para distinguir entre la latencia y las fallas, se puede usar:
    - [ ] a.  El tiempo como única métrica de detección
    - [x] b.  Protocolos que usen estrategias de confirmación de recepción de mensajes
    - [x] c.  Un registro de los tiempos de respuesta
    - [x] d.  Un tiempo máximo de espera

    **Justificación:** 

21. Entre las similitudes entre políticas y mecanismos están
    - [ ] a.  La política y el mecanismo proviene de una decisión organizacional
    - [ ] b.  La forma de implementación
    - [ ] c.  Se usan como conceptos análogos
    - [x] d.  Ninguna de las anteriores

    **Justificación:** 

22. Cuando un S.D permite agregar dominios de forma transparente al usuario se está refiriendo a:
    - [x] a.  Escalabilidad administrativa
    - [ ] b.  Escalabilidad geográfica
    - [ ] c.  Escalabilidad de procesos
    - [ ] d.  Todas las anteriores

    **Justificación:** 

23. Entre las semejanzas entre un S.D y uno paralelo están:
    - [ ] a.  Tener diferentes clocks
    - [ ] b.  Tener el mismo clock
    - [x] c.  Tener múltiples procesadores o cores en una o varias computadoras
    - [ ] d.  Tener procesadores de alto rendimiento en todos los sistemas

    **Justificación:** No necesariamente vas a tener procesadores de alto rendimiento. Podes tener un sistema distribuido o paralelo tomando tu máquina personal como nodo. Los S.D tienen distintos clocks, mientras que los paralelos lo comparten.

24. La memoria virtual sirve para:
    - [x] a.  Implementar memoria compartida
    - [x] b.  Extender la capacidad real de la memoria física
    - [ ] c.  Virtualizar el almacenamiento secundario
    - [ ] d.  Todas las anteriores

    **Justificación:** 

25. Un S.D local o clúster cuenta con:
    - [x] a.  Un mismo clock para todos los nodos
    - [ ] b.  Un clock diferente para c/nodo
    - [x] c.  Un nodo coordinador
    - [x] d.  Distribución de datos y/o instrucciones

    **Justificación:** 

26. En un S.D se usa una arquitectura multicapa para:
    - [ ] a.  Disminuir la cantidad de protocolos de comunicación
    - [x] b.  Descomponer el proceso de comunicación en tareas más simples
    - [x] c.  Aumentar el grado de confiabilidad en las comunicaciones
    - [x] d.  Tener un mejor control en el manejo de errores

    **Justificación:** Justamente si tenés muchas capas podrías terminar teniendo varios protocolos de comunicación

27. En una arquitectura orientada o basada en objetos:
    - [ ] a.  Un objeto representa un solo nodo o computadora en el sistema
    - [x] b.  Un dispositivo en el sistema puede manejar varios objetos
    - [x] c.  La estrategia es distribuir las tareas entre objetos independientemente de los nodos del sistema
    - [ ] d.  Un objeto puede resolver una única tarea particular solamente

    **Justificación:** 

28. En una arquitectura REST se busca:
    - [x] a.  Disminuir la cantidad de tipos de operaciones para facilitar la integración entre nodos en el sistema
    - [ ] b.  Los recursos son manejados y controlados de forma compartida
    - [x] c.  Los recursos están distribuidos y se acceden a través de protocolos compatibles con REST
    - [ ] d.  Ninguna de las anteriores

    **Justificación:** La idea es que los nodos de esta arquitectura se acoplen a una cierta interfaz, y que las operaciones a realizar se limiten a los distintos métodos de HTTP. No necesariamente los recursos van a estar manejados y controlados de manera compartida, puesto que puedo tener una arquitectura REST con 1 solo servidor y N clientes, donde los recursos los termina manejando solo el server. La 3ra opción es solo una implicancia de una arquitectura REST

29. En un S.D una interfaz permite
    - [x] a.  Comunicación entre aplicaciones del mismo tipo
    - [x] b.  Comunicación entre aplicaciones de distinto tipo
    - [x] c.  Comunicación entre dispositivos iguales
    - [x] d.  Comunicación entre dispositivos diferentes

    **Justificación:** Justamente se ponen estos contratos para abstraerse tanto del tipo de aplicación como del tipo de dispositivo.

30. Entre las ventajas de tener un coordinador en un S.D están:
    - [x] a.  Aumentar el control de la comunicación entre nodos
    - [x] b.  Aumentar la seguridad del sistema
    - [x] c.  Aumentar la coherencia de datos
    - [ ] d.  Evitar SPoFs (Single Points of Failure)

    **Justificación:** Claramente provocás un SPoF. La comunicación está más controlada porque todo pasa por el coordinador, lo cual te da una arquitectura más robusta y más sencilla de implementar. Lo mismo aplica para la seguridad y la coherencia de datos (todo pasa por el coordinador)

31. En cuanto a un middleware, se puede afirmar:
    - [ ] a.  Que es un intermediario entre HW y SW.
    - [x] b.  Que es un sistema compuesto por varias aplicaciones
    - [x] c.  Que es un sistema que ofrece al usuario la capacidad de uso de diferentes sistemas operativos
    - [ ] d.  Todas las anteriores

    **Justificación:** Lo de los sistema operativos es cierto en el caso del Hypervisor de las máquinas virtuales, el cual es un middleware entre el Host OS y las distintas VM. No necesariamente tiene que estar compuesto por varias apps, pero se puede implementar de esta manera.

32. Un wrapper siempre usa:
    - [ ] a.  Un nodo broker que intermedia entre aplicaciones que no están diseñadas para la comunicación entre nodos o dispositivos
    - [x] b.  Un hardware o software intermediario entre aplicaciones que carecen de APIs para proveer interacción con otros nodos
    - [x] c.  Una capa de software adicional que le permite a una aplicación interactuar con otra
    - [ ] d.  Una capa de hardware adicional que le permite a un nodo interactuar con otro

    **Justificación:** Es un tipo de middleware que encapsula otro cacho de software/hardware y le agrega comportamiento, lo cual puede derivar en las opciones seleccionadas.

33. Un modelo cliente/servidor puede ser considerado como:
    - [ ] a.  Una arquitectura descentralizada
    - [x] b.  Una arquitectura centralizada
    - [x] c.  Un modelo diseñado para la comunicación entre varios nodos clientes y varias réplicas de un servidor.
    - [x] d.  Un modelo diseñado para proveer servicios a varios nodos clientes

    >**Nota:** Esta es la única que me genera duda, porque en clase dijeron que no es una arquitectura descentralizada, ya que por definición el modelo cliente/servidor es centralizado, pero al Tiny le marcaron que es descentralizado

34. En cuanto a una arquitectura NFS:
    - [ ] a.  Se la puede considerar P2P
    - [x] b.  Se puede considerar un modelo cliente/servidor de uso particular
    - [x] c.  Se le puede considerar un modelo en capas
    - [ ] d.  Todas las anteriores

    **Justificación:** Es un sistema de archivos en la red, no es P2P.

35. Un sistema P2P desestructurado se usa para:
    - [x] a.  Conformar un anillo de comunicación entre nodos para tomar una decisión entre los mismos
    - [x] b.  Seleccionar un nodo líder o coordinador
    - [ ] c.  Sincronizar el tiempo entre todos los nodos
    - [ ] d.  Todas las anteriores

    **Justificación:** 

36. Un sistema de Cloud Computing ofrece servicios:
    - [x] a.  Orientados a Infraestructura
    - [ ] b.  Orientados a Middleware
    - [x] c.  Orientados a Software
    - [x] d.  Orientados a Plataforma

    **Justificación:** Lo vimos en AWS pero no me acuerdo

37. Los sistemas edge:
    - [ ] a.  Son estructurados en forma de hipercubos o mallas
    - [ ] b.  El nivel de latencia es alto, el nivel de confiabilidad y seguridad es bajo
    - [ ] c.  Son estructurados en forma de anillo
    - [x] d.  Ninguna de las anteriores

    **Justificación:** La respuesta "b" no está comparando con nada, por lo que no se puede afirmar esto

38. Para un sistema basado en blockchain
    - [ ] a.  Se usan cadenas de bloques independientes y totalmente diferentes en varios nodos
    - [x] b.  Procura mantener una sola versión válida de la cadena de bloques distribuida (replicada)
    - [ ] c.  Un nodo coordinador decide sobre la validez de los bloques en la cadena
    - [x] d.  Se hacen réplicas de la cadena de bloques en diferentes nodos

    **Justificación:** 

39. Se puede afirmar que un proceso y un thread
    - [x] a.  Pueden ejecutar un mismo programa
    - [ ] b.  Son conceptos totalmente separados
    - [x] c.  Los threads representan varias ejecuciones de un mismo proceso
    - [x] d.  Un proceso puede compartir sus recursos entre los threads del mismo proceso

    **Justificación:** 

40. Un S.D tiene entre sus objetivos principales
    - [ ] a.  Disminuir la latencia en la ejecución de un thread
    - [ ] b.  Aumentar el rendimiento de aplicaciones no paralelizables
    - [x] c.  Mejorar la performance de la ejecución de tareas
    - [x] d.  Aumentar la capacidad de cómputo y almacenamiento

    **Justificación:** No tiene sentido hacer un sistema distribuido para aplicaciones no paralelizables. Tampoco tiene sentido disminuir la latencia de un thread puesto que la latencia es propia de la red.
