from fastapi import FastAPI
from auth.auth_routes import auth_router
from config import settings
from contextlib import asynccontextmanager

@asynccontextmanager
async def create_app():
    app = FastAPI(
        title="API de Integração",
        description="API para integração de dados",
        version="settings.API_VERSION",
        docs_url="/docs",
    )
    app.include_router(auth_router)
    return app

app = create_app()