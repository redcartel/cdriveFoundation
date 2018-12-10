
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

def get_id(dictionary, name):
    if name in dictionary:
        return dictionary[name]['student-id']
    else:
        return None

print(get_id(dictionary, 'carter'))
print(get_id(dictionary, 'nikil'))
