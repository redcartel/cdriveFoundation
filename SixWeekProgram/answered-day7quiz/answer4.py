
file_object = open("sonnet.txt")

total = 0
for line in file_object:
    n = len(line.split())
    total = total + n

print(total, "words in the file")
