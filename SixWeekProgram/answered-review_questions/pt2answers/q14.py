import json

file_object = open("example.json")
data = json.load(file_object)
file_object.close()

data["five"] = 5

file_object = open("example.json", "w")
json.dump(data, file_object, indent=2)
file_object.close()
