import datetime
import requests
API_ID = ""
API_KEY = ""
parameters = {
    "query":input("What was your activity:"),
    "gender":"male",
    "weight_kg":65,
    "height_cm":180,
    "age": 18
}
header = {
    "x-app-id":API_ID,
    "x-app-key":API_KEY
}
response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", headers=header, json=parameters)
result = response.json()

time = datetime.datetime.now()
body = {
    "workout":{
        "date": datetime.date.today().strftime(r"%d/%m/%Y"),
        "time": f"{time.hour}:{time.minute}:{time.second}",
        "exercise":result["exercises"][0]["name"].title(),
        "duration":result["exercises"][0]["duration_min"],
        "calories":result["exercises"][0]["nf_calories"]
    }
}
print(body)
response = requests.post(url="https://api.sheety.co/*****/myWorkouts/workouts", json=body)
