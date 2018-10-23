score = int(input("Input a grade between 0 and 100: "))

if score < 0 or score > 100:
    print("Grade must be between 0 and 100.")
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    if score == 100 or (grade != "F" and score % 10 == 9):
        grade = grade + "+"
    elif score >= 60 and score <= 90 and score % 10 == 0:
        grade = grade + "-"

    print("Your grade is a {}.".format(grade))
