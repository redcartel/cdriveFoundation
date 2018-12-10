import json

test_dictionary = {
    "key1" : 100,
    "key2" : "value",
    "key3" : [0, 1, 2, 3, 4, 5],
    "key4" : {
        "this" : "is",
        "a" : "sub",
        "dictionary" : None
    }
}

with open("output.json", "w") as output_file:
    json.dump(test_dictionary, output_file, indent=1)