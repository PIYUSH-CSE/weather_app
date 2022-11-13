# API-Key


import requests


def api_key(city):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": "{}".format(city)}
    headers = {
        "X-RapidAPI-Key": "5813e2cf35mshca95fb7c1db2f5dp1ed490jsn579d844299d5",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    op = response.json()

    key = "0d00acd719839fccd88d35731c5dd059"

    url1 = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}'
    response1 = requests.get(url1)
    op1 = response1.json()
    return op, op1
