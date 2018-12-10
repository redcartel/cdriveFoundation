
for row_start in range(0,100,10):
    for column in range(10):
        print("{} ".format(row_start + column), end="")
    print()

print()
print()

for value in range(100):
    print("{} ".format(value), end="")
    if value % 10 == 9:
        print()
