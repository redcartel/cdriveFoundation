
file_object = open("thisis.txt", "r")

newlist = []
secondlist = []
for i in file_object:
    secondlist += i.split()

# another way of doing it:
for i in file_object:
    for word in i.split():
        newlist.append(word)

print(secondlist)

file_object.close()
