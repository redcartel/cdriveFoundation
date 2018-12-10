intlist = []
mysum = 0
while True:
    stringinput = input("Input a string: ")
    if stringinput == "done":
        break
    else:
        intlist.append(stringinput)
print(len(intlist))
