# Guía Tolerancia

## Métricas de Disponibilidad y Confiabilidad

### Ejercicio 1
Explique la diferencia fundamental entre los conceptos de **Availability** y **Reliability**.  
A continuación, ilustre estas diferencias proporcionando un ejemplo claro de un sistema o situación de la vida real para cada una de las siguientes combinaciones y justifique:

a) **High Reliability and High Availability**
b) **High Reliability and Low Availability**
> Para el B:(Un ejemplo análogo podría ser un auto de Fórmula 1: Durante la carrera debe ser súper confiable y rendir bien. Pero al término de la carrera puede que tenga que estar en el taller durante un tiempo, lo que produce una baja disponibilidad.)  

c) **Low Reliability and High Availability**
d) **Low Reliability and Low Availability**

### Respuesta
a) **High Reliability & High Availability**: los sistemas informáticos de los hospitales, por ejemplo. Es necesario que estén todo el tiempo disponibles y que los fallos sean mínimos (o que estén bien mitigados), son sensibles.
b) **High Reliability and Low Availability**: sistema bancario. Pueden clavarte un mantenimiento entre las 00:00 y las 03:00 y no pasa natalia.
c) **Low Reliability and High Availability**: como protocolo, UDP en sí mismo respeta estas características; como sistema, un juego en beta/alfa que revienta todo el tiempo, pero está disponible todo el tiempo.
- También el viejo sistema de compra de dólares de la AFIP era poco confiable: lo bajaban cuando querían

> - Disponibilidad: Cuánto tiempo digo que voy a estar disponible
> - Fiabilidad (reliability): Qué porcentaje del tiempo que digo que voy a estar disponible realmente estoy disponible

d) **Low Reliability and Low Availability**: el TP1, corre en nuestra máquina, anda a saber que pasa si hay un fallo, etc.


### Ejercicio 2
Durante el último Cyber Monday, el sistema de venta de merchandising de la Universidad Austral tuvo las siguientes caídas. Calcular **MTTF**, **MTTR** y **MTBF**:

| Hora caída | Hora recuperación | Tiempo indisponible |
| ---------- | ----------------- | ------------------- |
| 08:00 am   | 08:30 am          | 30 min              |
| 10:30 am   | 11:30 am          | 1 hora              |
| 16:15 pm   | 16:30 pm          | 15 min              |

### Ejercicio 3
Tengo un sistema que recibe un tráfico de **100.000 RPM (requests per minute)**.  
¿Cuántos requests podrían quedar sin respuesta o recibir un status code 5xx para asegurar un uptime del **99,99%** durante el lapso de 1 minuto?

## Redundancia

### Ejercicio 4
Manejo de fallos mediante **Redundancia**.  
Busque un ejemplo para cada uno de los 3 tipos de redundancia (**Información, tiempo y física**) que se utilicen en sistemas reales y especifique dicho sistema.

## Teorema de CAP

### Ejercicio 5
Indique qué tipo de sistema son los siguientes (**CP** o **AP**) y justifique:

a) **Youtube**
b) **Home banking**
c) **Feed de Instagram**
d) **Red Bitcoin**

### Respuesta
a) **Youtube**: es del tipo **AP**, se prioriza la disponibilidad, lo que querés es poder servir los videos; si falla un frame o si se pierde en el camino medio que no te importa.
- Priorizas que el usuario pueda consumir el servicio
b) **Home banking**: es del tipo **CP**, se prioriza tener un estado consistente; que si hago una transferencia esté en el mismo estado en todas las bases de datos

c) **Feed de Instagram**: es del tipo **AP**, lo que te importa es poder servir todos esos reels de brainrot <img src="https://miro.medium.com/1*RoxB4u0vzLpMEhMaOeTZIw.jpeg" height="40" width="40">, no te importa mucho que el feed sea en todos lados el mismo. 
- Querés verlo de manera inmediata, no te importa si está actualizado o si estás viendo el último estado real.

d) **Red Bitcoin**: es del tipo **CP**, se prioriza que toda la red esté en un estado consistente, que siempre muestres el último estado _**real**_ de la red.
- Sabiendo que es un sistema que se basa en `Proof of Work`, terminás esperando a que al menos el 51% de los bloques estén disponibles para ejecutar una transacción.

## Resiliencia de Procesos

### Ejercicio 6
En la **resiliencia de procesos** existen dos tipos de grupo.  
Explique cuáles y qué ventajas y desventajas tiene cada uno.

## Algoritmos de Consenso

### Ejercicio 7
¿Por qué existen diferentes tipos de **algoritmos de consenso**?  
¿Cuál es la problemática mayor?  
¿Podemos conseguir consenso en un sistema asíncrono?

