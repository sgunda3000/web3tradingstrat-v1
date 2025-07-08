import json
from datetime import datetime
import os

class PaperAccount:
    def __init__(self, initial_balance=10000, log_file="logs/paper_trades.log"):
        self.balance = initial_balance
        self.positions = {}
        self.log_file = log_file
        os.makedirs("logs", exist_ok=True)

    def log_trade(self, action, symbol, qty, price):
        trade = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "symbol": symbol,
            "quantity": qty,
            "price": price
        }
        with open(self.log_file, "a") as f:
            f.write(json.dumps(trade) + "\n")
        print(f"[PAPER TRADE] {action} {qty} of {symbol} at ${price}")

    def execute_trade(self, action, symbol, qty, price):
        cost = qty * price
        if action == "BUY" and self.balance >= cost:
            self.balance -= cost
            self.positions[symbol] = self.positions.get(symbol, 0) + qty
        elif action == "SELL" and self.positions.get(symbol, 0) >= qty:
            self.balance += cost
            self.positions[symbol] -= qty
        self.log_trade(action, symbol, qty, price)
