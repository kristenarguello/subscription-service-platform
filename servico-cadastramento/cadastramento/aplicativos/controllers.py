from .schemas import GetAplicativos
from ..assinaturas.schemas import GetAssinaturas


def get_aplicativos() -> list[GetAplicativos]:
    raise NotImplementedError


def update_aplicativo(aplicativo_id: int) -> GetAplicativos:
    raise NotImplementedError


def get_assinaturas(cod_aplicativo: int) -> list[GetAssinaturas]:
    raise NotImplementedError
