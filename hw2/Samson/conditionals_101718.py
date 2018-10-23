value = input()
value = int(value)
if value == 0:
    print("It is zero!")
if value != 0:
    print("It's not zero!")

if value <= 10:
    print("Less than 10!")
    print("Not a two digit number")
elif value >=10 and value <=20:
    print("Between 10 and 20")
elif value >=20:
    print("Big number!")

if value % 2 ==  0:
    print("It is even!")

if value % 3 == 0:
    print("Divisible by three!")

if value % 4 == 0:
    print("Divisible by four!")

elif value % 2 != 0 and value % 3 !=0 and value % 4 != 0:
    print("Not divisible by two, three, or four.")

if value % 7 != 0:
    print(str(int(value) * 7))

if value % 7 == 0:
    print(str(int(value) / 7))
