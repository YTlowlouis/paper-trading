import random

class TradingEngine:
    def __init__(self):
        self.cash = 10000
        self.positions = {}
        self.prices = {
            "AAPL": 150,
            "TSLA": 250,
            "BTC": 40000
        }

    def get_price(self, symbol: str) -> int:
        base = self.prices.get(symbol, 100)
        return round(base * random.uniform(0.98, 1.02), 2)

    def get_portfolio(self) -> dict:
        return {
            "cash": self.cash,
            "positions": self.positions
        }

    def buy(self, symbol: str, quantity: int) -> dict:
        price = self.get_price(symbol)
        cost = price * quantity

        if cost > self.cash:
            return {"error": "not enough cash"}

        self.cash -= cost
        self.positions[symbol] = self.positions.get(symbol, 0) + quantity

        return {
            "action": "buy",
            "symbol": symbol,
            "qty": quantity,
            "price": price,
            "cash_left": self.cash
        }

    def sell(self, symbol, qty):
        if self.positions.get(symbol, 0) < qty:
            return {"error": "Not enough shares"}

        price = self.get_price(symbol)
        revenue = price * qty

        self.cash += revenue
        self.positions[symbol] -= qty
        if self.positions[symbol] == 0:
            self.positions.pop(symbol)

        return {
            "action": "SELL",
            "symbol": symbol,
            "qty": qty,
            "price": price,
            "cash": self.cash
        }
