
file_object = open("sonnet.txt", "r")

total = 0
for line in file_object:
    total = total + len(line.split())

print(total)
