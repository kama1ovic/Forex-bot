import pandas as pd
import numpy as np

# Example function to calculate Moving Average
def moving_average(data, window=14):
    return data['close'].rolling(window=window).mean()

# Example function to calculate RSI (Relative Strength Index)
def relative_strength_index(data, window=14):
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
