from fastapi import APIRouter, FastAPI

from .health.health import router as health_router
from .aplicativos.routes import router as aplicativos_router
from .clientes.routes import router as clientes_router
from .assinaturas.routes import router as assinaturas_router


def create_app() -> FastAPI:
    app = FastAPI(title="Cadastramento")
    app.include_router(health_router, prefix="/health")
    app.include_router(clientes_router)
    app.include_router(aplicativos_router)
    app.include_router(assinaturas_router)
    return app
