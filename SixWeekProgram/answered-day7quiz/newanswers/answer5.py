num = []
output_file = open("output.txt", "w")
for number in range(10,21):
    print(number, file=output_file)
output_file.close()

# file_object = open("example.txt", "w")
# print("first", file=file_object)
# print("second", file=file_object)
# print("third", file=file_object)
# file_object.close()
