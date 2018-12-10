import json

file_object = open("example3.json", "r")
data = json.load(file_object)
file_object.close()

data["kai"] = {
        "studentID": "0004",
        "GPA": 91.2
        }

file_object = open("example3.json", "w")
json.dump(data, file_object, indent=2)
file_object.close()
