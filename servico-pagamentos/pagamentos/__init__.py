from fastapi import APIRouter, FastAPI

from .health.health import router as health_router
from .registrar.routes import router as registrar_router


def create_app() -> FastAPI:
    app = FastAPI(title="Pagamentos")
    app.include_router(health_router, prefix="/health")
    app.include_router(registrar_router)
    return app
