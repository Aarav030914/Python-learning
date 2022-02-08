import requests


MY_LAT = 21.764473
MY_LONG = 72.151932


def check_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])
    
    if (abs(iss_lat - MY_LAT) < 5) and (abs(iss_long - MY_LONG) < 5) :
        return True
    else:
        return False     