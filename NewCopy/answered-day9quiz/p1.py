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

for key in dictionary:
    record = dictionary[key]
    print("{}, {}, {}".format(key, record["student-id"], record["gpa"]))


