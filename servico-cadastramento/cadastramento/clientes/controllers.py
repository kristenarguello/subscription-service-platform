from .schemas import GetClientes
from ..assinaturas.schemas import GetAssinaturas


def get_clientes() -> list[GetClientes]:
    raise NotImplementedError


def get_assinaturas_cliente(codigo_cli: int) -> list[GetAssinaturas]:
    raise NotImplementedError
