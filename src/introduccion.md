# Introducción
## Objetivos funcionales
¿Vale la pena construir un sistema distribuido?
¿Para qué hago un sistema distribuido? -> Porque tengo que compartir información

### Objetivos que merecen crear un sistema distribuido
- **Los principales**:
  - Ofrecer recursos/procesos a otros
  - Transparencia en la distribución de procesos y recursos
  - Interoperabilidad
  - Confiabilidad

- **Otros aspectos influyentes**
  - Seguridad
  - Escalabilidad

### Por compartir recursos
**Brindar acceso a recursos para que esté disponible para muchos usuarios.**

En este contexto, casi que cualquier cosa que quiera compartir es un recurso:
- Archivos
- mensajes
- Impresoras
- Servicios
- etc.

Cuando necesito compartir recursos, se merece un sistema distribuido.
Recurso es un concepto amplio que puede ser cosas o procesos de negocio.

### Transparencia en el acceso
**Necesitamos esconder la ubicación de los recursos de la gente que accede**
Pero hay varios aspectos para "esconder" o hacer transparente:
- El acceso (representaciones de datos, sistemas operativos)
- La ubicación (donde está ubicado: data center, uno o varios)
- Reubicación (si muevo el recurso mientras lo estoy accediendo)
  - Si yo me muevo mientras que quiero acceder un recurso, debería de poder accederlo.
- Migración (si el recurso se mueve)
  - Si el recurso se mueve y yo no.
- Replicación (si hay una o varias copias del mismo recurso)
- Concurrencia (si hay muchos usuarios accediendo al mismo recurso)
- Fallas (el recurso puede fallar y recuperarse sin afectar el uso)

Con **esconder**, nos referimos a que deberíamos de poder acceder al recurso a pesar de cualquiera de estas condiciones previamente mencionadas.

> **Content Encoding**: cuando se le pide un HTML muy pesado a un server en el browser, no se manda en Plain Text, sino que se zippea (comprime) y se manda.

### Apertura e interoperabilidad
Un sistema abierto es cuando los componentes pueden ser usados por otros sistemas, y/o cuando el sistema tiene componentes originados por otro lado.

Normalmente nos referimos a:
- Sistemas que adhieren a reglas (protocolos) estándar.

La idea es que **"todos nos apeguemos al mismo contrato"**, y que hagas fácil para el resto poder interactuar con dicho sistema.

### Confiabilidad
La confiabilidad de un sistema distribuido más compleja que uno centralizado:

**¡Hay muchas más partes que pueden fallar!**

Encima hay varios aspectos dentro de la confiabilidad:
- Disponibilidad
  - Cuánto tiempo digo que voy a estar disponible
- Fiabilidad (reliability)
  - Qué porcentaje del tiempo que digo que voy a estar disponible realmente estoy disponible
- Seguridad ante fallas (safety)
  - Qué tan resiliente es el sistema, qué tanto soporta las fallas
- Mantenibilidad

### Seguridad
Queremos proteger el sistema de usos indebidos (en un concepto amplio)

Los conceptos comunes de seguridad:
- Identificación (quién sos)
- Autenticación (sos quien decís ser)
- Autorización (hacés sólo lo que tenés permitido hacer)

Otros aspectos relacionados:
- **Privacidad** de la comunicación (que no escuchen nuestras conversaciones) <img src="https://media.tenor.com/j75dJveWv9sAAAAM/angry-bird-hearing.gif" height="20" width="20">
- **Intercepción** de la comunicación (que no se hagan pasar por otro)

### Escalabilidad
Hay varias dimensiones relacionadas con la escalabilidad:
- **En tamaño** (cuántos usuarios o recursos acceden al sistema)
  - Aumenta mucho el tráfico
  - Puedo tener una Raspberry Pi con 124.000.000 intentos de conexión. No va a andar bien ni en pedo, tampoco escala.
- **En geografía** (si se accede al sistema desde distintas ubcaciones físicas)
- **En administración** (se puede adminsitrar, aunque crezca)

#### Estrategias de escalamiento
- **Mejorar la latencia**: hacer eficiente la comunicación
  - Es el tiempo "muerto" donde no se está procesando nada.
  - Si bajo la latencia, puedo dedicarle más tiempo al procesamiento, justamente. Puedo acelerar la comunicación.
- **Particionar y distribuir**: llegar más rápido al dato.
  - Tengo un F.S en la facultad. Si está en un sólo servidor, se van a encolar todas las requests que se hagan al server.
  - Si particiono los F.S por apellido, puedo acceder más rápido a la información. Puedo **paralelizar** esos accesos.
