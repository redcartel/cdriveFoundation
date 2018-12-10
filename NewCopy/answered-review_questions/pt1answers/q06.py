
message = input("Enter a message: ")
number = int(input("Enter an int: "))
# number = int(number) would have worked

print(message * number)

for i in range(number):
    print(message, end="")
print()
