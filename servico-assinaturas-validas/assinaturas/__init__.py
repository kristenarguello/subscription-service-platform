from fastapi import FastAPI

from .health.health import router as health_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="AssinaturasValidas",
    )
    app.include_router(health_router, prefix="/health")
    return app
