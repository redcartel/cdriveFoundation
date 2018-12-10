
value = int(input("Enter an integer value: "))

if value == 0:
    print("It is zero!")
else:
    print("It's not zero!")

if value < 10:
    print("Less than 10!")
elif value < 20:
    print("Less than 20!")
else:
    print("Big number you got there!")

if 10 <= value and value <= 100:
    print("Two digits!")

# This also works:
# if 10 <= value <= 100:
#   print("Two digits!")

if value % 5 == 0:
    print("It is divisible by 5!")

if value % 13 == 0 or value % 17 == 0:
    print("Cicadas!")

if value % 2 == 0 and value % 9 == 0:
    print("Even and divisible by 9!")

if value % 7 != 0:
    value = value * 7
else:
    value = value / 7

print("The new number is {} now.".format(value))