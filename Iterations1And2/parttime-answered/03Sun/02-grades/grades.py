
grade = float(input("What is your grade (between 0.0 and 1.0? "))
gradeletter = None

if grade < 0.0 or grade > 1.0:
    print("Grade out of range")
    quit()

if grade >= .9:
    gradeletter = "A"
elif grade >= .8:
    gradeletter = "B"
elif grade >= .7:
    gradeletter = "C"
elif grade >= .6:
    gradeletter = "D"
else:
    gradeletter = "F"

if gradeletter == "A" or gradeletter == "F":
    print("You earned an {}.".format(gradeletter))
else:
    print("You earned a {}.".format(gradeletter))