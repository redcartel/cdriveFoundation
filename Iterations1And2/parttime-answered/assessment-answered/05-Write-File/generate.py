from random import randint

print("grid = [")
for i in range(10):
    print("    [", end='')
    intlist = []
    for j in range(10):
        intlist.append(j+i)
    print(",".join(["{:>3}".format(str(num)) for num in intlist]), end="")
    print("],")
print("]")