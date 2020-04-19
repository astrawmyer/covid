import requests
import json
content = requests.get("https://covidtracking.com/api/us/daily")
json = json.loads(content.content)

for x in json:
    print(x['positive']).