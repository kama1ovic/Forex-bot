import pandas as pd
import numpy as np
import talib
from strategy import Strategy

def backtest_strategy(data):
    strategy = Strategy(data)
    signals = []
    for i in range(len(data)):
        signal = strategy.get_signal(data[:i])
        signals.append(signal)

    return signals

# Load historical data
data = pd.read_csv('historical_data.csv')
signals = backtest_strategy(data)
