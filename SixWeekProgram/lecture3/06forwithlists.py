# pattern to build a list of objects converted into strings:

numberstrings = []
for i in range(12):
    numberstrings.append(str(i))

# use join to work with lists of strings. only works if all the elements are strings:

print(", ".join(numberstrings))

numbers = list(range(5))

for number in numbers:
    print("{} squared is {}".format(number, number * number))
