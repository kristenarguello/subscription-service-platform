import json
from datetime import datetime

import requests
from fastapi import HTTPException
from loguru import logger

from ..cache import Cache

cache = Cache()
from ..settings import Settings

settings = Settings()


def callback_pgtoassinaturavalida(ch, method, properties, body):
    event_data = json.loads(body)
    cod_assinatura = event_data["codass"]
    cache.remove_from_cache(cod_assinatura)
    logger.debug(f"Event handler: {cod_assinatura} removed from cache.")


def validar_assinatura(codass: int) -> bool:
    cached_info = cache.get_from_cache(codass)
    logger.debug(f"CACHE: {cached_info}")
    if cached_info:
        if (
            datetime.strptime(cached_info["data_fim"], "%Y-%m-%dT%H:%M:%S.%f")
            >= datetime.now()
        ):
            return True
        cache.remove_from_cache(codass)
        return False

    response = requests.get(settings.ASSINATURAS_URL)
    assinaturas = response.json()
    logger.debug(f"Assinaturas: {assinaturas}")
    for assinatura in assinaturas:
        if assinatura["cod_assinatura"] == codass:
            cache.add_to_cache(codass, assinatura)
            return True

    raise HTTPException(status_code=404, detail="Assinatura não encontrada")
