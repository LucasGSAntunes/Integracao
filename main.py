from fastapi import FastAPI
from src.models.LeadModel import Lead

app = FastAPI(
    title="API de Integração",
    description="API para integração de dados",
    version="0.1",
    docs_url="/docs",
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/data/")
async def get_data(dados: Lead):
    return dados