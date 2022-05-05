from notification_manager import send_email
import requests
from flight_data import FINAL_LOC, STARTING_LOC
from flight_search import Flight
flight = Flight()
class DataManager:
    def update(self):
        response1 = requests.get(url="https://api.sheety.co/85af671b56f941cac2a6be9a342a0f9f/copyOfFlightDeals/prices/")
        data1 = response1.json()
        response2 = requests.get(url="https://api.sheety.co/85af671b56f941cac2a6be9a342a0f9f/copyOfFlightDeals/users/")
        data2 = response2.json()
        for users in data2["users"]:
            
            i = 0
            for key in FINAL_LOC:
                try:
                    price = flight.search(STARTING_LOC, FINAL_LOC[key], 60, 90)
                except:
                    print("No flights found")
                
                if data1["prices"][i]["lowestPrice"] > price:
                    message = f"""Low price Alert!
                    Flight from Mumbai to {key} has a low price of {price}
                    """
                    send_email(message, users["email"])
                i+=1


            
            
             




