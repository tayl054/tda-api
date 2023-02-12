from tda import auth, client
import json

token_path = 'C:\Users\GREG\VS_CODE\tda-api\tda-api'
api_key = 'QCGZOCCCTTOAXUV1XNMNJW5FJLINKCM8@AMER.OAUTHAP'
redirect_uri = 'https://localhost'
try:
    c = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executible_path='C:\Users\GREG\VS_CODE\tda-api\tda-api\chromedriver') as driver:
        c = auth.client_from_login_flow(
            driver, api_key, redirect_uri, token_path)

r = c.get_price_history('AAPL',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
assert r.ok, r.raise_for_status()
print(json.dumps(r.json(), indent=4))
