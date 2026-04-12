from fastapi import APIRouter
from pydantic import BaseModel
from app.core.engine import engine

router = APIRouter()

class OrderRequest(BaseModel):
    symbol: str
    quantity: int

@router.post("/buy")
def buy(order: OrderRequest):
    return engine.buy(order.symbol, order.quantity)

@router.post("/sell")
def sell(order: OrderRequest):
    return engine.sell(order.symbol, order.quantity)
