number = int(input("Input an integer: "))

if number == 0:
    print("It is zero!")
else:
    print("It is not zero!")

if number < 10:
    print("Less than 10!")
elif number <= 20:
    print("Between 10 and 20")
else:
    print("Big number!")

if number >= 0:
    if number < 10 or number > 99:
        print("Not a two digit number!")
else:
    if number < -99 or number > -10:
        print("Not a two digit number!")

if number % 2 == 0:
    print("It is even!")

if number % 3 == 0:
    print("Divisible by three!")

if number % 4 == 0:
    print("Divisible by four!")

if number % 2 != 0 and number % 3 != 0 and number % 4 != 0:
    print("Not divisible by two, three, or four.")

if number % 7 != 0:
    number = number * 7
else:
    number = number // 7

print(number)
