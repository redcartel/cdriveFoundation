# The program works, but I don't love it. I'd like to get it all on one logic line, somehow add the 400 year test
# to the line which currently has the 4 and 100 year test.
# Also it is prone to fail because it relies on the first if statement hitting true. An error could sneak by.

# Wrote a little function. I wanted to use it to print all these outputs and write the code once, but such is life. :D


input_year = int(input("What year would you like to test? "))


def leap_test(year):
    if year % 400 == 0:
        print(year, 'is a leap year!')
    elif (year % 4 == 0) and not(year % 100 == 0):
        print(year, 'is a leap year!')
    else:
        print(year, 'is not a leap year.')


leap_test(input_year)

for i in range(1880, 2021):
    if i % 400 == 0:
        print(i)
    elif i % 4 == 0 and not(i % 100 == 0):
        print(i)
