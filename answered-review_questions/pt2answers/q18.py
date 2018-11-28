import json

file_object = open("example3.json", "r")
data = json.load(file_object)
file_object.close()

print("input 'done' to save and exit")
while True:
    name = input("Enter student name: ")
    if name == 'done':
        break
    studentid = input("Enter student ID: ")
    if studentid == 'done':
        break
    gpa = input("Enter student GPA (00.0 - 100.0): ")
    if gpa == 'done':
        break
    try:
        gpa = float(gpa)
    except ValueError:
        print("bad input")
        continue
    data[name] = {
            "studentID": studentid,
            "GPA": gpa
            }

file_object = open("example3.json", "w")
json.dump(data, file_object, indent=2)
file_object.close()
