from typing import Literal
from datetime import datetime

from pydantic import BaseModel


class GetAplicativos(BaseModel):
    codigo: int
    nome: str
    custo_mensal: float


class UpdateApp(BaseModel):
    custo: float


class GetAssinaturasAplicativo(BaseModel):
    codigo_assinatura: int
    codigo_cliente: int
    codigo_aplicativo: int
    data_inicio: datetime
    data_fim: datetime
    status: Literal["ATIVA", "CANCELADA"]
