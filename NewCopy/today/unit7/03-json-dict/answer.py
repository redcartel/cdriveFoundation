import json

myfile = open('tsla.json', 'r')
data = json.load(myfile)
myfile.close()

for key in data:
    print(key, data[key])

newdict = {}

newdict["Name"] = data["Name"]
newdict["Symbol"] = data["Symbol"]
newdict["LastPrice"] = data["LastPrice"]

outputfile = open('tsla_summary.json', 'w')
json.dump(newdict, outputfile)
outputfile.close()
