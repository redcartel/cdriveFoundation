import json

def read_data(filename):
    try:
        file_object = open("records.json", "r")
        data = json.load(file_object)
        file_object.close()
    except FileNotFoundError:
        data = {}
    return data


def write_data(data, filename):
    file_object = open("records.json", "w")
    json.dump(data, file_object)
    file_object.close()


def splitgrades(string):
    gradestrings = string.split()
    grades = []
    for grade in gradestrings:
        grades.append(float(grade))
    return grades


data = read_data("records.json")

name = input("What is the student's first name? ")

hwgrades = input("Input the student's homework grades. Separate numbers by spaces: ")

hwgradelist = splitgrades(hwgrades)

quizgrades = input("Input the student's quiz grades. Separate numbers by spaces: ")

quizgradelist = splitgrades(quizgrades)

testgrades = input("Input the student's test grades. Separate numbers by spaces: ")

testgradelist = splitgrades(testgrades)

newrecord = {
        "name" : name,
        "homework" : hwgradelist,
        "quizzes" : quizgradelist,
        "tests": testgradelist
        }

key = name.lower()
data[key] = newrecord

write_data(data, "records.json")
