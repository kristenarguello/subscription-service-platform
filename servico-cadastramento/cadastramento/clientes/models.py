from pydantic import BaseModel


class ClientesDAO(BaseModel):
    codigo: int
    nome: str
    email: str
