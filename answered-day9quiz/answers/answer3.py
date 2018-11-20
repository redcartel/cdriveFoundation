import json

dictionary = {
    "carter" : {
        "student-id" : 1,
        "gpa" : 2.8
    },
    "greg" : {
        "student-id" : 2,
        "gpa" : 3.3
    },
    "kenso" : {
        "student-id" : 3,
        "gpa" : 3.7
    }
}

file_object = open("dictionary.json", "w")
json.dump(dictionary, file_object)
file_object.close()
