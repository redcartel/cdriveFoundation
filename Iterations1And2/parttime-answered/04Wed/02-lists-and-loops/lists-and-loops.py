from random import randint

numberlist = []

for i in range(10):
    numberlist.append(randint(0,99))

print(numberlist)

stringlist = []

_sum = 0
for num in numberlist:
    _sum = _sum + num

print(_sum)

doublelist = []
for num in numberlist:
    doublelist.append(num * 2)

print(doublelist)

for num in numberlist:
    if num > 40:
        print num

stringlist = []

for num in numberlist:
    stringlist.append(str(num))

numberstring = ", ".join(stringlist)

stringlist = [str(num) for num in numberlist]