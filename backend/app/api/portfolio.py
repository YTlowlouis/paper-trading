from fastapi import APIRouter
from app.core.engine import engine

router = APIRouter()

@router.get("/")
async def get_portfolio():
    return engine.get_portfolio()
