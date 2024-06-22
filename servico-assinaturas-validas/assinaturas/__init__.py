import asyncio

from fastapi import FastAPI

from .event_consumers.async_pgto import event_consumer_init
from .health.health import router as health_router
from .validacao.routes import router as assinaturas_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="AssinaturasValidas",
    )
    app.include_router(health_router, prefix="/health")
    app.include_router(assinaturas_router)

    @app.on_event("startup")
    async def startup_event():
        loop = asyncio.get_event_loop()
        loop.create_task(event_consumer_init())

    return app