- **Replicar**: Orphan black y sus derivadas
  - Es tener copias idénticas del recurso. Puedo darle una copia a los de un lado, otra a los de otro, así no acaparo el ancho de banda principal.
  - Es una copia fiel, a diferencia del cache, más "pull".
- **Caching**: casi un clon, pero de una forma más específica
  - Tengo una sola fuente de información, pero tengo almacenamientos intermedios que le hacen de copia a los que me preguntan.
  - El cache es una copia "volátil", más "push".
  - Usar esto o una réplica cambia muchas cosas dentro de la arquitectura.

> El arte de hacer un sistema distribuido es hacer un trade-off entre escalabilidad, costos y capacidades.

## YAC de sistemas distribuidos
YAC = yet another classification

YAML = yet another markup language

- **Computación de alta performance**
  - Cluster computing (están todos juntos)
  - Grid computing (sistema descentralizado cooperando)
    - Masivo, muchas computadoras.
- **Sistemas de información distribuidos**
  - Este es el mundo empresarial de esos días
  - Enterprise application integration
- **Sistemas ubicuos** (pervasive)
  - IoT
- **Sistemas para dispositivos móviles**

## Derribando mitos
**Verdadero o falso**:
- La red es confiable
- La red es segura
- La red es homogénea
- La topología de la red no cambia
- La latencia es cero
- El ancho de banda es infinito
- El costo de comunicación es cero
- Hay una sola administración

> Spoiler: son todas falsas.

## Arquitectura de software
La idea principal es conocer los patrones de arquitectura que podemos usar para conectar sus partes.
Tenemos que preguntarnos cosas como:
- **¿Qué distribución funcional y técnica de componentes usamos?**
- **¿Cómo conectamos las piezas de software?**

La elección de la arquitectura define las características del sistema:
- Capacidades, restricciones y desempeño
- Estilo arquitectónico

### Estilos arquitectónicos
Hay básicamente 3 estilos:
- Por capas
- Orientada a servicios
- Pub/Sub

#### Por capas
Siempre van de arriba para abajo.
**Ejemplo**: Stack de comunicación TCP, la arquitectura que siguen todos los proyectos de Spring.

Aplicaciones por capas. Modelo de 3 capas (aplicación, procesos y datos).

#### Orientada a servicios
Separo componentes funcionales en vez de por nivel de abstracción.

Criterios/formas para distribuir:
- Objetos
- Componentes
- Recursos (REST)

Es necesario saber los contratos de los componentes disponibles para usar, para saber qué me ofrece.
No tiene mucha ciencia:
- Tengo un servicio que me devuelve la ubicación geográfica de una IP
- Tengo otro que, luego de autenticarme, me devuelve mi saldo de Mercado Pago
- ...
Compongo estos servicios para desarrollar mis funcionalidades.

Distinción importante entre arquitecturas:
- ¿Necesito algún "ware" en el "middle"?
- Se comunican las partes directamente sin intermediarios

Middleware sirve para enviar mensajes entre orígenes y destinatarios. Es un cacho de software que se para en el medio y hace de mediador entre cliente y servidor, por ejemplo.
Es una pieza de software más para administrar.

|                              | **Acoplado temporalmente**                                    | **Desacoplado temporalmente**                                                     |
| ---------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Acoplado x referencia**    | Comunicación directa online.<br/>• Llamada REST               | Mailbox:<br/>• Te dejo el mensaje                                                 |
| **Desacoplado x referencia** | Eventos<br/>• Notificar algo y los que están escuchando hacen | Espacio compartido de datos<br/>• Digo algo y los que quieren lo toman y accionan |


#### Pub/Sub
Tenés un montón de soluciones: Apache Kafka, Redis, RabbitMQ, etc.

Es un diseño desacoplado. Requiere una pieza de software adicional como intermediario.

No requiere que productores y consumidores estén disponibles al mismo tiempo. La asincronía requiere cierta relajación de los requerimientos de performance.

La diferencia principal entre eventos y espacio compartido es la persistencia del mensaje.

### Middleware
Mediar entre componentes vía interfaces.
Modelos:
- Wrappers
- Interceptor

La diferencia radica en lo siguiente:
- El wrapper es una implementación distinta que encapsula una implementación ya existente, pero le agrego comportamiento.
  - Ej: File System. Tengo que leer un archivo puntual. No sé si estoy leyendo un disco físico o uno en la nube. Con la implementación que ya tenía sólo podía leer discos físicos, pero con el Wrapper que implementaron en la última versión puedo leer discos en OneDrive (?).
