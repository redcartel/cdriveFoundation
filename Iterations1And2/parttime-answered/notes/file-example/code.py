
filename = "sonnet.txt"

with open("output.txt", "w") as file_object:
    while True:
        line = input("enter a line of text: ")
        if line == 'done':
            break
        print(line, file=file_object)

# to read
with open("sonnet.txt", "r") as file_object:
    for line in file_object:
        print(line, end="")