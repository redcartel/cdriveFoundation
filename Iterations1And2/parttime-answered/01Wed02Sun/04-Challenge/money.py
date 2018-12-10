
money = float(input("How much money do you have? "))
cents = int(100 * money)

hundreds = cents // (100 * 100)
cents = cents - 100 * 100 * hundreds
print("You have {} hundred dollar bills.".format(hundreds))

fifties = cents // (50 * 100)
cents = cents - 50 * 100 * fifties
print("You have {} fifty dollar bills.".format(fifties))

twenties = cents // (20 * 100)
cents = cents - 20 * 100 * twenties
print("You have {} twenty dollar bills.".format(twenties))

tens = cents // (10 * 100)
cents = cents - 10 * 100 * tens
print("You have {} ten dollar bills.".format(tens))

fives = cents // (5 * 100)
cents = cents - 5 * 100 * fives
print("You have {} five dollar bills.".format(fives))

ones = cents // 100
cents = cents - 100 * ones
print("You have {} one dollar bills.".format(ones))

quarters = cents // 25
cents = cents - 25 * quarters
print("You have {} quarters.".format(quarters))

dimes = cents // 10
cents = cents - 10 * dimes
print("You have {} dimes.".format(dimes))

nickels = cents // 5
cents = cents - 5 * nickels
print("You have {} nickels.".format(nickels))

pennies = cents
cents = cents - 1 * pennies
print("You have {} pennies.".format(pennies))

assert(cents == 0)