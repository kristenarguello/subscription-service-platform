from pydantic import BaseModel


class RegistrarPagamento(BaseModel):
    dia: int
    mes: int
    ano: int
    codass: int
    valorPago: float
