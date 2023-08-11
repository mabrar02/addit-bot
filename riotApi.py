import requests
from keys import RIOT_API_KEY

def riotApiCall(url):
    api_req = "%s?api_key=%s" % (url, RIOT_API_KEY)
    response = requests.get(api_req)
    data = response.json()
    return data

def getLastMatches(puuid, count):
    api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/%s/ids?type=ranked&start0&count=%d&api_key=%s" % (puuid, count, RIOT_API_KEY)
    response = requests.get(api_url)
    data = response.json()
    return data

def getMatchData(matchId):
    api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/%s" % (matchId)
    return riotApiCall(api_url) 


def getAccountInfo(accName):
    accName.replace(" ", "%20")
    api_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + accName
    return riotApiCall(api_url)