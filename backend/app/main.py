from fastapi import FastAPI
from model import TradingEngine
from pydantic import BaseModel

app = FastAPI()
engine = TradingEngine()

class OrderRequest(BaseModel):
    symbol: str
    quantity: int

@app.get("/health")
async def root():
    return {"status": "ok"}


@app.get("/portfolio")
async def get_portfolio():
    return engine.get_portfolio()
