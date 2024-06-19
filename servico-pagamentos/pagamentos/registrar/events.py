from pydantic import BaseModel


class PagamentoServicoCadastramento(BaseModel):
    dia: int
    mes: int
    ano: int
    codass: int
    valorPago: float


class PagamentoServicoAssinaturaValida(BaseModel):
    dia: int
    mes: int
    ano: int
    codass: int
    valorPago: float
