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

def USANewPos():
    pos = []
    for x in jsonUSA:
        pos.insert(0,x['positiveIncrease'])
    plt.plot(pos)
    plt.show()

def USANewDeath():
    pos = []
    for x in jsonUSA:
        pos.insert(0,x['deathIncrease'])
    plt.plot(pos)
    plt.show()

def USAdeath():
    pos = []
    for x in jsonUSA:
        pos.insert(0,x['death'])
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
        plt.ylabel("Total Positive Cases")
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

def StateDeath():
    while True:
        state = input("What State?\n")
        state = state.upper()
        pos = []
        for x in jsonStates:
            if x['state'] == state:
                pos.insert(0,x['death']) #this is causing an error
        plt.plot(pos)
        plt.ylabel("Total Deaths")
        plt.xlabel("Days")
        plt.suptitle(state)
        plt.show()
        leave = input("Exit to main menu?(Y/N)\n")
        leave = leave.upper()
        if leave == "Y":
            break

def StateNewDeath():
    while True:
        state = input("What State?\n")
        state = state.upper()
        pos = []
        for x in jsonStates:
            if x['state'] == state:
                pos.insert(0,x['deathIncrease'])
        plt.plot(pos)
        plt.ylabel("New Deaths")
        plt.xlabel("Days")
        plt.suptitle(state)
        plt.show()
        leave = input("Exit to main menu?(Y/N)\n")
        leave = leave.upper()
        if leave == "Y":
            break

if __name__ == "__main__":
    main_switch_function = {"1": USApos, "2": USANewPos, "3": USAdeath, "4": USANewDeath, "5": StatePos, "6": StateNewPos, "7": StateDeath, "8": StateNewDeath, "9": exit}
    while True:
        print("What do you want to do?")
        response = input(
            "1. USA Cumulative Positive\n2. State Cumulative Positive\"3. State New Positive\n4. USA Cumulative Death\n5. Quit:\n")
        try:
            main_switch_function.get(response)()
        except TypeError:
            print("Not a valid input.")