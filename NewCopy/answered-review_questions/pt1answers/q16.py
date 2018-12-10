
def stringlist(mylist):
    newlist = []
    for i in mylist:
        newlist.append(str(i))
    return newlist

print(stringlist([1, True, (1, 2), None]))

print(", ".join(stringlist([1, 2, 3, 4, 5])))
