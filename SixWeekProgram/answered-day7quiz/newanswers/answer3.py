
def processlist(stringlist):
# apply a transformation to each element of
# stringlist and return the new list
    newlist = []
    for string in stringlist:
        newlist.append(emphasize(string))
    return newlist

def emphasize(string):
# put a '!' on each side of a string and return
# the new string
    newword = "!"+string+"!"
    return newword


stringlist = ["one", "two", "three", "four", "five"]
print(processlist(stringlist))

# print(emphasize("Byte Academy"))
