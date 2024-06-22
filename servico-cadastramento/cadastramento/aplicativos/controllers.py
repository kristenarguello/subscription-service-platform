from fastapi import HTTPException
import pymongo
from .schemas import GetAplicativos, UpdateApp
from ..assinaturas.schemas import GetAssinaturas
from ..assinaturas.controllers import parse_assinaturas_from_db


def get_aplicativos() -> list[GetAplicativos]:
    client = pymongo.MongoClient("localhost", 27017)
    db = client["cadastro_geral"]
    collection = db["aplicativos"]
    aplicativos_cursor = collection.find(projection={"_id": 0})
    return list(aplicativos_cursor)


def update_aplicativo(aplicativo_id: int, body: UpdateApp) -> GetAplicativos:
    client = pymongo.MongoClient("localhost", 27017)
    db = client["cadastro_geral"]
    collection = db["aplicativos"]
    update = collection.update_one(
        {"codigo": aplicativo_id}, {"$set": {"custo_mensal": body.custo}}
    )
    if update.matched_count == 0:
        raise HTTPException(status_code=404, detail="Aplicativo não encontrado")

    aplicativo = collection.find({"codigo": aplicativo_id}, projection={"_id": 0})
    aplicativo = list(aplicativo)[0]
    return GetAplicativos(
        codigo=aplicativo["codigo"],
        nome=aplicativo["nome"],
        custo_mensal=aplicativo["custo_mensal"],
    )


def get_assinaturas(cod_aplicativo: int) -> list[GetAssinaturas]:
    client = pymongo.MongoClient("localhost", 27017)
    db = client["cadastro_geral"]
    collection = db["assinaturas"]
    assinaturas_cursor = collection.find(
        filter={"cod_aplicativo": cod_aplicativo}, projection={"_id": 0}
    )
    return parse_assinaturas_from_db(list(assinaturas_cursor))
