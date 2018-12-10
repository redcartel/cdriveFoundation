
inputstring = ""
while len(inputstring) < 10:
    inputstring = input("Please enter a string that is at least 10 characters long")

alist = list(inputstring)

print(alist)

print(len(alist))

print(sorted(alist))

alist.append('!')

print(alist.count(' '))

# or if you don't know about count:

total = 0
for char in alist:
    if char == ' ':
        total = total + 1

print(total)

print(alist[::2])

lastelement = alist.pop()

print(alist)

alist.insert(0, lastelement)

print(alist)
