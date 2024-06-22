import pika
from ..validacao.controllers import callback_pgtoassinaturavalida


def event_consumer_init():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="pgto_servico_assinatura_valida_queue")

    channel.queue_bind(
        exchange="payments_events",
        queue="pgto_servico_assinatura_valida_queue",
        routing_key="pgto_servico_assinatura_valida",
    )

    channel.basic_consume(
        queue="pgto_servico_assinatura_valida_queue",
        on_message_callback=callback_pgtoassinaturavalida,
        auto_ack=True,
    )
    channel.start_consuming()
