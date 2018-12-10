
import json

file_object = open("example.json", "r")
data = json.load(file_object)

print(len(data))
