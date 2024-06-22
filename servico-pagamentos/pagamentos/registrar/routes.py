from typing import Literal

from fastapi import APIRouter, HTTPException
from loguru import logger

from . import controllers as controller
from .schemas import RegistrarPagamento

router = APIRouter(prefix="/registrarpagamento", tags=["registrarpagamento"])


@router.post("", status_code=200)
@router.post("/", status_code=200, include_in_schema=False)
async def registrar_pagamento(body: RegistrarPagamento):
    try:
        # Make sure to await the asynchronous function
        return await controller.registrar_pagamento(body)
    except HTTPException as http_exc:
        # If an HTTPException is raised, re-raise it to be handled by FastAPI
        raise http_exc
    except Exception as e:
        # Log the error and raise an HTTPException for any other errors
        logger.error(f"Failed to register payment: {e}")
        raise HTTPException(status_code=500, detail="Failed to register payment")
