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

d) **Low Reliability and Low Availability**: el TP1, corre en nuestra máquina, andá a saber qué pasa si hay un fallo, etc.


### Ejercicio 2
Durante el último Cyber Monday, el sistema de venta de merchandising de la Universidad Austral tuvo las siguientes caídas. Calcular **MTTF**, **MTTR** y **MTBF**:

| Hora caída | Hora recuperación | Tiempo indisponible |
| ---------- | ----------------- | ------------------- |
| 08:00 am   | 08:30 am          | 30 min              |
| 10:30 am   | 11:30 am          | 1 hora              |
| 16:15 pm   | 16:30 pm          | 15 min              |


### Respuesta

**Datos del problema:**
- 3 fallos durante el Cyber Monday
- Tiempos de indisponibilidad: 30 min, 60 min, 15 min

**Cálculos:**

**1. MTTR (Mean Time To Repair) - Tiempo promedio de reparación:**
$$
MTTR = (30 + 60 + 15) / 3 = 105 / 3 = 35 \text{ minutos}
$$

**2. MTTF (Mean Time To Failure) - Tiempo promedio entre fallos:**

Para calcular MTTF, necesitamos el tiempo total de operación y el número de fallos.

Asumiendo que el sistema operó desde las 00:00 hasta las 24:00 (24 horas = 1440 minutos):
- Tiempo total de indisponibilidad = 30 + 60 + 15 = 105 minutos
- Tiempo total de operación = 1440 - 105 = 1335 minutos
- Número de fallos = 3

$$
MTTF = \frac{\text{Tiempo total de operación}}{\text{Número de fallos}} \\
$$
$$
MTTF = \frac{1335}{3} = 445 \text{ minutos} = 7 \text{ horas y } 25 \text{ minutos}
$$
**3. MTBF (Mean Time Between Failures) - Tiempo promedio entre fallos:**

$MTBF = MTTF + MTTR = 445 + 35 = 480 \text{ minutos} = 8 \text{ horas}$


**Resumen:**
- **MTTR**: 35 minutos
- **MTTF**: 445 minutos (7h 25min)
- **MTBF**: 480 minutos (8h)

**Disponibilidad del sistema durante el Cyber Monday:**

$\text{Disponibilidad} = MTTF / (MTTF + MTTR) = 445 / 480 = 0.927 = 92.7\%$

### Ejercicio 3
Tengo un sistema que recibe un tráfico de **100.000 RPM (requests per minute)**.  
¿Cuántos requests podrían quedar sin respuesta o recibir un status code 5xx para asegurar un uptime del **99,99%** durante el lapso de 1 minuto?

### Respuesta
Esto es hacer una regla de 3 simple:

Si el $100\%$ de las requests que me llegan por minuto son $100{,}000$, si quiero un uptime del $99.99\%$ necesito:

$$
\text{Requests totales} = Req_{total} = 100{,}000
$$

$$
\text{Porcentaje de uptime requerido} = 99.99\%
$$

$$
Req_{uptime} = Req_{total} \times 0.9999 = 100{,}000 \times 0.9999 = 99{,}990
$$

$$
Req_{droppeables} = Req_{total} - Req_{uptime} = 100{,}000 - 99{,}990 = 10
$$

Entonces, la respuesta es que puedo dejar 10 solicitudes sin respuesta por minuto.

## Redundancia

### Ejercicio 4
Manejo de fallos mediante **Redundancia**.  
Busque un ejemplo para cada uno de los 3 tipos de redundancia (**Información, tiempo y física**) que se utilicen en sistemas reales y especifique dicho sistema.

### Respuesta

Según el material de la materia, existen **3 tipos de redundancia** para el manejo de fallos:

1. **Redundancia de información**: Se añade información redundante (p. ej. códigos de detección o corrección de errores, como en TCP)
2. **Redundancia de tiempo**: Se realiza una acción varias veces (p. ej. retransmisión de mensajes)
3. **Redundancia física**: Se usan componentes duplicados (p. ej. replicación de procesos o datos)

#### Ejemplos reales (en tabla):

| Tipo de Redundancia            | Sistema / Ejemplo                                             | Mecanismo                                   | Funcionamiento/Descripción                                                                                                                              | Aplicación                                         |
|---------------------------------|--------------------------------------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| **Redundancia de Información**  | Protocolo TCP (Transmission Control Protocol)                | Checksums y códigos de corrección de errores| TCP incluye un checksum de 16 bits en cada segmento; si no coincide, se detecta error y se pide retransmisión                                         | Comunicaciones de internet (HTTP, HTTPS, FTP, etc.)|
| **Redundancia de Información**  | Sistemas de almacenamiento RAID (RAID 5/6)                   | Paridad distribuida y códigos de corrección | RAID 5/6 almacena información de paridad y permite reconstruir datos perdidos si un disco falla                                                        | Servidores empresariales y centros de datos        |
| **Redundancia de Tiempo**       | Protocolo TCP - Retransmisión de paquetes                    | Timeout y retransmisión automática          | Si no se recibe ACK en un tiempo, se retransmite el paquete automáticamente                                                                           | Todas las comunicaciones TCP                       |
| **Redundancia de Tiempo**       | Bases de datos - Transacciones con reintentos                | Retry logic, circuit breakers               | Si una transacción falla por timeout/error temporal, se reintenta automáticamente (ej: DynamoDB reintenta hasta 3 veces)                              | Bases de datos distribuidas (DynamoDB, Cassandra…) |
| **Redundancia Física**          | Google Search - Clusters de servidores                       | Múltiples servidores detrás de load balancer| Si un servidor falla, el balancer redirige el tráfico automáticamente a servidores sanos                                                              | Google, YouTube, Gmail                            |
| **Redundancia Física**          | Amazon Web Services (AWS) - Multi-AZ deployments             | Réplicas de bases de datos en varias zonas  | Datos replicados entre zonas de disponibilidad; si una falla, se usa la réplica (ej: Amazon RDS promueve la réplica ante un fallo de zona)             | Aplicaciones empresariales en AWS (Netflix, Airbnb)|
| **Redundancia Física**          | Sistemas bancarios - Replicación de datos críticos           | Múltiples copias en centros de datos        | Cada transacción se escribe en múltiples réplicas antes de confirmarse (Visa/Mastercard mantiene réplicas en varios data centers)                     | Procesamiento de pagos con tarjetas de crédito     |


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

