from fastapi import FastAPI, Request
from typing import Dict

from src.app.fastapi_api.LeadService import lead_router
from fastapi.openapi.utils import get_openapi
from src.domain.entities.lead import Lead
from starlette.responses import StreamingResponse, JSONResponse

from src.app.utils import dependency_injection

app = FastAPI(
    title="API de Integração",
    description="API para integração de dados",
    version="0.1",
    docs_url="/docs",
)
app.include_router(lead_router)

@app.get("/", include_in_schema=False)
def api_root():
    return {"message": "Hello World"}

app.middleware("http")
async def before_request(request: Request, call_next):
    dependency_injection()

    response: StreamingResponse = await call_next(request)

    return response

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API de Integração",
        version="0.1",
        description="API para integração de dados",
        routes=app.routes,
    )
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi