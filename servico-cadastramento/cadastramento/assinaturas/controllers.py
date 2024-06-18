from typing import Literal
from .schemas import Assinatura, CreateAssinatura, GetAssinaturas


def get_assinaturas(
    tipo: Literal["TODAS", "ATIVAS", "CANCELADAS"]
) -> list[GetAssinaturas]:
    raise NotImplementedError


def create_assinatura(body: CreateAssinatura) -> Assinatura:
    raise NotImplementedError
