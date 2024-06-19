import json

import pika
from loguru import logger

from .registrar.events import (
    PagamentoServicoAssinaturaValida,
    PagamentoServicoCadastramento,
)

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue="pgto_cadastramento_queue")
channel.queue_declare(queue="pgto_servico_assinatura_valida_queue")


def publish_event(event_type: str, data: dict):
    # TODO: change values
    if event_type == "cadastro":
        queue_name = "pgto_cadastramento_queue"
        body = PagamentoServicoCadastramento(
            dia=19, mes=6, ano=2024, codass=1, valorPago=5.4
        )
    elif event_type == "assinatura_valida":
        queue_name = "pgto_servico_assinatura_valida_queue"
        body = PagamentoServicoAssinaturaValida(
            dia=19, mes=6, ano=2024, codass=2, valorPago=9.3
        )
    else:
        return "Invalid event type"
    logger.debug(f"Event: {body.model_dump()}")

    channel.basic_publish(
        exchange="", routing_key=queue_name, body=json.dumps(body.model_dump())
    )
    logger.debug(f"Event published to {queue_name}")
