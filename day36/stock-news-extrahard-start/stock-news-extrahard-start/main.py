from pyexpat.errors import messages
import requests
import datetime
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":"abcd"
}

yesterday = datetime.date.today() - datetime.timedelta(days=3)
d_b_yesterday = datetime.date.today() - datetime.timedelta(days=4)

data = requests.get(url="https://www.alphavantage.co/query", params=parameters).json()
y_stock = float(data["Time Series (Daily)"][f"{yesterday}"]["4. close"])
d_b_y_stock = float(data["Time Series (Daily)"][f"{d_b_yesterday}"]["4. close"])

if abs(y_stock-d_b_y_stock)/d_b_y_stock > 0.05:
    parameters = {
        "apikey":"abcd",
        "q":"Tesla"
    }
    news = requests.get(url="https://newsapi.org/v2/top-headlines", params=parameters).json()
    if y_stock-d_b_y_stock < 0:
        s_message = f'{STOCK}: 🔻%{round(abs(y_stock-d_b_y_stock)/d_b_y_stock*100, 2)}%' 
    else:
        s_message = f'{STOCK}: 🔺%{round(abs(y_stock-d_b_y_stock)/d_b_y_stock*100, 2)}%'
    
    account_sid = "abcd"
    api_key = "abcd"
    client = Client(account_sid, api_key)
    
    s_message += f'Heading:{news["articles"][0]["title"]}\n Description:{news["articles"][0]["description"]}'

    message = client.messages \
                    .create(
                    body="s_message",
                    from_="1234",
                    to="1234"
                )
    print(message.status)
