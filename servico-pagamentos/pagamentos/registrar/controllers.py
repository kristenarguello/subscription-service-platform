from datetime import datetime
from typing import Literal

import pymongo
from fastapi import HTTPException

from ..async_event import publish_event
from .schemas import RegistrarPagamento


async def registrar_pagamento(body: RegistrarPagamento):
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

    collection = db["aplicativos"]
    aplicativo = collection.find_one({"codigo": assinatura["cod_aplicativo"]})
    if aplicativo is not None and body.valorPago != aplicativo["custo_mensal"]:
        raise HTTPException(
            status_code=400,
            detail=f"O valor do pagamento deve ser igual ao valor da assinatura. O valor da assinatura é de {aplicativo['custo_mensal']}",
        )

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

    await publish_event(body)
