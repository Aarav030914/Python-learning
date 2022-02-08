import requests

def get_quote():
    quote = requests.get(url="https://api.kanye.rest/")
    print(quote.json())
get_quote()    