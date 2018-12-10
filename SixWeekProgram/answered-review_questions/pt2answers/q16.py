import json

file_object = open("example3.json", "r")

data = json.load(file_object)

for key in data:
    print(key, data[key]['studentID'])

file_object.close()
