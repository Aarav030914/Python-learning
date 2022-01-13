travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country, visits, list_of_cities):
    country_dict = {
        "country" : country,
        "visits" : visits,
        "list_of_cities" : list_of_cities 
    }
    travel_log.append(country_dict)
    print(travel_log)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])