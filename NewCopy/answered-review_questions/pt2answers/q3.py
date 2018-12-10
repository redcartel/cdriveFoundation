file_object = open("output.txt", "w")

while True:
    value = input("Enter a line of text: ")
    if value == 'done':
        break
    else:
        print(value, file=file_object)

file_object.close()
