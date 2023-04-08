import yfinance
from tda import auth, client
import json
import pandas_ta as ta
import pandas as pd

#import ccxt
#exchange = ccxt.binance()
#bars = exchange.fetch_ohlcv('ETH/USDT', timeframe='5m', limit=500)
#df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
#print(df)

ticker = yfinance.Ticker("TSLA")
df = ticker.history(period="1y")

#Print Yfinance TSLA = 1 yr
#print(df)


account_id = 686232781
token_path = 'token'
api_key = 'QCGZOCCCTTOAXUV1XNMNJW5FJLINKCM8@AMER.OAUTHAP'
redirect_uri = 'https://localhost'

try:
    c = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome() as driver:
        c = auth.client_from_login_flow(
            driver, api_key, redirect_uri, token_path)

r = c.get_price_history('AAPL',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
assert r.status_code == 200, r.raise_for_status()
print(df)
adx = ta.adx(df['High'], df['Low'], df['Close'])
# I can comment out prior line if combine df. and ta.adx() which takes care of the colum headings
#adx = df.ta.adx()

#macd = df.ta.macd(fast=14, slow=28)

#print(macd)

#rsi = df.ta.rsi()
#print(rsi)

#df = pd.concat([df, adx, macd, rsi], axis=1)

#print(df)

#df = df[df['RSI_14'] < 30]
#help(ta.adx)
#print(df)

#Concat Example
#dfpd = df
#dfadx = df.ta.adx()
#dfadx = df.ta.adx()
#dftotal = pd.concat(dfpd, dfadx)
#print(dftotal)









##from tda import auth, client
##import json

##account_id = 686232781
##token_path = 'token'
##api_key = 'QCGZOCCCTTOAXUV1XNMNJW5FJLINKCM8@AMER.OAUTHAP'
##redirect_uri = 'https://localhost'
##try:
##    c = auth.client_from_token_file(token_path, api_key)


###from tda.orders.equities import equity_buy_limit
###from tda.orders.common import Duration, Session

#client = ... # See "Authentication and Client Creation"

###response = c.place_order(
###    account_id,  # account_id
###    equity_buy_limit('RDFN', 1, 8.0)
###        .set_duration(Duration.GOOD_TILL_CANCEL)
###        .set_session(Session.SEAMLESS)
###        .build())

#builder = OrderBuilder('RDFN', 5)
#builder.set_instructions(OrderBuilder.Instruction.BUY)
#builder.set_order_type(OrderBuilder.OrderType.LIMIT)
#builder.set_price(8.10)
#builder.set_duration(Duration.GOOD_TILL_CANCEL)
#builder.set_session(Session.NORMAL)

#response = c.place_order(account_id, builder.build())
#response = c.get_quote('BA')

#print(response.json())