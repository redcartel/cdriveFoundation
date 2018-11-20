import json

infile = open("example.json", "r")
dictionary = json.load(infile)
print(len(dictionary))
