from fastapi import HTTPException
import pymongo
from datetime import datetime, timedelta
from typing import Literal
from .schemas import Assinatura, CreateAssinatura, GetAssinaturas


def get_assinaturas(
    tipo: Literal["TODAS", "ATIVAS", "CANCELADAS"]
) -> list[GetAssinaturas]:
    filters = {}
    if tipo == "ATIVAS":
        filters["inicio_vigencia"] = {"$lte": datetime.now()}
        filters["fim_vigencia"] = {"$gte": datetime.now()}
    elif tipo == "CANCELADAS":
        filters["fim_vigencia"] = {"$lt": datetime.now()}

    client = pymongo.MongoClient("localhost", 27017)
    db = client["cadastro_geral"]
    collection = db["assinaturas"]
    assinaturas_cursor = collection.find(filter=filters, projection={"_id": 0})

    return parse_assinaturas_from_db(list(assinaturas_cursor))


def create_assinatura(body: CreateAssinatura) -> Assinatura:
    client = pymongo.MongoClient("localhost", 27017)
    db = client["cadastro_geral"]

    collection_clientes = db["clientes"]
    cliente = collection_clientes.find({"codigo": body.codigo_cliente})
    if len(list(cliente)) == 0:
        raise HTTPException(
            status_code=404, detail="Cliente não encontrado para criar assinatura"
        )

    collection_aplicativos = db["aplicativos"]
    aplicativo = collection_aplicativos.find({"codigo": body.codigo_aplicativo})
    if len(list(aplicativo)) == 0:
        raise HTTPException(
            status_code=404, detail="Aplicativo não encontrado para criar assinatura"
        )

    collection = db["assinaturas"]
    assinatura = {
        "codigo": collection.count_documents({}) + 1,
        "cod_cliente": body.codigo_cliente,
        "cod_aplicativo": body.codigo_aplicativo,
        "inicio_vigencia": datetime.now(),
        "fim_vigencia": datetime.now() + timedelta(days=7),  # initial 7 days
    }
    collection.insert_one(assinatura)

    return Assinatura(
        codigo=assinatura["codigo"],
        cod_aplicativo=assinatura["cod_aplicativo"],
        cod_cliente=assinatura["cod_cliente"],
        inicio_vigencia=assinatura["inicio_vigencia"],
        fim_vigencia=assinatura["fim_vigencia"],
    )


def parse_assinaturas_from_db(assinaturas_cursor: list) -> list[GetAssinaturas]:
    assinatura_result = []
    for assinatura in assinaturas_cursor:
        assinatura_result.append(
            GetAssinaturas(
                cod_assinatura=assinatura["codigo"],
                cod_cliente=assinatura["cod_cliente"],
                cod_aplicativo=assinatura["cod_aplicativo"],
                data_inicio=assinatura["inicio_vigencia"],
                data_fim=assinatura["fim_vigencia"],
                status=is_active(assinatura),
            )
        )
    return assinatura_result


def is_active(assinatura) -> Literal["ATIVA", "CANCELADA"]:
    if (
        assinatura["inicio_vigencia"] <= datetime.now()
        and assinatura["fim_vigencia"] >= datetime.now()
    ):
        return "ATIVA"
    return "CANCELADA"
