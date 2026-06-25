# MoM — Message-Oriented Middleware (RabbitMQ)

Ejemplo de comunicación **persistente y asíncrona** a través de un broker de mensajes real ([RabbitMQ](https://www.rabbitmq.com/)), con producer y consumer en **Python** (`pika`).

Demuestra el patrón **work queue** y la garantía central de un MoM que dice la teórica: *lo único que se asegura es que el mensaje queda insertado en la queue de destino*. El productor y el consumidor están **totalmente desacoplados** — ninguno necesita que el otro esté vivo en el mismo momento.

## Arquitectura

```
producer.py  ──publish──>  [ RabbitMQ: cola "tareas" ]  ──deliver──>  consumer.py
   (no sabe quién consume)        (broker intermediario)        (no sabe quién produjo)
```

- El **broker** persiste los mensajes (a disco, con `delivery_mode=2`). Si no hay consumers, se acumulan en la cola.
- Varios consumers compiten por la cola: el broker hace **fair dispatch** (round-robin con `prefetch=1`).
- **ACK manual**: el mensaje se borra recién cuando el consumer confirma que lo procesó. Si el consumer se cae antes, RabbitMQ lo re-encola y se lo da a otro.

## Prerrequisitos

- Docker (para levantar el broker)
- Python 3 + `pip install -r requirements.txt`

## Cómo correr

### 1. Levantar el broker

```bash
docker compose up -d
```

Management UI en http://localhost:15672 (user/pass: `guest` / `guest`) para ver las colas y los mensajes en vivo.

### 2. Levantar uno o más consumers

En una o varias terminales:

```bash
python3 consumer.py
```

### 3. Producir mensajes

```bash
python3 producer.py
```

## Qué observar

- **Desacople temporal**: corré primero el `producer.py` SIN consumers. Mirá en la UI que los mensajes quedan encolados. Después levantá un consumer y mirá cómo los procesa. Esa es la **comunicación persistente**.
- **Reparto de carga**: con 2+ consumers, el broker reparte las tareas entre ellos. Las tareas con más puntos (`...`) tardan más, y el fair dispatch evita que se le amontonen a uno solo.
- **Tolerancia**: matá un consumer (CTRL+C) mientras procesa. El mensaje sin ack vuelve a la cola y otro consumer lo retoma.

### Apagar todo

```bash
docker compose down
```

## ¿Por qué RabbitMQ y no Kafka?

Ambos son MoM, pero modelan cosas distintas:
- **RabbitMQ** es una **cola** (AMQP): el mensaje se consume y se borra. Ideal para work queues / reparto de tareas, que es lo que muestra este ejemplo.
- **Kafka** es un **log particionado**: los mensajes se retienen y los consumers leen por *offset*. Mejor para streaming y re-procesamiento.

Para ilustrar la garantía básica del MoM ("queda en la cola de destino") y el patrón producer/consumer, RabbitMQ es más simple de levantar y de leer.
