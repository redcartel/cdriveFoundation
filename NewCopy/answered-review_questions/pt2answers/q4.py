file_object = open("output.txt", "r")
output_list = []

for line in file_object:
    output_list.append(line[0:-1])

print(output_list)
file_object.close()
