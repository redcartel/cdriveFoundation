
def stringlist(mylist):
    newlist = []
    for i in mylist:
        newlist.append(str(i))
    return newlist

sequence = list(range(20))
print(sequence)
print(", ".join(stringlist(sequence)))
