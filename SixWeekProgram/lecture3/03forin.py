# traverse sequences with a for in loop

for i in range(10):
    print("i = {}".format(i))

message = "Now is the time for all good men to come to the aid of their country."

for letter in message:
    print("{}, ".format(letter), end="")
print()

for value in (5, 7, -1, 10, 20):
    print(value)

for i in range(1,20):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

vowels = "AEIOUaeiou"
for letter in message:
    if letter not in vowels:
        print(letter, end="")
print()
