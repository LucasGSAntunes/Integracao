from fastapi import FastAPI

def create_app():
    app = FastAPI(
        title="API de Integração",
        description="API para integração de dados",
        docs_url="/docs",
    )
    return app

app = create_app()