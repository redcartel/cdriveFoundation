import json
import pprint

with open("simple.json", "r") as file_object:
    dictionary = json.load(file_object)

for key in dictionary:
    print("{} : {}".format(key, dictionary[key]))
