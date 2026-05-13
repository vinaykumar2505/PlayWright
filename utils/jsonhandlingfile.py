import json

def jsonFile(filepath):
 #reading the JSON file
    with open(filepath) as json_file:
        credentials = json.load(json_file)
        return credentials