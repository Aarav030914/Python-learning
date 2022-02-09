from urllib import response
import requests
questions = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
questions.raise_for_status()
print(questions.json())