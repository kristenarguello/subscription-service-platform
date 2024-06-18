from pydantic import BaseModel


class GetClientes(BaseModel):
    codigo: int
    nome: str
    email: str
