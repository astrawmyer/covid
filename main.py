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
    
    while True:
        state = input("What State?\n")
        state = state.upper()
        pos = []
        for x in jsonStates:
            if x['state'] == state:
                pos.insert(0,x['positive'])
        plt.plot(pos)
        plt.ylabel("Positive Cases")
        plt.xlabel("Days")
        plt.suptitle(state)
        plt.show()
        leave = input("Exit to main menu?(Y/N)\n")
        leave = leave.upper()
        if leave == "Y":
            break

def StateNewPos():
    
    while True:
        state = input("What State?\n")
        state = state.upper()
        pos = []
        for x in jsonStates:
            if x['state'] == state:
                pos.insert(0,x['positiveIncrease'])
        plt.plot(pos)
        plt.ylabel("New Positive Cases")
        plt.xlabel("Days")
        plt.suptitle(state)
        plt.show()
        leave = input("Exit to main menu?(Y/N)\n")
        leave = leave.upper()
        if leave == "Y":
            break

if __name__ == "__main__":
    main_switch_function = {"1": USApos, "2": StatePos, "3": StateNewPos, "4": exit}
    while True:
        print("What do you want to do?")
        response = input("1. USA Cumulative Positive\n2. State Cumulative Positive\n3. State New Positive\n4. Quit:\n")
        try:
            main_switch_function.get(response)()
        except TypeError:
            print("Not a valid input.")