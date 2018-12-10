
count = 0
while True:
    name = input("Give me a name: ")
    if name == "done":
        break
    names = name.strip().split()
    if len(names) == 2 and len(names[0]) >= 4:
        count += 1

print(count, "names pass the test.")