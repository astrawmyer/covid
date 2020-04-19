""" Reads US daily data from covidtracking.com and makes a graph of positive per day. """

import requests
import json
import matplotlib.pyplot as plt
import numpy as np

usaData = requests.get("https://covidtracking.com/api/us/daily")
jsonUSA = json.loads(usaData.content)

stateData = requests.get("https://covidtracking.com/api/v1/states/daily.json")
jsonStates = json.loads(stateData.content)

def USApos():
    pos = []
    for x in jsonUSA:
        pos.insert(0,x['positive'])
    plt.plot(pos)
    plt.show()

def StatePos():
    pos = []
    for x in jsonStates:
        if x['state'] == "OK":
            pos.insert(0,x['positive'])
    plt.plot(pos)
    plt.show()



if __name__ == "__main__":
    main_switch_function = {"1": USApos, "2": StatePos, "3": USApos, "4": USApos, "5": exit}
    while True:
        print("What do you want to do?")
        response = input("1. USA Positive chart, 2. Create a Report, 3. Send all letters, 4. Projection, 5. Quit: ")
        try:
            main_switch_function.get(response)()
        except TypeError:
            print("Not a valid input.")