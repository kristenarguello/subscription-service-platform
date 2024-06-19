import pika
import json


def callback_pagamentoservicocadastramento(ch, method, properties, body):
    event_data = json.loads(body)
    print("CADASTRAMENTO", event_data)
    print("aaaa")


def event_consumer_init():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="pgto_cadastramento_queue")

    channel.basic_consume(
        queue="pgto_cadastramento_queue",
        on_message_callback=callback_pagamentoservicocadastramento,
        auto_ack=True,
    )
    channel.start_consuming()
