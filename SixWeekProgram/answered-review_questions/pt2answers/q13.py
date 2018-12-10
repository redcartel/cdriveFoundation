
import json

file_object = open("example.json", "r")

data = json.load(file_object)

for key in data:
    print(key)

file_object.close()
