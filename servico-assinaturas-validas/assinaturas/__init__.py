from fastapi import FastAPI

from . import apps, dependencies


def create_app() -> FastAPI:
    app = FastAPI(
        title="AssinaturasValidas",
    )
    return app
