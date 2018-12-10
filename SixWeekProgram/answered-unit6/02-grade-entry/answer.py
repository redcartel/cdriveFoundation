
def prompt_values():
    firstname = input("First name: ")
    if firstname == "done":
        return False

    lastname = input("Last name: ")
    if lastname == "done":
        return False

    grade = input("Grade:")
    if grade == "done":
        return False

    valuetuple = (firstname, lastname, grade)
    return valuetuple


def outputline(valuetuple):
    line = "{} {} {}".format(valuetuple[0], valuetuple[1], valuetuple[2])
    return line


def mainloop(filename):
    file_object = open(filename, "w")

    values = True
    while values:
        values = prompt_values()

        if values:
            line = outputline(values)
            print(line, file=file_object)

    file_object.close()


mainloop("grades.txt")
