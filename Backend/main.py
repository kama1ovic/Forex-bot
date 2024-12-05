from flask import Flask, jsonify, request
import ccxt
from config import Config
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the Binance API (example)
exchange = ccxt.binance({
    'apiKey': app.config['API_KEY'],
    'secret': app.config['API_SECRET'],
})

@app.route('/get_price', methods=['GET'])
def get_price():
    ticker = exchange.fetch_ticker(app.config['SYMBOL'])
    return jsonify({
        'symbol': app.config['SYMBOL'],
        'price': ticker['last']
    })

@app.route('/place_order', methods=['POST'])
def place_order():
    data = request.get_json()
    side = data.get('side')  # 'buy' or 'sell'
    amount = data.get('amount')
    price = data.get('price')

    # Place order with basic stop-loss and take-profit logic
    if side == 'buy':
        order = exchange.create_market_buy_order(app.config['SYMBOL'], amount)
    elif side == 'sell':
        order = exchange.create_market_sell_order(app.config['SYMBOL'], amount)
    else:
        return jsonify({'error': 'Invalid order type'}), 400
    
    return jsonify({'order': order})

@app.route('/get_history', methods=['GET'])
def get_history():
    # Example of getting past trades
    trades = exchange.fetch_my_trades(app.config['SYMBOL'])
    return jsonify({'trades': trades})

if __name__ == '__main__':
    app.run(debug=True)
