import requests
from keys import FORTUNE_API_KEY

fortunate = {}

def getFortune(user):

    if(fortunate.get(user) is None):
        url = "https://fortune-cookie2.p.rapidapi.com/fortune"

        headers = {
            "X-RapidAPI-Key": FORTUNE_API_KEY,
            "X-RapidAPI-Host": "fortune-cookie2.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        addKey(user, response.json()["answer"])
        return response.json()
    else:
        return


def addKey(user, fortune):
    fortunate[user] = fortune