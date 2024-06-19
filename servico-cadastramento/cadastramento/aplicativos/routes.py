from fastapi import APIRouter
from . import controllers as controller
from ..assinaturas.schemas import GetAssinaturas
from .schemas import UpdateApp


router = APIRouter(prefix="/aplicativos", tags=["aplicativos"])


@router.get("/aplicativos", status_code=200)
@router.get("/aplicativos/", status_code=200, include_in_schema=False)
def get_aplicativos():
    return controller.get_aplicativos()


@router.patch("/aplicativos/{aplicativo_id}", status_code=200)
@router.patch("/aplicativos/{aplicativo_id}/", status_code=200, include_in_schema=False)
def update_aplicativo(aplicativo_id: int, body: UpdateApp):
    return controller.update_aplicativo(aplicativo_id, body)


@router.get("/assapp/{cod_aplicativo}", status_code=200)
@router.get("/assapp/{cod_aplicativo}/", status_code=200, include_in_schema=False)
def get_assinaturas_aplicativo(cod_aplicativo: int) -> list[GetAssinaturas]:
    return controller.get_assinaturas(cod_aplicativo)
