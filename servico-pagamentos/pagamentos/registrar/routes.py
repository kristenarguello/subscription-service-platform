from fastapi import APIRouter
from typing import Literal
from . import controllers as controller

router = APIRouter(prefix="/registrarpagamento", tags=["registrarpagamento"])


@router.post("", status_code=201)
@router.post("/", status_code=201, include_in_schema=False)
def registrar_pagamento(tipo: Literal["cadastro", "assinatura_valida"]):
    return controller.registrar_pagamento(tipo)
