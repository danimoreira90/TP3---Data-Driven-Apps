from fastapi import FastAPI
from .dependencies.data_manager import fetch_energy_data

app = FastAPI()

@app.get("/energy")
async def get_energy_data(limit: int = 5, query: str = ""):
    data = fetch_energy_data(limit, query)
    return data
