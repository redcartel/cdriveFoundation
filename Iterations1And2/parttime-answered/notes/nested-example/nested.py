import pprint

array = []

for row in range(10):
    rowlist = []
    for column in range(10):
        rowlist.append(row * 10 + column)
    array.append(rowlist)

for row in range(10):
    for column in range(10):
        print("{:<3}".format(array[row][column]), end="")
    print()

with open("output.txt", "w") as output_file:
    for row in range(7):
        for column in range(5):
            print("{:<3}".format(row * 5 + column), end="", file=output_file)
        print(file=output_file)

with open("output.txt", "r") as input_file:
    for line in input_file:
        string_values = line.strip().split()
        for string_number in string_values:
            number = int(string_number)
            print("{:<3}".format(number * 2), end="")
        print()