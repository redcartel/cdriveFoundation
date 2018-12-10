filename = "attendance.txt"

with open(filename, "w") as file_object:
    while True:
        name = input("Enter a name (input 'done' to exit): ")
        if name == "done":
            break
        print(name, file=file_object)