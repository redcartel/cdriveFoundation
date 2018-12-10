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

print(formatstring.format(hundreds, "hundred dollar bills"))
print(formatstring.format(fifties, "fifty dollar bills"))
print(formatstring.format(twenties, "twenty dollar bills"))
print(formatstring.format(tens, "ten dollar bills"))
print(formatstring.format(fives, "five dollar bills"))
print(formatstring.format(ones, "one dollar bills"))
print(formatstring.format(quarters, "quarters"))
print(formatstring.format(dimes, "dimes"))
print(formatstring.format(nickels, "nickels"))
print(formatstring.format(pennies, "pennies"))
