import requests

def fetch_data():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    return response.json()
