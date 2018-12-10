year = int(input("Give me the number of a year: "))

if year < 1582:
    print("The Gregorian calendar was not implemented until 1582.")
    quit()

leap = False

if year % 400 == 0:
    leap = True
elif year % 100 == 0:
    leap = False
elif year % 4 == 0:
    leap = True
else:
    leap = False

if leap:
    print("{} is a leap year.".format(year))
else:
    print("{} is not a leap year.".format(year))