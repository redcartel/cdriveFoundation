
file_object = open("numbers.txt", "r")
file_object_output = open("numbers2.txt", "w")

for line in file_object:
    print(line, file = file_object_output, end="")

file_object.close()
file_object_output.close()
