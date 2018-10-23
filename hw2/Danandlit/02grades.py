# The user gives their grade between 0-100, which is converted to an integer
# I used a trick that isn't super readable, but I wanted to see if I could do it
# grades_possible string with all the possible string outputs e.g. "an A+" or "a C-"
# I used the value of the input to determine an index in the string
# I passed the index through the grades_possible string and inputted the value into the final printed string.



grade = int(input("What did you get on the test? "))


while not (0 <= grade <= 100):
    print('That is not a legitimate grade!')
    grade = int(input("What did you get on the test? "))



# Determine index for later string
if grade == 100:
    index = 0

if 91 <= grade <= 99:
    index = 1

if grade == 90:
    index = 2

if grade == 89:
    index = 3

if 81 <= grade <= 88:
    index = 4

if grade == 80:
    index = 5

if grade == 79:
    index = 6

if 71 <= grade <= 78:
    index = 7

if grade == 70:
    index = 8

if grade == 69:
    index = 9

if 61 <= grade <= 68:
    index = 10

if grade == 60:
    index = 11

if 0 <= grade <= 59:
    index = 12

grades_possible = ['an A+', 'an A', 'an A-', 'a B+', 'a B', 'a B-', 'a C+', 'a C', 'a C-', 'a D+', 'a D', 'a D-', 'an F']



print('Your grade is {}!'.format(grades_possible[index]))
