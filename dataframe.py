import requests
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

usaData = requests.get("https://covidtracking.com/api/us/daily")
jsonUSA = json.loads(usaData.content)

stateData = requests.get("https://covidtracking.com/api/v1/states/daily.json")
jsonStates = json.loads(stateData.content)

USA = pd.read_json("https://covidtracking.com/api/us/daily")
print(USA)

plt.plot(USA['positive'])
plt.show()