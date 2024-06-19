import pika
import json


def callback_pgtoassinaturavalida(ch, method, properties, body):
    event_data = json.loads(body)
    # print("Received Event 1:", event_data)
    print("ASSINATURA VALIDA", event_data)
    print("aaaa")


def event_consumer_init():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="pgto_servico_assinatura_valida_queue")

    channel.basic_consume(
        queue="pgto_servico_assinatura_valida_queue",
        on_message_callback=callback_pgtoassinaturavalida,
        auto_ack=True,
    )
    channel.start_consuming()
