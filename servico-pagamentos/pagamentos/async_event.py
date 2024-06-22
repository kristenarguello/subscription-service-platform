import json

from aio_pika import ExchangeType, Message, connect
from loguru import logger

from .registrar.schemas import RegistrarPagamento


async def publish_event(body: RegistrarPagamento):
    # Establish a connection to RabbitMQ
    connection = await connect("amqp://guest:guest@localhost/")
    channel = await connection.channel()

    # Declare the exchange if it doesn't exist
    exchange = await channel.declare_exchange("payments_events", ExchangeType.DIRECT)

    logger.debug(f"Event: {body.model_dump()}")
    routing_keys = ["pgto_cadastramento", "pgto_servico_assinatura_valida"]
    for routing_key in routing_keys:
        message = Message(body=json.dumps(body.model_dump()).encode())
        # Publish the message to the exchange with the specified routing key
        await exchange.publish(message, routing_key=routing_key)
        logger.debug(f"Event published to {routing_key}")

    # Close the channel and connection when done
    await channel.close()
    await connection.close()
