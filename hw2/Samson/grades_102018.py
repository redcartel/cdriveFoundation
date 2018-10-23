number = input()
number = int(number)

if number < 0: 
    print("Not a legitimate grade")

if number > 100:
    print("Not a legitimate grade")

elif number >= 91 and number < 99:
    print("Your grade is a A")
    
if number >= 99:
    print("Your grade is a A+")

if number == 90:
    print("Your grade is a A-")
    
elif number >= 81 and number <= 88:
    print("Your grade is a B")

if number == 89:
    print("Your grade is a B+")

if number == 80:
    print("Your grade is a B-")
    
elif number >= 71 and number <= 78:
    print("Your grade is a C")

if number == 79:
    print("Your grade is a C+")

if number == 70:
    print("Your grade is a C-")

elif number >= 61 and number <= 68:
    print("Your grade is a D")

if number == 69:
    print("Your grade is a D+")

if number == 60:
    print("Your grade is a D-")

if number < 60:
    print("Your grade is a F")
