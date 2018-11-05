from random import randint

numberlist = []

for i in range(10):
    numberlist.append(randint(0,99))

print(numberlist)

total = 0
for whatever in numberlist:
    total = total + whatever

print("Sum: ", total)

newlist = []
for number in numberlist:
    newlist.append(number * 2)

print(newlist)

for number in numberlist:
    if number > 40:
        print(number)

strlist = []

for number in numberlist:
    strlist.append(str(number))

outputstring = ", ".join(strlist)

print(outputstring)
