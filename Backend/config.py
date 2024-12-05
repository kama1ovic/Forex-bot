import os

class Config:
    API_KEY = os.getenv('API_KEY', 'your_api_key_here')
    API_SECRET = os.getenv('API_SECRET', 'your_api_secret_here')
    BASE_URL = 'https://api.binance.com'  # Example broker API base URL
    SYMBOL = 'BTC/USDT'  # Example trading pair
    TIMEFRAME = '1m'  # Timeframe for data
    STOP_LOSS = 50  # Default stop loss in percentage
    TAKE_PROFIT = 100  # Default take profit in percentage
