import json
import requests

def get_articles(topic) :
    url = "https://newsapi.org/v2/everything?q=" + topic + "&from=2022-10-15&sortBy=publishedAt&apiKey=37f3f5562d6449778e935ffbbed23970"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    domain_names(json.dumps(response.json()))

    return response.text

def domain_names(jsonFile):
    j = json.loads(jsonFile)
    wiki = []

    for s in j.get('articles'):
        wiki.append(mediaWiki(s.get('source')['name']))

    print(wiki)
    return  wiki

def mediaWiki(source):
    url = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=10&exlimit=1&titles=" + source + "&explaintext=1&formatversion=2&format=json"

    payload = {}
    headers = {
        'Cookie': 'GeoIP=US:VA:Ashburn:39.05:-77.49:v4; WMF-Last-Access-Global=15-Nov-2022; WMF-Last-Access=15-Nov-2022; enwikiBlockID=14675105%21c32a1f79e2c70302b86474755e78359e47dec74eee8732be91eac3225a047ac43e4369487c6c8b10d8bdda45c8aaeb72bb61b8617327897e5d3af54b54c8e37f'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text