- El interceptor se pone más abajo, casi a nivel de protocolo, y en lugar de hacer la llamada directa lo manda por detrás a otro servicio. Ataja la llamada en el medio y la reenvía.
  - Ej: File System. No sé qué disco estoy leyendo para acceder a un archivo en particular porque me lo resuelve el Interceptor que opera en el medio.

### Otra vuelta de la arquitectura por capas
Cliente - Servidor: el clásico / casi una reliquia.
Multi capas - algo más común, siempre separamos un poco más.

Ejemplos
- NFS
  - Network File System
- WWW (World-Wide-Web)
  - Abajo de todo está TCP/IP.

## Criterios de distribución
Distribución vertical y horizontal.

**Vertical**: tengo varios nodos que hacen lo mismo
**Horizontal**: tengo un nodo que cumple distintas funciones

Cuando están desacoplados, ¿cómo encuentro al destinatario?

¿Qué función cumplen los nodos? ¿Son todos iguales?

Distribución estructurada vs. peer to peer.

## Conclusiones
Hay un montón de opciones para distribuir los componentes.
La forma determina problemas y soluciones.
Elegir una forma adecuada para los requerimientos es fundamental.

**Arquitectura del sistema** = distribución física de procesos y conexiones
> La de sistema es la más técnica.
**Arquitectura de software** = estuctura funcional y patrones de uso


# Procesos
## Procesos e hilos
Tanto procesos como threads son formas de ejecutar en paralelo distintas funciones del sistema (Obvio...¿no?)

Los thread nos permiten separar las operaciones lentas (como el I/O) para no entorpecer el funcionamiento general del sistema.

Es una decisión de arquitectura interna del programa como usar los threads para mejorar el rendimiento general.

Muchas veces confiamos en la plataforma para que nos resuelva el manejo de threads pero a veces es importante ajustarlo a nuestras necesidades.

## Virtualización
La clásica (toda la compu)

Contenedores
- Un poco más liviano
- Docker, Kubernetes

Clientes en entornos virtuales
- La clásica terminal
- X Windows
- Escritorios remotos

La virtualización tiene, en cierto punto, un beneficio sobre la fiabilidad en runtime (?).

## Clientes
> El que representa a los usuarios.

Representan la interfaz de los clientes contra los servicios:
- Escritorios remotos
- Protocolos de acceso a servicios (NFS)
- Web Browser
- Progressive Web Apps

## Servidores
> El que atiende a todos los clientes.
En la mayoría de los casos hay un patrón común:
- Reciben conexiones en puertos de red.
- Procesan pedidos y devuelven una respuesta.

Los threads que se ejecutan en un server describe la arquitectura de software como procesan los pedidos

Hay servers que mantienen estado de sus clientes:
- Stateful vs. Stateless
- Back For Front (BFF).
  - Están tuneados para lo que necesitan para las aplicaciones móviles.
  - Si los servicios de backend de abajo cambian, sólo cambia el Back For Front y no la implementación directa de la aplicación móvil.

Definir que vas a usar un BFF es una decisión de arquitectura de software.

Como se implementa el escalamiento del server HTTP o TCP: 
- Balanceador de carga.
  - Es un intermediario que tiene que existir casi siempre en este tipo de sistemas.
  - Es un pasamano que intercepta el mensaje, se fija quién está disponible y se lo manda.
  - Si se quiere hacer escalamiento, es necesario un balanceador de carga.
  - Existen versiones físicas y de software.

## Migración de código
> Dentro de la virtualización.

¿Qué hay que tener en cuenta para permitir una migración?
- Soporte de la infraestructura
- Características de soporte (reinicios, notificaciones)

**Escalado horizontal o vertical**
Ejemplos:
- VmWare
  - Migra una máquina de un equipo al otro y vos no te enteraste.
- Kubernetes
  - Si vos querés escalarlo, te baja el POD y te lo levanta en otro lado. Te hace un reinicio para este "autoescalado".
- Azure
- AWS

La virtualización y el escalamiento tiene sus chiches para cuando se quiera migrar la infraestructura.

## Conclusiones
Los procesos son la base de cualquier infraestructura de software, aunque sean centralizados o distribuidos.

La arquitectura interna de los procesos con threads es fundamental para la arquitectura del sistema.

La mayoría de las veces, nuestros procesos corren en ambientes virtualizados, y la migración de código se hace de forma transparente.

Sin embargo, es importante entender como los cambios de base afectan los procesos en ejecución.


# TP1
Están pensando en hacer un servicio que dada una IP te devuelva una ubicación, y otro servicio que dada una coordinada te devuelva un clima. 

Escalándolo...
- Cientos de miles de personas tratando de usarlo.

