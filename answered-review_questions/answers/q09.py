intlist = []
mysum = 0
while True:
    stringinput = input("Input an integer: ")
    if stringinput == "done":
        break
    else:
        intlist.append(int(stringinput))
print(sum(intlist))
