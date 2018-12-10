import json

filename = "data.json"

try:
    with open(filename, "r") as file_object:
        data = json.load(file_object)
except FileNotFoundError:
    data = {}

n = len(data)
newkey = "newdata{}".format(n)

data[newkey] = "some new data"

with open(filename, "w") as file_object:
    json.dump(data, file_object, indent=2)
