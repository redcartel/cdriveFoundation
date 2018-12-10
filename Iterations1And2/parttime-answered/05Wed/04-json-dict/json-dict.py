import json

with open("tsla.json", "r") as f:
    dictionary = json.load(f)

for key in dictionary:
    print(key, ":", dictionary[key])

new_dictionary = {
    "Name": dictionary["Name"],
    "Symbol": dictionary["Symbol"],
    "LastPrice": dictionary["LastPrice"],
    "Volume": dictionary["Volume"]
}

with open("output.json", "w") as output_file:
    json.dump(new_dictionary, output_file)