from pydantic import BaseModel
from datetime import datetime


class AssinaturasDAO(BaseModel):
    codigo: int
    cod_aplicativo: int
    cod_cliente: int
    inicio_vigencia: datetime
    fim_vigencia: datetime
