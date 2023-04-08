import pandas as pd
import numpy as np
import yfinance as yf
import talib

# Download stock data
data = yf.download("AAPL", start="2020-01-01", end="2021-01-01")

# Define indicators
data['MA20'] = talib.SMA(data['Close'], timeperiod=20)
data['upper'], data['middle'], data['lower'] = talib.BBANDS(data['Close'], timeperiod=20)
data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
data['MACD'], data['MACD_signal'], data['MACD_hist'] = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

# Define trading signals
data['long_signal'] = np.where((data['Close'] > data['MA20']) &
                               (data['Close'] < data['upper']) &
                               (data['RSI'] < 30) &
                               (data['MACD'] > data['MACD_signal']), 1, 0)
data['short_signal'] = np.where((data['Close'] < data['MA20']) &
                                (data['Close'] > data['lower']) &
                                (data['RSI'] > 70) &
                                (data['MACD'] < data['MACD_signal']), 1, 0)
data['position'] = data['long_signal'] - data['short_signal']

# Calculate profits
data['buy'] = np.where(data['position'] == 1, data['Close'], np.nan)
data['sell'] = np.where(data['position'] == -1, data['Close'], np.nan)
data['profit'] = data['sell'] - data['buy']
total_profit = data['profit'].sum()
print(f"Total profit: {total_profit}")