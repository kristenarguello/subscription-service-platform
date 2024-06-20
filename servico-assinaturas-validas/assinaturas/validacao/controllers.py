from datetime import datetime
from fastapi import HTTPException
import requests
from ..cache import get_from_cache


def validar_assinatura(codass: int) -> bool:
    cached_info = get_from_cache(codass)
    if cached_info:
        if cached_info["fim_vigencia"] >= datetime.now():
            return True
        return False

    response = requests.get(f"http://localhost:8000/assinaturas")
    assinaturas = response.json()
    for assinatura in assinaturas:
        if assinatura["cod_assinatura"] == codass:
            if assinatura["data_fim"] >= datetime.now():
                return True
            return False

    raise HTTPException(status_code=404, detail="Assinatura não encontrada")
