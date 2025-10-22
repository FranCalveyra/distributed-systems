# Guía Tolerancia

## Métricas de Disponibilidad y Confiabilidad

### Ejercicio 1
Explique la diferencia fundamental entre los conceptos de **Availability** y **Reliability**.  
A continuación, ilustre estas diferencias proporcionando un ejemplo claro de un sistema o situación de la vida real para cada una de las siguientes combinaciones y justifique:

a) **High Reliability and High Availability**  
b) **High Reliability and Low Availability**  
> (Un ejemplo análogo podría ser un auto de Fórmula 1: Durante la carrera debe ser súper confiable y rendir bien. Pero al término de la carrera puede que tenga que estar en el taller durante un tiempo, lo que produce una baja disponibilidad.)  
c) **Low Reliability and High Availability**  
d) **Low Reliability and Low Availability**

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

a) Youtube  
b) Home banking  
c) Feed de Instagram  
d) Red Bitcoin  

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

## Multicast confiable

### Ejercicio 9
Defina qué tipo de multicast necesitan cada uno de los siguientes sistemas y justifique:

a) Sistema de sensores que reportan lecturas (ej. temperatura, humedad) de cada una de los espacios de una oficina para poder armar un dashboard sobre la temperatura. Por ejemplo, la temperatura media de la oficina.

b) Un sistema bancario con varias réplicas de la base de datos que gestionan saldos de cuentas. Se envían operaciones como "TRANSFERIR \$100 de A a B" y "DEPOSITAR \$50 en A".

c) En una sala de chat de grupo, se pueden dar respuestas explícitas a mensajes (el mensaje m_2 de Carlos fue una respuesta explícita al mensaje m_1 de Horacio). Sin embargo, si dos mensajes no están relacionados, podrían aparecer en un orden diferente en distintas máquinas.

d) Un sistema de edición de documentos colaborativo en tiempo real (como Google Docs). Donde las modificaciones de un usuario pueden basarse en la que realiza otro usuario. Además, si hay dos ediciones concurrentes, se necesita que todas las réplicas del documento converjan al mismo estado final.

e) Un sistema de procesamiento de video con varios workers que van recibiendo tareas. Donde es importante que no se realice una tarea más de una vez. Por ejemplo: Un usuario A envía 1 “cargar video1.mp4” y luego “Transcode video1.mp4”. Al mismo tiempo, usuario 2 envía “Analizar audio video2.mp4”.

f) Un sistema de logging distribuido donde múltiples procesos envían entradas a un grupo de servidores de análisis. Para el usuario final, es fundamental ver los logs en el orden en que se va ejecutando el código en cada proceso.
