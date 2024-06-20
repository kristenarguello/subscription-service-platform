from fastapi import APIRouter
from typing import Literal
from . import controllers as controller
from .schemas import RegistrarPagamento

router = APIRouter(prefix="/registrarpagamento", tags=["registrarpagamento"])


@router.post("", status_code=201)
@router.post("/", status_code=201, include_in_schema=False)
def registrar_pagamento(body: RegistrarPagamento):
    return controller.registrar_pagamento(body)
