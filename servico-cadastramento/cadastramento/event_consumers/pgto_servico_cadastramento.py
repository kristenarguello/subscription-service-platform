import json
from datetime import timedelta

import pika
import pymongo
from loguru import logger


def callback_pagamentoservicocadastramento(ch, method, properties, body):
    event_data = json.loads(body)
    cod_assinatura = event_data["codass"]
    client = pymongo.MongoClient("localhost", 27017)
    db = client["cadastro_geral"]
    collection = db["assinaturas"]

    assinatura = collection.find_one({"codigo": cod_assinatura})
    if assinatura:
        current_datetime = assinatura["fim_vigencia"]
        new_datetime = current_datetime + timedelta(days=30)

        collection.update_one(
            {"codigo": cod_assinatura}, {"$set": {"yourDateField": new_datetime}}
        )
        logger.debug(
            f"Event handler: Document with codigo {cod_assinatura} has been updated."
        )
    else:
        logger.debug(f"Event handler: No document found with codigo {cod_assinatura}.")


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
