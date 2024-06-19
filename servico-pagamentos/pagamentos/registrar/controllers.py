from typing import Literal
from ..event_publisher import publish_event


def registrar_pagamento(tipo: Literal["cadastro", "assinatura_valida"]):
    publish_event(tipo, {"data": "data"})
