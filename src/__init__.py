from fastapi import FastAPI
from src.config import Settings

def create_app():
    app = FastAPI(
        title="API de Integração",
        description="API para integração de dados",
        version="Settings.API_VERSION",
        docs_url="/docs",
    )
    return app

app = create_app()