
import json

try:
    file_object = open('records.json', 'r')
    data = json.load(file_object)
    file_object.close()
except FileNotFoundError:
    data = {}

firstname = input("Input name: ")
print("separate multiple grades by spaces")
hwgrades = input("Input homework grades: ")
quizgrades = input("Input quiz grades: ")
testgrades = input("Input test grades: ")

key = firstname.lower()

def getscores(scorestring):
    stringlist = scorestring.split()
    result = []
    for i in stringlist:
        result.append(float(i))
    return result


data[key] = {
        "Name" : firstname,
        "homework" : getscores(hwgrades),
        "tests" : getscores(testgrades),
        "quizzes" : getscores(quizgrades)
}

file_object = open('records.json', 'w')
json.dump(data, file_object, indent=2)
file_object.close()
