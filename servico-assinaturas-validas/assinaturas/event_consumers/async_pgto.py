import asyncio

from aio_pika import ExchangeType, IncomingMessage, connect
from loguru import logger

from ..validacao.controllers import callback_pgtoassinaturavalida


async def event_consumer_init():
    # Establish a connection to RabbitMQ
    logger.debug("Connecting to RabbitMQ")
    connection = await connect("amqp://guest:guest@localhost/")
    channel = await connection.channel()

    # Declare the exchange if it doesn't exist
    exchange = await channel.declare_exchange("payments_events", ExchangeType.DIRECT)

    # Declare the queue if it doesn't exist
    queue = await channel.declare_queue("pgto_servico_assinatura_valida_queue")

    # Bind the queue to the exchange
    await queue.bind(exchange, routing_key="pgto_servico_assinatura_valida")

    async def on_message(message: IncomingMessage):
        logger.debug("Processing message")
        async with message.process():
            body = message.body
            ch = message.channel
            method = message.delivery_tag
            properties = message.properties

            # Run the synchronous callback in the default executor
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(
                None, callback_pgtoassinaturavalida, ch, method, properties, body
            )

    # # Start consuming messages
    await queue.consume(on_message)  # type: ignore
