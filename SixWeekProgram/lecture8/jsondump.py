import json # very important

studentgrades = {
        "Carter" : 60.5,
        "Kenso" : 74.9,
        "Greg" : 87.5,
        "Kai" : 92.8,
        "Rak" : 100.0
    }

# write json to file:

file_object = open("grades.json", "w")
json.dump(studentgrades, file_object)
file_object.close()

# easy as that

bigger_data = {
        "record1" : {
            "coordinates" : [1020101.122, 2103020.1232],
            "name" : "secret missile silo"
            },
        "record2" : {
            "coordinates" : [-1292192.139, 8238238238.12129 ],
            "name" : "secret volcano hideout"
            },
        "record3" : {
            "coordinates" : [742848484.12, 439824.43],
            "name" : "vault of stolen art"
            }
        }

file_object = open("villains.json", "w")
json.dump(bigger_data, file_object, indent=2)
file_object.close()

