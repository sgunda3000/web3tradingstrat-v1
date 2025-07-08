import yaml
from strategy import moving_average_strategy
import pandas as pd
from paper_trading_account import PaperAccount
import random

class Trader:
    def __init__(self, config_file="config.yaml", paper=True):
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)
        self.symbols = self.config['symbols']
        self.trade_amount = self.config['trade_amount']
        self.paper = paper
        if paper:
            self.account = PaperAccount(initial_balance=10000)

    def fetch_mock_data(self, symbol):
        # Simulated historical price data
        prices = [random.uniform(50, 150) for _ in range(50)]
        return pd.DataFrame({"close": prices})

    def execute_trade(self, symbol, qty, price, signal):
        if self.paper:
            self.account.execute_trade(signal, symbol, qty, price)

    def trade(self):
        for symbol in self.symbols:
            print(f"Checking {symbol}...")
            data = self.fetch_mock_data(symbol)
            signal = moving_average_strategy(data)
            print(f"Signal for {symbol}: {signal}")
            price = data['close'].iloc[-1]
            qty = self.trade_amount / price
            if signal in ["BUY", "SELL"]:
                self.execute_trade(symbol, qty, price, signal)
            else:
                print(f"No action for {symbol}")
