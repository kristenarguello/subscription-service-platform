from datetime import datetime
from typing import Literal
import pymongo

from fastapi import HTTPException
from ..event_publisher import publish_event
from .schemas import RegistrarPagamento


def registrar_pagamento(body: RegistrarPagamento):
    if body.valorPago < 0:
        raise HTTPException(
            status_code=400, detail="O valor do pagamento não pode ser negativo"
        )

    client = pymongo.MongoClient("localhost", 27017)
    db = client["cadastro_geral"]
    collection = db["assinaturas"]
    assinatura = collection.find_one({"codigo": body.codass})
    if not assinatura:
        raise HTTPException(status_code=404, detail="Assinatura não encontrada")

    data_pagamento = datetime(day=body.dia, month=body.mes, year=body.ano)
    db = client["pagamentos"]
    collection = db["pagamentos"]
    pagamento = {
        "codigo": collection.count_documents({}) + 1,
        "cod_assinatura": body.codass,
        "valor_pago": body.valorPago,
        "data_pagamento": data_pagamento,
    }
    collection.insert_one(pagamento)

    publish_event(body)
