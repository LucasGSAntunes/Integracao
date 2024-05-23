from fastapi import FastAPI, HTTPException
from functions.filterData import filterData
from models.LeadModel import Lead

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/data/")
async def get_data(dados: Lead):
    return dados