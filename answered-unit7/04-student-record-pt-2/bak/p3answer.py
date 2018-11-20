import json

file_object = open("records.json", "r")
data = json.load(file_object)
file_object.close()

def avg(homework, quizzes, tests):
    hwavg = sum(homework) / len(homework)
    quizavg = sum(quizzes) / len(quizzes)
    testavg = sum(tests) / len(tests)
    return hwavg * .1 + quizavg * .3 + testavg * .6

for key in data:
    hwlist = data[key]["homework"]
    quizlist = data[key]["quizzes"]
    testlist = data[key]["tests"]
    name = data[key]["name"]
    average = avg(hwlist, quizlist, testlist)
    print("{}: {}%".format(name, average))
