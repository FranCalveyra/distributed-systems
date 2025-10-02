# Guía Naming
### Ejercicio 1
Escribir un ejemplo en donde la dirección de una entidad E necesita resolverse dentro de
otra dirección para acceder en realidad a E.

### Ejercicio 2
En general, ¿cuál es la diferencia en la manera en que se implementan los nombres en
sistemas distribuidos y no distribuidos?

### Ejercicio 3
Si no se cuenta con un sistema de nombres, ¿qué ocurre si una entidad ofrece más de un punto de acceso?

### Ejercicio 4
¿En qué se diferencian el sistema de direccionamiento plano (Flat Naming System) y el sistema de direccionamiento estructurado (Structured Naming System)?

### Ejercicio 5
En la solución de difusión por broadcast para Flat Naming System:

a. ¿En qué capa del Modelo de referencia OSI operaría?
b. ¿Qué limitaciones tiene?
c. ¿Cuál es el protocolo más comúnmente utilizado para la difusión por Broadcast en Flat Naming System?

### Ejercicio 6
De acuerdo al protocolo, ¿Como se sabe que dirección MAC está asociada con una dirección IP?

### Ejercicio 7
De acuerdo al sistema de nombres estructurado, ¿Cómo se denomina el mecanismo para saber cómo y dónde comenzar la resolución de nombres?

### Ejercicio 8
Realizar, en grupo, el laboratorio guiado de ARP con Packet Tracer hasta la parte 2, paso 1.

Packet Tracer: Revisión de la tabla ARP

Tabla de asignación de direcciones
| Dispositivo | Interfaz    | Dirección MAC  | Interfaz del switch |
| ----------- | ----------- | -------------- | ------------------- |
| Router0     | Gg0/0       | 0001.6458.2501 | G0/1                |
| Router0     | S0/0/0      | N/A            | N/A                 |
| Router1     | G0/0        | 00E0.F7B1.8901 | G0/1                |
| Router1     | S0/0/0      | N/A            | N/A                 |
| 10.10.10.2  | Inalámbrica | 0060.2F84.4AB6 | F0/2                |
| 10.10.10.3  | Inalámbrica | 0060.4706.572B | F0/2                |
| 172.16.31.2 | F0          | 000C.85CC.1DA7 | F0/1                |
| 172.16.31.3 | F0          | 0060.7036.2849 | F0/2                |
| 172.16.31.4 | G0          | 0002.1640.8D75 | F0/3                |

#### Objetivos
Parte 1: Examine una solicitud de ARP

Partee 2: Examine una tabla de direcciones MAC del switch

Parte 3: Examine el proceso ARP en Comunicaciones remotas

Aspectos básicos
Esta actividad está optimizada para la visualización de PDU. Los dispositivos ya están configurados. Recopilará información de la PDU en modo de simulación y contestará una serie de preguntas sobre los datos que recopila.

Instrucciones
Parte 1: Examine una solicitud de ARP
Paso 1: Genere solicitudes de ARP haciendo ping a 172.16.31.3 desde 172.16.31.2.
Abra un símbolo del sistema.

a.     Haga clic en 172.16.31.2 y abra el símbolo del sistema.

b.     Introduzca el comando arp -d para borrar la tabla ARP.

Cierre símbolo del sistema

c.     Ingrese al modo Simulation e introduzca el comando ping 172.16.31.3. Se generan dos PDU. El comando ping no puede completar el paquete ICMP sin conocer la dirección MAC del destino. Entonces, la computadora envía una trama de difusión ARP para encontrar la dirección MAC del destino.

d.     Haga clic en Capture/Forward una vez. La PDU ARP mueve el Switch1 mientras la PDU ICMP desaparece, esperando la respuesta de ARP. Abra la PDU y registre la dirección MAC de destino.

Pregunta:
¿Esta dirección aparece en la tabla de arriba? $\rightarrow$ No, es `0000.0000.0000`.

Pregunta:
¿Cuántas copias de la PDU hizo Switch 1? $\rightarrow$ 3 copias, una para cada dirección dentro de la tabla.

¿Cuál es la dirección IP del dispositivo que aceptó la PDU? $\rightarrow$ 172.16.31.3

e.     Abra la PDU y examine la capa 2.

Pregunta:
¿Qué pasó con las direcciones MAC de origen y destino? $\rightarrow$ La de origen es la de la terminal 172.16.31.2, y la de destino es la de broadcast.

