import datetime
import requests

class Flight:          
    def search(self, start, final, after_dt, till_dt):
        fr_time = datetime.datetime.today()+datetime.timedelta(days=after_dt)
        to_time = datetime.datetime.today()+datetime.timedelta(days=till_dt)
        self.header = {
            "apikey":"PS84_84vHsml7tJvKPEBp8e3K6aLp-aF"
        }
        self.parameters = {
            "fly_from":start,
            "fly_to":final,
            "date_from":fr_time.strftime(r"%d/%m/%Y"),
            "date_to":to_time.strftime(r"%d/%m/%Y"),
            "one_per_date":1,
            "limit":1,
            "adults":1,
            "children":0,
            "infants":0,
            "curr":"INR"
        }
        response = requests.get("https://tequila-api.kiwi.com/v2/search", params=self.parameters, headers=self.header)
        data = response.json().get("data")[0]
        price = data.get("price")
        return price   
        

