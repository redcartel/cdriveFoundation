
inputstring = input("Give me an input string: ")

while len(inputstring) < 10:
    inputstring = input("Give me a longer string: ")

inputlist = list(inputstring)
print(inputlist)

print("Length of list: {}".format(len(inputlist)))

print("Sorted: ", sorted(inputlist))

inputlist.append("!")

print("Space occurs {} times.".format(inputlist.count(' ')))

print(inputlist[::2])

lastelement = inputlist.pop()

inputlist.insert(0, lastelement)

print(inputlist)

outputstring = "".join(inputlist)

print(outputstring)