from typing import Literal
from pydantic import BaseModel
from datetime import datetime


class CreateAssinatura(BaseModel):
    codigo_cliente: int
    codigo_aplicativo: int


class Assinatura(BaseModel):
    codigo: int
    cod_aplicativo: int
    cod_cliente: int
    inicio_vigencia: datetime
    fim_vigencia: datetime


class GetAssinaturas(BaseModel):
    cod_assinatura: int
    cod_cliente: int
    cod_aplicativo: int
    data_inicio: datetime
    data_fim: datetime
    status: Literal["ATIVA", "CANCELADA"]
