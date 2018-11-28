
import json

data = { "Hello" : "World" }

file_object = open("output.json", "w")

json.dump(data, file_object, indent=2)
