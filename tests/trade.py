from tda import auth, client
import json

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
print(json.dumps(r.json(), indent=4))

##from tda import auth, client
##import json

#token_path = 'C:\Users\GREG\VS_CODE\tda-api\tda-api'

##account_id = 686232781
##token_path = 'token'
##api_key = 'QCGZOCCCTTOAXUV1XNMNJW5FJLINKCM8@AMER.OAUTHAP'
##redirect_uri = 'https://localhost'
##try:
##    c = auth.client_from_token_file(token_path, api_key)
##except FileNotFoundError:
##    from selenium import webdriver
##    with webdriver.Chrome(executable_path='c://Users//GREG//VS_CODE//tda-api//tda-api//chromedriver') as driver:
##        c = auth.client_from_login_flow(
##            driver, api_key, redirect_uri, token_path)

#r = c.get_price_history('AAPL',
#                        period_type=client.Client.PriceHistory.PeriodType.YEAR,
#                        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
#                        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
#                        frequency=client.Client.PriceHistory.Frequency.DAILY)
#assert r.ok, r.raise_for_status()
#print(json.dumps(r.json(), indent=4))

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