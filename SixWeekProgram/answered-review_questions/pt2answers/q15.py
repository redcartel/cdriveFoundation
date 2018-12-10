import json

file_object = open("example2.json", "r")

data = json.load(file_object)

for key in data:
    print(key, data[key][0])

file_object.close()