f.      Haga clic en Capture/Forward hasta que la PDU regrese a 172.16.31.2.

Pregunta:
¿Cuántas copias de la PDU realizó el switch durante la respuesta ARP? $\rightarrow$ Hizo 5 copias.

Paso 2: Examine la tabla ARP.
a.     Tome en cuenta que el paquete ICMP vuelve a aparecer. Abra la PDU y examine las direcciones MAC.

Pregunta:
¿Las direcciones MAC del origen y el destino se alinean con sus direcciones IP? $\rightarrow$ Sí.

b.     Regrese a Realtime y se completa el ping.

c.     Haga clic en 172.16.31.2 e ingrese el comando arp –a.

Pregunta:
¿A qué dirección IP corresponde la entrada de la dirección MAC? $\rightarrow$ 172.16.13.3, la que buscábamos.

En general, ¿cuándo emite una terminal una solicitud de ARP? $\rightarrow$ Cuando no tiene la dirección de destino en su tabla de ARP.

Parte 2: Examine en un switch la tabla de direcciones MAC
Paso 1: Genere tráfico adicional para llenar la tabla de direcciones MAC del switch.
Abra un símbolo del sistema.

a.     Desde 172.16.31.2, introduzca el comando 172.16.31.4.

b.     Haga clic en 10.10.10.2 y abra el símbolo del sistema..

c. Ingrese el comando ping 10.10.10.3.

Pregunta:
¿Cuántas respuestas fueron enviadas y recibidas? $\rightarrow$ Tanto en el primer caso como en el segundo, 4 y 4.

Cierre símbolo del sistema

Paso 2: Examine la tabla de direcciones MAC en los switches.
a.     Haga clic en Switch1y luego en la pestaña de CLI. Introduzca el comando show mac-address-table .

Pregunta:
¿Las entradas corresponden a las de la tabla de arriba? $\rightarrow$ Sí, a cada terminal conectada a ese switch.

b.     Hag clic en elSwitch0, y luego en la pestaña de CLI. Introduzca el comando show mac-address-table.

Preguntas:
¿Las entradas corresponden a las de la tabla de arriba? $\rightarrow$ Sí, a las 2 terminales inalámbricas y al Router.

¿Por qué hay dos direcciones MAC asociadas a un puerto? $\rightarrow$ Porque es el puerto del Access Point.

Parte 3: Examine el proceso ARP en Comunicaciones Remotas
Paso 1: Generar tráfico para producir tráfico ARP.
Abra un símbolo del sistema.

a. Haga clic en 172.16.31.2 y abra el símbolo del sistema.

b. Ingrese el comando ping 10.10.10.1.

c.     Type arp –a.

Pregunta:
¿Cuál es la dirección IP de la nueva entrada de la tabla ARP? $\rightarrow$ 172.16.13.1

d.     Ingrese arp -d para borrar la tabla ARP y cambie al modo de Simulation.

e.     Repita el ping a 10.10.10.1.

Pregunta:
¿Cuántas PDU aparecen? $\rightarrow$ 7

Cierre símbolo del sistema

f.      Haga clic en Capture/Forward. Haga clic en la PDU que ahora se encuentra en el Switch1.

Pregunta:
¿Cuál es la dirección IP de destino de destino de la solicitud ARP? $\rightarrow$ 172.16.13.1

g.     La dirección IP de destino no es 10.10.10.1.

Pregunta:
¿Por qué? $\rightarrow$ Porque 10.10.10.1 está en otra red. ARP solo se usa en la red local, así que el host resuelve la MAC del gateway por defecto (172.16.13.1) y le envía allí el paquete hacia 10.10.10.1.

Paso 2: Examine la tabla ARP en el Router1.
a.     Cambie al modo Realtime. Haga clic enRouter1 y luego en la pestaña de CLI .

b.     Ingrese al modo EXEC privilegiado y luego al comando show mac-address-table.

Pregunta:
¿Cuántas direcciones MAC hay en la tabla? ¿Por qué? $\rightarrow$ Ninguna, porque el Router solo guarda direcciones IP, no MAC.

c.     Introduzca el comando show arp.

Preguntas:
¿Existe una entrada para 172.16.31.2? $\rightarrow$ Sí

¿Qué sucede con el primer ping en una situación en la que el router responde a la solicitud de ARP? $\rightarrow$ No tengo ni idea


