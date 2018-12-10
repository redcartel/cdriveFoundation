
file_object = open("thisis.txt", "r")

for i in file_object:
    print(i, end="")

file_object.close()
