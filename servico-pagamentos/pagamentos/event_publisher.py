import json

import pika
from loguru import logger

from .registrar.events import (
    PagamentoServicoAssinaturaValida,
    PagamentoServicoCadastramento,
)
from .registrar.schemas import RegistrarPagamento

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

exchange_name = "payments_events"
channel.exchange_declare(exchange=exchange_name, exchange_type="direct")


def publish_event(body: RegistrarPagamento):
    logger.debug(f"Event: {body.model_dump()}")
    routing_keys = ["pgto_cadastramento", "pgto_servico_assinatura_valida"]
    for routing_key in routing_keys:
        channel.basic_publish(
            exchange=exchange_name,
            routing_key=routing_key,
            body=json.dumps(body.model_dump()),
        )
        logger.debug(f"Event published to {routing_key}")
