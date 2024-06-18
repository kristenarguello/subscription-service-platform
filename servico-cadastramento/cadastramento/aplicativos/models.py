from pydantic import BaseModel


class AplicativosDAO(BaseModel):
    codigo: int
    nome: str
    custo_mensal: float
