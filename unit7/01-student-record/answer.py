import pprint

lloyd = {
      "name": "Lloyd",
        "homework": [90.0,97.0,75.0,92.0],
          "quizzes": [88.0,40.0,94.0],
            "tests": [75.0,90.0]
}
alice = {
      "name": "Alice",
        "homework": [100.0, 92.0, 98.0, 100.0],
          "quizzes": [82.0, 83.0, 91.0],
            "tests": [89.0, 97.0]
}
tyler = { 
    "name": "Tyler", 
    "homework": [0.0, 87.0, 75.0, 22.0],    
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

records = {}
records["lloyd"] = lloyd
records["alice"] = alice
records["tyler"] = tyler

#pprint.pprint(records)

for key in records:
    print("Name:", records[key]["name"])
    print("HW Grades:", records[key]["homework"])
    print("Quizzes Grades:", records[key]["quizzes"])
    print("Tests Grades:", records[key]["tests"])
    print()


def get_mean(numberlist):
    total = sum(numberlist)
    return total / len(numberlist)


def get_average(student_name):
    record = records.get(student_name)
    if record == None:
        return None
    homework = record["homework"]
    quizzes = record["quizzes"]
    tests = record["tests"]

    homeworkavg = get_mean(homework)
    quizzesavg = get_mean(quizzes)
    testsavg = get_mean(tests)

    total = 0.0
    total = total + .1 * homeworkavg
    total = total + .3 * quizzesavg
    total = total + .6 * testsavg

    return total


def letter_grade(number_grade):
    if number_grade < 60.0:
        return "F"
    if number_grade < 70.0:
        return "D"
    if number_grade < 80.0:
        return "C"
    if number_grade < 90.0:
        return "B"
    return "A"

for key in records:
    # letter grade for this student is:
    numerical_average = get_average(key)
    letter = letter_grade(numerical_average)
    records[key]["letter grade"] = letter

pprint.pprint(records)
