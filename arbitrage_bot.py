import ccxt
import time
import pandas as pd
import numpy as np

# List of exchanges to monitor
exchanges = {
    'binance': ccxt.binance(),
    'kraken': ccxt.kraken(),
    'coinbase': ccxt.coinbase()
}

# Define the cryptocurrency pair
symbol = 'BTC/USDT'

def fetch_prices():
    """Fetch current prices from multiple exchanges."""
    prices = {}
    for name, exchange in exchanges.items():
        try:
            ticker = exchange.fetch_ticker(symbol)
            prices[name] = ticker['last']
        except Exception as e:
            print(f"Error fetching price from {name}: {e}")
    return prices

def find_arbitrage_opportunity(prices):
    """Identify the best arbitrage opportunity."""
    if len(prices) < 2:
        return None
    
    min_exchange = min(prices, key=prices.get)
    max_exchange = max(prices, key=prices.get)
    min_price = prices[min_exchange]
    max_price = prices[max_exchange]
    
    profit = max_price - min_price
    
    if profit > 0:
        return {
            'buy_exchange': min_exchange,
            'sell_exchange': max_exchange,
            'buy_price': min_price,
            'sell_price': max_price,
            'profit': profit
        }
    return None

def execute_trade(opportunity):
    """Execute buy and sell orders on respective exchanges."""
    print(f"Buying on {opportunity['buy_exchange']} at {opportunity['buy_price']}")
    print(f"Selling on {opportunity['sell_exchange']} at {opportunity['sell_price']}")
    print(f"Estimated profit per BTC: {opportunity['profit']}")
    # API key setup required to actually execute orders

# Main loop to monitor and execute arbitrage
while True:
    prices = fetch_prices()
    print("Current Prices:", prices)
    opportunity = find_arbitrage_opportunity(prices)
    if opportunity:
        execute_trade(opportunity)
    time.sleep(10)
