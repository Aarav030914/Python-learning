import requests
from twilio.rest import Client
import os
parameters = {
    "lat":42.430420,
    "lon":19.259363,
    "appid":"c7ea1a3837bd7e968c53d36d195b62fc",
    "exclude":"current,minutely,daily"
}

account_sid = "AC3e38aa2f1028efc3f4e31ece3082920a"
auth_token = "49841c629171d06314fe17c9ba0e4a64"
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


