"""
Producer: publica mensajes en una cola durable de RabbitMQ.

Demuestra la ÚNICA garantía que da un MoM (de la teórica): el mensaje queda
insertado en la queue de destino. Y nada más. El consumer puede estar caído:
cuando vuelva, los mensajes siguen ahí. Eso es comunicación persistente y
asíncrona.

Cómo correr:
    python3 producer.py                  # publica 5 tareas de ejemplo
    python3 producer.py hola "tarea ..." # publica los mensajes que le pases
"""
import sys

import pika

QUEUE = "tareas"


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    # durable=True -> la definición de la cola sobrevive a un reinicio del broker.
    channel.queue_declare(queue=QUEUE, durable=True)

    mensajes = sys.argv[1:] or [f"tarea-{i}" + "." * i for i in range(1, 6)]
    for msg in mensajes:
        channel.basic_publish(
            exchange="",          # default exchange: rutea por nombre de cola
            routing_key=QUEUE,
            body=msg.encode(),
            properties=pika.BasicProperties(
                delivery_mode=2,  # mensaje persistente: se escribe a disco
            ),
        )
        print(f" [x] enviado: {msg}")

    connection.close()


if __name__ == "__main__":
    main()