### Respuesta

Según lo visto en clase, hay **2 formas básicas de organizar grupos de procesos** para lograr resiliencia:

1. **Grupos sin coordinador (todos los procesos iguales):**
   - **Descripción:** Todos los procesos del grupo tienen el mismo rol (en lo que a jerarquía refiere) y toman decisiones de manera colectiva, por ejemplo, a través de votos o protocolos de consenso.
   - **Ventajas:** 
     - No hay un único punto de falla, ya que todos los procesos pueden continuar incluso si algunos fallan.
     - Potencialmente mayor disponibilidad y tolerancia a fallos.
   - **Desventajas:** 
     - La coordinación suele ser más compleja, ya que todos deben ponerse de acuerdo.
     - Puede requerir una mayor cantidad de mensajes y algoritmos más complejos para garantizar la coherencia.
     - Mayor dificultad para escalar si el grupo es muy grande.

2. **Grupos con coordinador (líder/trabajadores):**
   - **Descripción:** Uno de los procesos actúa como coordinador o líder, y los demás como trabajadores (ejemplo: modelo primary-backup, o sistemas como DNS).
   - **Ventajas:**
     - La toma de decisiones es simple y más rápida, ya que el coordinador centraliza la coordinación.
     - Menor complejidad de sincronización: el líder determina la acción y los demás replican.
   - **Desventajas:**
     - Existe un único punto de falla: si el coordinador cae, hay que elegir uno nuevo (pudiendo haber brechas temporales en la disponibilidad).
     - El coordinador puede ser cuello de botella si la carga crece mucho.

**Resumen:**  
- Grupos “todos iguales” tienen mejor tolerancia a fallos y disponibilidad, pero son más difíciles de coordinar.
- Grupos con coordinador son más fáciles de manejar y más ágiles, pero arrastran el riesgo del SPoF.

Esto se usa según el tipo de aplicación, el número de procesos y el nivel de tolerancia a fallos requerido por el sistema distribuido.

## Algoritmos de Consenso

### Ejercicio 7
¿Por qué existen diferentes tipos de **algoritmos de consenso**?  
¿Cuál es la problemática mayor?  
¿Podemos conseguir consenso en un sistema asíncrono?

### Respuesta

Existen diferentes tipos de algoritmos de consenso porque los sistemas distribuidos pueden enfrentarse a distintos modelos de fallo (fallos por caída, fallos arbitrarios/Byzantinos, fallos detectables, etc.), y cada uno de estos escenarios tiene requisitos y desafíos particulares. Además, varía el grado de tolerancia a fallos que se necesita, la cantidad de procesos, las garantías de rendimiento y el entorno de sincronía (sincrónico, parcialmente sincrónico o asíncrono).

La problemática mayor es cómo lograr que un conjunto de procesos, posiblemente afectados por fallos o mensajes retrasados/perdidos, se ponga de acuerdo en una única decisión (por ejemplo, una operación, un valor de estado o el siguiente bloque de una cadena), garantizando que todos los procesos correctos lleguen al mismo resultado incluso ante fallas. Esto se complica si hay fallos de comunicación, fallas arbitrarias (donde un proceso puede comportarse de manera maliciosa o impredecible), o si los procesos pueden funcionar a distintas velocidades.

Respecto a si podemos conseguir consenso en un sistema asíncrono: **no es posible garantizar consenso en un sistema asíncrono puro si existe aunque sea un solo fallo de proceso**. Esto es una limitación fundamental demostrada teóricamente (resultado de Fischer, Lynch y Paterson, "el teorema FLP"), porque en un entorno totalmente asíncrono no es posible diferenciar entre un proceso lento y uno caído. Por eso, los algoritmos prácticos suelen asumir algún nivel de sincronía (aunque sea eventual), o utilizan detección de fallos basada en timeouts y otras técnicas.

En resumen:
- Hay diferentes algoritmos de consenso porque los escenarios de fallo y requisitos varían mucho.
- El mayor desafío es coordinar decisiones correctas en presencia de fallos y comunicación incierta.
- En sistemas asíncronos puros no se puede lograr consenso tolerante a fallos; siempre se requieren algunas suposiciones de sincronía o mecanismos extra para avanzar.


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