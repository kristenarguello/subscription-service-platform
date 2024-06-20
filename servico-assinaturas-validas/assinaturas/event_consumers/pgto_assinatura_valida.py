import pika
import json
from ..cache import remove_from_cache
from loguru import logger


def callback_pgtoassinaturavalida(ch, method, properties, body):
    event_data = json.loads(body)
    cod_assinatura = event_data["codass"]
    remove_from_cache(cod_assinatura)
    logger.debug(f"Event handler: {cod_assinatura} removed from cache.")


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
