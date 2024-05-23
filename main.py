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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)