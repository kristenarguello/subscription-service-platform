from fastapi import FastAPI

from .health.health import router as health_router
from .validacao.routes import router as assinaturas_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="AssinaturasValidas",
    )
    app.include_router(health_router, prefix="/health")
    app.include_router(assinaturas_router)
    return app
