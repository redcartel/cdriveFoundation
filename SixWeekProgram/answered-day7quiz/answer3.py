
def wow(word):
    return "!{}!".format(word)

stringlist = ["one", "two", "three", "four", "five"]

newlist = []
for word in stringlist:
    newlist.append(wow(word))

print(newlist)
