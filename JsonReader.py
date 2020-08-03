"""
JsonReader.py
Responsible for reading JSON file containing baseUrls
"""

# Imports
import json
from random import randint

class JsonReader:
    # Fields
    jsonData = ""
    jsonParsed = ""

    # Constructor
    def __init__(self, jsonFile):
        with open(jsonFile, "r") as jFile:
            self.jsonData = jFile.read()
        self.jsonParsed = json.loads(self.jsonData)

    # Gets an individual item from the list of URLs
    def getItem(self, pos):
        return self.jsonParsed["urls"][pos]

    # Get random url
    def getRandomUrl(self):
        size = len(self.jsonParsed["urls"])
        pos = randint(1, size-1)
        return self.getItem(pos)


    # To string
    def toString(self):
        print(self.jsonParsed)