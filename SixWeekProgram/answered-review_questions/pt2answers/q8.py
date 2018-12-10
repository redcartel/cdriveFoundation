
file_object = open("numbers.txt", "r")

for line in file_object:
    strings = line.split()
    sum = 0
    for string in strings:
        sum = sum + int(string)
    print(sum)

file_object.close()
