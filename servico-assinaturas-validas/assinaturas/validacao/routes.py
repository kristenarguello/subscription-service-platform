from fastapi import APIRouter
from . import controllers as controller

router = APIRouter(prefix="/assinvalidas", tags=["validarassinatura"])


@router.get("/{codass}", status_code=200)
@router.get("/{codass}/", status_code=200, include_in_schema=False)
def validar_assinatura(codass: int) -> bool:
    return controller.validar_assinatura(codass)
