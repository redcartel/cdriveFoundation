# answer to the third question

import json

try:
    file_object = open('records.json', 'r')
    data = json.load(file_object)
    file_object.close()
except FileNotFoundError:
    data = {}

def get_average(student_name, data):
    homework_list = data[student_name]["homework"]
    quizzes_list = data[student_name]["quizzes"]
    tests_list = data[student_name]["tests"]
    hwavg = sum(homework_list) / len(homework_list)
    quizavg = sum(quizzes_list) / len(quizzes_list)
    testavg = sum(tests_list) / len(tests_list)

    total = 0.1 * hwavg + 0.3 * quizavg + 0.6 * testavg
    return total

def letter_grade(score):
    if score >= 90.0:
        return "A"
    elif score >= 80.0:
        return "B"
    elif score >= 70.0:
        return "C"
    elif score >= 60.0:
        return "D"
    else:
        return "F"

for key in data:
    avg = get_average(key, data)
    letter = letter_grade(avg)
    print("{:<15} : {}, {:.2f}".format(key, letter, avg))
