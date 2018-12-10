
n = input("Give me an integer: ")
n = int(n)

print("with a while loop:\n")

val = 0
while val < n:
    print(val)
    val = val + 2

print("\nwith a for loop:\n")

for val2 in range(0,n,2):
    print(val2)
