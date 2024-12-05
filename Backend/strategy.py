import talib
import numpy as np

class Strategy:
    def __init__(self, data):
        self.data = data

    def get_signal(self, market_data):
        close = np.array([data['close'] for data in self.data])
        sma_short = talib.SMA(close, timeperiod=50)
        sma_long = talib.SMA(close, timeperiod=200)

        if sma_short[-1] > sma_long[-1]:
            return 'buy'
        elif sma_short[-1] < sma_long[-1]:
            return 'sell'
        return 'hold'
