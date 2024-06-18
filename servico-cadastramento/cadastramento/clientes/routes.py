from fastapi import APIRouter
from .schemas import GetClientes
from . import controllers as controller
from ..assinaturas.schemas import GetAssinaturas

router = APIRouter(prefix="/clientes", tags=["clientes"])


@router.get("/clientes", status_code=200)
@router.get("/clientes/", status_code=200, include_in_schema=False)
def get_clientes() -> list[GetClientes]:
    return controller.get_clientes()


@router.get("/asscli/{codigo_cli}", status_code=200)
@router.get("/asscli/{codigo_cli}/", status_code=200, include_in_schema=False)
def get_assinaturas_cliente(codigo_cli: int) -> list[GetAssinaturas]:
    return controller.get_assinaturas_cliente(codigo_cli)
