""" Reads US daily data from covidtracking.com and makes a graph of positive per day. """

import requests
import json
import matplotlib.pyplot as plt
import numpy as np

content = requests.get("https://covidtracking.com/api/us/daily")
json = json.loads(content.content)
pos = []
for x in json:
    pos.insert(0,x['positive'])
    #print(x['positive'])

print(pos)
xaxis = list(range(len(pos)))

plt.plot(pos)
plt.show()