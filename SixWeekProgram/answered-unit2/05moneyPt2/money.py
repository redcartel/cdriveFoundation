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
formatstring = "You have {} {}."

if hundreds == 1:
    print(formatstring.format(hundreds, "hundred dollar bill"))
elif hundreds > 1:
    print(formatstring.format(hundreds, "hundred dollar bills"))

if fifties == 1:
    print(formatstring.format(fifties, "fifty dollar bill"))
elif fifties > 1:
    print(formatstring.format(fifties, "fifty dollar bills"))

if twenties == 1:
    print(formatstring.format(twenties, "twenty dollar bill"))
elif twenties > 1:
    print(formatstring.format(twenties, "twenty dollar bills"))

if tens == 1:
    print(formatstring.format(tens, "ten dollar bill"))
elif tens > 1:
    print(formatstring.format(tens, "ten dollar bills"))

if fives == 1:
    print(formatstring.format(fives, "five dollar bill"))
elif fives > 1:
    print(formatstring.format(fives, "five dollar bills"))

if ones == 1:
    print(formatstring.format(ones, "one dollar bill"))
elif ones > 1:
    print(formatstring.format(ones, "one dollar bills"))
    
if quarters == 1:
    print(formatstring.format(quarters, "quarter"))
elif quarters > 1:
    print(formatstring.format(quarters, "quarters"))

if dimes == 1:
    print(formatstring.format(dimes, "dime"))
elif dimes > 1:
    print(formatstring.format(dimes, "dimes"))

if nickels == 1:
    print(formatstring.format(nickels, "nickel"))
elif nickels > 1:
    print(formatstring.format(nickels, "nickels"))

if pennies == 1:
    print(formatstring.format(pennies, "penny"))
elif pennies > 1:
    print(formatstring.format(pennies, "pennies"))
