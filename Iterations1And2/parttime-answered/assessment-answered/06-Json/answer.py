import json

with open("market-data.json", "r") as file_object:
    dictionary = json.load(file_object)

outdict = {}
for key in dictionary:
    name = dictionary[key]["Name"]
    symbol = dictionary[key]["Symbol"]
    price = dictionary[key]["LastPrice"]
    outdict[name] = {
        "Symbol": symbol,
        "LastPrice": price
    }

with open("processed.json", "w") as f:
    json.dump(outdict, f)