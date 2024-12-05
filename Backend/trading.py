import time
import ccxt
from strategy import Strategy
from api_integration import BrokerAPI

class TradingBot:
    def __init__(self, api_key, secret, strategy):
        self.api = BrokerAPI('binance', api_key, secret)
        self.strategy = strategy

    def run(self):
        while True:
            market_data = self.api.get_market_data()
            signal = self.strategy.get_signal(market_data)
            
            if signal == 'buy':
                self.api.place_order('BTC/USDT', 'buy', 0.01, market_data['ask'])
            elif signal == 'sell':
                self.api.place_order('BTC/USDT', 'sell', 0.01, market_data['bid'])
            
            time.sleep(10)
