import ccxt
import time

class BrokerAPI:
    def __init__(self, exchange_name, api_key, secret):
        self.exchange = ccxt.__getattr__(exchange_name)({
            'apiKey': api_key,
            'secret': secret
        })

    def get_balance(self):
        return self.exchange.fetch_balance()

    def get_market_data(self, symbol='BTC/USDT'):
        return self.exchange.fetch_ticker(symbol)

    def place_order(self, symbol, side, amount, price=None):
        if side == 'buy':
            return self.exchange.create_limit_buy_order(symbol, amount, price)
        elif side == 'sell':
            return self.exchange.create_limit_sell_order(symbol, amount, price)
        else:
            raise ValueError("Invalid order side")
