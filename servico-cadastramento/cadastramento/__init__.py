import asyncio

from fastapi import APIRouter, FastAPI

from .aplicativos.routes import router as aplicativos_router
from .assinaturas.routes import router as assinaturas_router
from .clientes.routes import router as clientes_router
from .event_consumers.async_pgto import event_consumer_init
from .health.health import router as health_router


def create_app() -> FastAPI:
    app = FastAPI(title="Cadastramento")
    app.include_router(health_router, prefix="/health")
    app.include_router(clientes_router)
    app.include_router(aplicativos_router)
    app.include_router(assinaturas_router)

    @app.on_event("startup")
    async def startup_event():
        loop = asyncio.get_running_loop()
        loop.create_task(event_consumer_init())

    return app
