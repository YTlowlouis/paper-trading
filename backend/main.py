from fastapi import FastAPI
from pydantic import BaseModel
from app.api import trading, portfolio

webapp = FastAPI()

webapp.include_router(trading.router, prefix="/trade")
webapp.include_router(portfolio.router, prefix="/portfolio")

@webapp.get("/health")
async def root():
    return {"status": "ok"}
