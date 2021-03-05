import requests
import json
import pprint

url = "https://api.opensea.io/api/v1/assets"

querystring = {"order_direction":"desc","offset":"0","limit":"1"}

response = requests.request("GET", url, params=querystring)
r = requests.get(url, params=querystring)

json_data = r.json()

pprint.pprint(json_data)
