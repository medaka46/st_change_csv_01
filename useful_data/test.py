from binance.client import Client
import pandas as pd

# import datetime
from datetime import datetime


# Your Binance API key and secret key
api_key = "9mLBNUqAX5O4V25FUTCT5BEycllM5q1yjwGkqf95x6dnJqQ5KEROFULLGnfQZUqE"
api_secret = "2PVYffej74Odsc7WXoOCubkUK07moF4P3dAgfffFjdGFWE3Ykq8kNU9eoPnTPw3V"

# Create a Binance client instance
client = Client(api_key, api_secret)

# Define the start date
start_date = '2019-09-08 00:00:00'  # Start date in the format 'YYYY-MM-DD HH:MM:SS'

# Get historical klines for BTCUSDT
candles = client.get_klines(
    symbol='BTCUSDT', 
    interval=Client.KLINE_INTERVAL_5MINUTE,
    # interval=Client.KLINE_INTERVAL_1DAY, 
    start_str=start_date,
    limit=5)

# Print the result
for candle in candles:
    print(candle)

df = pd.DataFrame(candles, columns=[
    'Open Time', 'Open', 'High', 'Low', 'Close', 'Volume',
    'Close Time', 'Quote Asset Volume', 'Number of Trades',
    'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume', 'Ignore'
])