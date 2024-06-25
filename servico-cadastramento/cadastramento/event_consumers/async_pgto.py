import asyncio
import json
from datetime import datetime, timedelta

import pymongo
from aio_pika import ExchangeType, IncomingMessage, connect
from loguru import logger

from ..settings import Settings

settings = Settings()


async def event_consumer_init():
    logger.debug("Connecting to RabbitMQ")
    connection = await connect(settings.RABBITMQ)
    channel = await connection.channel()
    exchange = await channel.declare_exchange("payments_events", ExchangeType.DIRECT)
    queue = await channel.declare_queue("pgto_cadastramento_queue")
    await queue.bind(exchange, routing_key="pgto_cadastramento")

    async def on_message(message: IncomingMessage):
        async with message.process():
            body = message.body
            # Convert the body to the expected format and call the callback function
            await callback_pagamentoservicocadastramento(body)

    # Start consuming messages as a background task
    await queue.consume(on_message)  # type: ignore


async def callback_pagamentoservicocadastramento(body):
    logger.debug("Processing message")
    event_data = json.loads(body)
    cod_assinatura = event_data["codass"]
    client = pymongo.MongoClient(settings.MONGO_DB_URI)
    db = client["cadastro_geral"]
    collection = db["assinaturas"]

    assinatura = collection.find_one({"codigo": cod_assinatura})

    if assinatura:
        data_pagamento = datetime(
            day=event_data["dia"], month=event_data["mes"], year=event_data["ano"]
        )
        fim_vigencia = assinatura["fim_vigencia"]

        if fim_vigencia < data_pagamento:
            new_datetime = data_pagamento + timedelta(days=30)
        else:
            new_datetime = fim_vigencia + timedelta(days=30)

        collection.update_one(
            {"codigo": cod_assinatura}, {"$set": {"fim_vigencia": new_datetime}}
        )
        logger.debug(
            f"Event handler: Document with codigo {cod_assinatura} has been updated."
        )
    else:
        logger.debug(f"Event handler: No document found with codigo {cod_assinatura}.")
