import pprint

data = {
        "lloyd" : {
          "name": "Lloyd",
            "homework": [90.0,97.0,75.0,92.0],
              "quizzes": [88.0,40.0,94.0],
                "tests": [75.0,90.0]
    },
        "alice" : {
          "name": "Alice",
            "homework": [100.0, 92.0, 98.0, 100.0],
              "quizzes": [82.0, 83.0, 91.0],
                "tests": [89.0, 97.0]
    },
        "tyler" : {
          "name": "Tyler",
            "homework": [0.0, 87.0, 75.0, 22.0],
              "quizzes": [0.0, 75.0, 78.0],
                "tests": [100.0, 100.0]
    }
}

for key in data:
    subdict = data[key]
    keys = ["name", "homework", "quizzes", "tests"]
    for key2 in keys:
        print(subdict[key2])

def get_average(student_name):
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
    subdict = data[key]
    average = get_average(key)
    grade = letter_grade(average)
    subdict["letter grade"] = grade

pprint.pprint(data)
