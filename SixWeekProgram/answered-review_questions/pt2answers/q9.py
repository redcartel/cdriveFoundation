
file_object = open("numbers.txt", "r")

numbers = []
for line in file_object:
    numbers.append(line)

file_object.close()

numbers.reverse()

for line in numbers:
    print(line, end="")
