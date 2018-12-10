
stringlist = []
while True:
    string = input("Input a string: ")
    if string == "done":
        break
    else:
        stringlist.append(string)

newlist = []
for i in stringlist:
    newlist.append(i.upper())

print(newlist)
