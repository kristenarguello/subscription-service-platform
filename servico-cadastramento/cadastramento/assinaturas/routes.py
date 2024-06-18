from typing import Literal
from fastapi import APIRouter

from . import controllers as controller
from .schemas import Assinatura, CreateAssinatura

router = APIRouter(prefix="/assinaturas", tags=["assinaturas"])


@router.post("/assinaturas", status_code=201)
@router.post("/assinaturas/", status_code=201, include_in_schema=False)
def create_assinatura(body: CreateAssinatura) -> Assinatura:
    return controller.create_assinatura(body)


@router.get("/assinaturas/{tipo}", status_code=200)
@router.get("/assinaturas/{tipo}/", status_code=200, include_in_schema=False)
def get_assinaturas(tipo: Literal["TODAS", "ATIVAS", "CANCELADAS"]):
    return controller.get_assinaturas(tipo)
