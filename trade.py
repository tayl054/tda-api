import json
from tda import client, auth

<<<<<<< HEAD

#token_path = 'C:\\Users\\GREG\\VS_Projects\\tda-api\\tda-api\\'
token_path = 'token'
=======
token_path = 'token'
#token_path = 'C:\Users\GREG\VS_CODE\tda-api\tda-api'
>>>>>>> 4f560015b923f2b7015cc07cd5dc3e5288ef502f
api_key = 'QCGZOCCCTTOAXUV1XNMNJW5FJLINKCM8@AMER.OAUTHAP'
redirect_uri = 'https://localhost'
try:
    c = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver
<<<<<<< HEAD
    with webdriver.Chrome(executible_path='C:\\Users\\tayl054\\VS_Projects\\tda-api\\chromedriver') as driver:
=======
    with webdriver.Chrome(executible_path='//workspaces/tda-api/chromedriver') as driver:
>>>>>>> 4f560015b923f2b7015cc07cd5dc3e5288ef502f
        c = auth.client_from_login_flow(
            driver, api_key, redirect_uri, token_path)

r = c.get_price_history('AAPL',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
        frequency=client.Client.PriceHistory.Frequency.DAILY)
#assert r.ok, r.raise_for_status()

#df = r.json()
#print(df)
print(json.dumps(r.json(), indent=4))