import requests

def get_articles(topic) :
    url = "https://newsapi.org/v2/everything?q=" + topic + "&from=2022-10-15&sortBy=publishedAt&apiKey=37f3f5562d6449778e935ffbbed23970"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text