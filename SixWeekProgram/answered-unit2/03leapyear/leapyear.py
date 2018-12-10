print("Input a year, or input \"all\" for all years between 1880 and 2020")
year = input(": ")

if year != "all":
    year = int(year)
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        print("{} is a leap year.".format(year))
    else:
        print("{} is not a leap year.".format(year))

else:
    year = 1880
    while year <= 2020:
        if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
            print("{} is a leap year.".format(year))

        year = year + 1
