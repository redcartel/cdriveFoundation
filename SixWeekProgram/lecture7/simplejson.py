""" Dictionaries """

import json

dictionary = {
    "key1" : 5,
    "key2" : "value",
    "key3" : [0, 2, 4, 6, 8]
}

with open("simple.json", "w") as file_object:
    json.dump(dictionary, file_object, indent=2)
