import json

file_object = open("villains.json", "r")
data_dict = json.load(file_object)
file_object.close()

for record in data_dict:
    print(record, ":")
    print("    coords: ", data_dict[record]["coordinates"])
    print("    asset : ", data_dict[record]["name"])
