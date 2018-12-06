
sequence = (1, 2, 3)

for value in sequence:
    print(value)

print("Now value is {}".format(value))
sequence = "Carter"

for character in sequence:
    print("The letter", character)

for number in range(7):
    if number % 2 == 0:
        print("{} squared is {}".format(number, number ** 2))
    
value = 0
while value < 10:
    print("Value = ", value)
    value = value + 1

while False:
    user_input = input("Input 'done' to quit this: ")
    if user_input == 'done':
        break

print("Ok!")

numberstring = ""
_max = 0

while True:
    user_input = input("Input an integer or input 'done' to quit this: ")
    if user_input == 'done':
        break
    
    try:
        user_input = int(user_input)
    except ValueError:
        print("Did not recognize that input")
        continue

    if user_input > _max:
        _max = user_input
    
    numberstring = numberstring + str(user_input)

print("The string we built is: ", numberstring)
print("The maximum value was: ", _max)

# or character in sequence: