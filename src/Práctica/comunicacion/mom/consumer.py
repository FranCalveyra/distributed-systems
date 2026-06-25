"""
Consumer: procesa mensajes de la cola con ACK manual y fair dispatch.

Levantá VARIAS instancias en paralelo (varias terminales) para ver el patrón
work-queue: el broker reparte los mensajes entre los consumers disponibles.
Con prefetch=1 no le manda un mensaje nuevo a un consumer hasta que confirmó
(ack) el anterior — así no se le acumula trabajo a uno mientras otro está libre.

El ack manual es clave: el mensaje recién se borra de la cola cuando el consumer
confirma que lo procesó. Si el consumer se cae antes de hacer ack, RabbitMQ
re-encola el mensaje y se lo da a otro. Eso es la "confiabilidad" del MoM.

Cómo correr:
    python3 consumer.py
"""
import time

import pika

QUEUE = "tareas"


def callback(ch, method, _properties, body):
    msg = body.decode()
    print(f" [.] procesando: {msg}")
    time.sleep(msg.count(".") + 1)  # simula trabajo proporcional a los puntos
    print(f" [v] listo:      {msg}")
    ch.basic_ack(delivery_tag=method.delivery_tag)  # recién acá se borra de la cola


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE, durable=True)

    channel.basic_qos(prefetch_count=1)  # fair dispatch: de a uno por consumer
    channel.basic_consume(queue=QUEUE, on_message_callback=callback)

    print(" [*] esperando mensajes. CTRL+C para salir.")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        connection.close()


if __name__ == "__main__":
    main()