## Comunicación Cliente-Servidor

### Ejercicio 8
**Comunicación Cliente-Servidor Confiable**  
Indique en cuál de las siguientes opciones (consulta a otro microservicio) podría configurar un *retry* sin más preocupaciones y justifique:

a) Actualizar información del usuario como edad.  
b) Obtener la geolocalización a partir de una IP.  
c) Realizar pago de un pasaje de avión.  
d) Eliminar usuario de la base de datos.

### Respuesta
a) No hay problema, siempre estás escribiendo lo mismo.

El problema estaría en caso de que otro proceso quiera leer.

b) Es una operación de lectura, todo pelota

c) No se podría hacer un retry, es algo sensible, involucra plata. Te puede pasar que se concretó el pago pero en una operación posterior falló algo, podrías terminar pagando 2 veces

d) Sí, porque estoy targeteando un usuario en particular. Si el usuario ya se eliminó y reintento, como mucho la query va a fallar porque el usuario no existe más.


## Multicast confiable

### Ejercicio 9
Defina qué tipo de multicast necesitan cada uno de los siguientes sistemas y justifique:

a) Sistema de sensores que reportan lecturas (ej. temperatura, humedad) de cada una de los espacios de una oficina para poder armar un dashboard sobre la temperatura. Por ejemplo, la temperatura media de la oficina.

b) Un sistema bancario con varias réplicas de la base de datos que gestionan saldos de cuentas. Se envían operaciones como "TRANSFERIR \$100 de A a B" y "DEPOSITAR \$50 en A".

c) En una sala de chat de grupo, se pueden dar respuestas explícitas a mensajes (el mensaje $m_2$ de Carlos fue una respuesta explícita al mensaje $m_1$ de Horacio). Sin embargo, si dos mensajes no están relacionados, podrían aparecer en un orden diferente en distintas máquinas.

d) Un sistema de edición de documentos colaborativo en tiempo real (como Google Docs). Donde las modificaciones de un usuario pueden basarse en la que realiza otro usuario. Además, si hay dos ediciones concurrentes, se necesita que todas las réplicas del documento converjan al mismo estado final.

e) Un sistema de procesamiento de video con varios workers que van recibiendo tareas. Donde es importante que no se realice una tarea más de una vez. Por ejemplo: Un usuario A envía 1 “cargar video1.mp4” y luego “Transcode video1.mp4”. Al mismo tiempo, usuario 2 envía “Analizar audio video2.mp4”.

f) Un sistema de logging distribuido donde múltiples procesos envían entradas a un grupo de servidores de análisis. Para el usuario final, es fundamental ver los logs en el orden en que se va ejecutando el código en cada proceso.

### Respuesta
a) Se puede usar el **desordenado** (o _multicast confiable_), por 2 razones:
- Son datos de temperatura, no son críticos
- Si sólo vas a calcular el promedio, el orden en el que te llegan no te importan

b) Acá el orden de las operaciones importa necesariamente; no es lo mismo primero depositar \$50 y luego transferir \$100 que hacerlo en orden distinto, puedo llegar a no tener saldo en el 2do caso. Por ende, es necesario un tipo de multicast **atómico totalmente ordenado**.
- Necesito que me llegue todo, todo el tiempo en el mismo orden
- Todas las réplicas de la base de datos deben mantener el mismo estado, la versión final de la BD debe tener la misma versión de los datos en cada réplica.

c) La propia pregunta de lo dice: necesitás **multicast causalmente ordenado**, no te importa el orden de los mensajes que no están explícitamente relacionados

d) Necesariamente debemos tener ordenamiento **atómico**, pero acá tanto **FIFO** como **Causal** pueden ir:
- Causal puede servir por el hecho de que, por ejemplo, el sistema puede interpretar que una persona escribió un pedazo de texto y luego otro lo modificó
- FIFO medio que se explica solo, modificas en el orden en el que van llegando los mensajes. Los cambios se van encolando.
  - Este termina teniendo más sentido, porque la relación no es tan clara como en el caso anterior de los mensajes.

e) Se requiere un multicast ordenado, primordialmente **FIFO Atomic**.
- Causal no es tan necesario porque no necesariamente la carga del video te va a generar el `transcode`

f) Es imperativo que estén ordenados para mantener trazabilidad, y lo ideal sería usar un ordenamiento **FIFO atómico**
- No se requiere tanto el causal puesto que un log no necesariamente dispara otro

> Atomic es necesariamente Ordenado
> El causal puede estar desordenado, mientras quede clara la relación causal