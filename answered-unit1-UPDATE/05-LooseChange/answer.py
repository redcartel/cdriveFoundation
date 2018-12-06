value = input("How much change do you have? ")
cents = int(float(value) * 100)

hundreds = cents // (100 * 100)
cents = cents - hundreds * (100 * 100)

fifties = cents // (50 * 100)
cents = cents - fifties * (50 * 100)

twenties = cents // (20 * 100)
cents = cents - twenties * (20 * 100)

tens = cents // (10 * 100)
cents = cents - tens * (10 * 100)

fives = cents // (5 * 100)
cents = cents - fives * (5 * 100)

ones = cents // (1 * 100)
cents = cents - ones * (1 * 100)

quarters = cents // 25
cents = cents - quarters * 25

dimes = cents // 10
cents = cents - dimes * 10

nickels = cents // 5
cents = cents - nickels * 5

pennies = cents

formatstring = "You have {} {}{}."

endings = ("s", "", "s", "s", "s", "s", "s", "s", "s", "s")
penny_endings = ("ies", "y", "ies", "ies", "ies", "ies", "ies", "ies", "ies")
print(formatstring.format(hundreds, "hundred dollar bill", endings[hundreds]))
print(formatstring.format(fifties, "fifty dollar bill", endings[fifties]))
print(formatstring.format(twenties, "twenty dollar bill", endings[twenties]))
print(formatstring.format(tens, "ten dollar bill", endings[tens]))
print(formatstring.format(fives, "five dollar bill", endings[fives]))
print(formatstring.format(ones, "one dollar bill", endings[ones]))
print(formatstring.format(quarters, "quarter", endings[quarters]))
print(formatstring.format(dimes, "dime", endings[dimes]))
print(formatstring.format(nickels, "nickel", endings[nickels]))
print(formatstring.format(pennies, "penn", penny_endings[pennies]))
