name = input("What is your name? ")

if name == "Alice":
    print("Hello, Alice.")

elif name == "Kenso":
    print("Hello, Kenso")

elif name == "Carter":
    print("Hello, Carter")
    print("How is class going today?")

else:
    print("I do not recognize you.")

print("Enough about names.")

number = int(input("Tell me a number: "))

if number < 0:
    print("It is a negative number!")

elif number < 10:
    print("It is a one digit number!")

elif number % 2 == 0 and number > 100:
    print("It is a big even number!")

else:
    print("Nothing special about that number.")
