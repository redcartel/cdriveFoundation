value = int(input("Give me a positive integer: "))

for number in range(0,value+1,2):
    print(number)

number = 0

while number <= value:
    print(number)
    number = number + 2