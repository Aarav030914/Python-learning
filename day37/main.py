import requests
import datetime
parameters = {
    "token":"dob14/09/2003",
    "username":"aaravjn",
    "agreeTermsOfService":"yes",
    "notMinor": "yes",

}
# response = requests.post(url="https://pixe.la/v1/users", json=parameters)
# print(response.text)
header = {
    "X-USER-TOKEN":"dob14/09/2003"
}
graph_config = {
    "id":"excr-graph",
    "name":"excercise graph",
    "unit":"min",
    "type":"int",
    "color":"sora"
}
# response = requests.post(url="https://pixe.la/v1/users/aaravjn/graphs", json=graph_config, headers=header)
# print(response.text)
today = datetime.date.today()

pixel_param = {
    "date": today.strftime(r"%Y%m%d"),
    "quantity": "10"    
}
pixel_update = {
    "quantity": "15"
}
# response = requests.post(url="https://pixe.la/v1/users/aaravjn/graphs/excr-graph", json=pixel_param, headers=header)
url = "https://pixe.la/v1/users/aaravjn/graphs/excr-graph/" + pixel_param["date"]
response = requests.put(url=url, json=pixel_update, headers=header)
print(response.text)
