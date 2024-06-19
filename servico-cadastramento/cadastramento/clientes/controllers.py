from datetime import datetime
from typing import Literal
import pymongo
from .schemas import GetClientes
from ..assinaturas.schemas import GetAssinaturas
from ..assinaturas.controllers import parse_assinaturas_from_db


def get_clientes() -> list[GetClientes]:
    client = pymongo.MongoClient("localhost", 27017)
    db = client["cadastro_geral"]
    collection = db["clientes"]

    clientes_cursor = collection.find(projection={"_id": 0})
    clientes_cursor = list(clientes_cursor)
    return clientes_cursor


def get_assinaturas_cliente(codigo_cli: int) -> list[GetAssinaturas]:
    client = pymongo.MongoClient("localhost", 27017)
    db = client["cadastro_geral"]
    collection = db["assinaturas"]

    assinaturas_cursor = collection.find(
        {"cod_cliente": codigo_cli}, projection={"_id": 0}
    )
    return parse_assinaturas_from_db(list(assinaturas_cursor))
