import pprint

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

dictionary['carter']['gpa'] = 2.5

dictionary['kai'] = {
        "student-id" : 4,
        "gpa" : 3.9
        }

pprint.pprint(dictionary)
