mylist = []

mylist.append(1)
mylist.append(2)
mylist.append(3)

print(len(mylist))

print(mylist[1])

counting = list(range(10))

print(len(counting))
print(counting[5])

lastnum = counting.pop()
print(lastnum)
print(counting)

counting.insert(2, 1000)
print(counting)

if 5 in counting:
    print("5 is in there.")

if 1001 in counting:
    print("1001 is in there.")

counting.append(-1)
counting.append(-2)
print(counting)
print(sorted(counting)) # sorted makes a sorted copy
print(counting) # leaves the original unchanged
counting.sort() # .sort() changes the list by sorting it
print(counting)

message = "Carter Adams"
letterlist = list(message)
print(letterlist.index("A")) # index gives the position of an element
del(letterlist[0])
print(letterlist)
letterlist.remove("A")
print(letterlist)
