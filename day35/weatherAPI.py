import requests
from twilio.rest import Client
import os
parameters = {
    "lat":42.430420,
    "lon":19.259363,
    "appid":"abcd",
    "exclude":"current,minutely,daily"
}

account_sid = "abcd"
auth_token = "abcd"
bring_umbrella = False

data = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
data.raise_for_status()
w_data = data.json()
for i in range(0, 13):
    if w_data["hourly"][i]["weather"][0]["id"] < 700:
        bring_umbrella = True

if bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="I can rain today, don't forget your umbrella.",
                        from_='++19377313747',
                        to='+917487853240'
                    )
    print(message.status)                                 


