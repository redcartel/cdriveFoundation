# Gather input as string
total_str = input('How much money do you have? ')

# If first character is $, remove the $, a convert to a float.
# If first character is not a $, just convert to a float.
if total_str[0] == '$':
    total = float(total_str.replace('$', ''))
else:
    total = float(total_str)

# Create a variable for a whole number of bills by taking the decimal places off.
total_bills = int(total)

# Get a whole value for number of cents.
total_cents = int(round((total % 1) * 100, 2))

print('Easy! You need: ')

# Isolate the number of hundreds and the remainder value
hundreds = total_bills // 100
hundreds_remain = total_bills % 100

# Repeat the process with fifties, twenties and so on
fifties = hundreds_remain // 50
fifties_remain = hundreds_remain % 50

twenties = fifties_remain // 20
twenties_remain = fifties_remain % 20

tens = twenties_remain // 10
tens_remain = twenties_remain % 10

fives = tens_remain // 5
fives_remain = tens_remain % 5

ones = fives_remain // 1

# These blocks of if / else statements determine if a singular, plural, or no units need to be printed for a given value
if hundreds == 1:
    print(str(hundreds) + ' benjamin')
elif hundreds >= 2:
    print(str(hundreds) + ' benjamins')
elif hundreds == 0:
    pass

if fifties == 1:
    print(str(fifties) + ' fifty')
elif fifties == 0:
    pass

if twenties == 1:
    print(str(twenties) + ' twenty')
elif twenties >= 2:
    print(str(twenties) + ' twenties')
elif twenties == 0:
    pass

if tens == 1:
    print(str(tens) + ' ten')
elif tens == 0:
    pass

if fives == 1:
    print(str(fives) + ' five')
elif fives == 0:
    pass

if ones == 1:
    print(str(ones) + ' one')
elif ones >= 2:
    print(str(ones) + ' ones')
elif ones == 0:
    pass

# The isolation and remainder process repeats for cents--remember, starting with a positive integer
quarters = total_cents // 25
quarters_remain = total_cents % 25

dimes = quarters_remain // 10
dimes_remain = quarters_remain % 10

nickels = dimes_remain // 5
nickels_remain = dimes_remain % 5

pennies = nickels_remain // 1

# The printing repeats with accurate plurals and omissions depending on the value
if quarters == 1:
    print(str(quarters) + ' quarter')
elif quarters >= 2:
    print(str(quarters) + ' quarters')
elif quarters == 0:
    pass

if dimes == 1:
    print(str(dimes) + ' dime')
elif dimes >= 2:
    print(str(dimes) + ' dimes')
elif dimes == 0:
    pass

if nickels == 1:
    print(str(nickels) + ' nickel')
elif nickels == 0:
    pass

if pennies == 1:
    print(str(pennies) + ' penny')
elif pennies >= 2:
    print(str(pennies) + ' pennies')
elif pennies == 0:
    pass
