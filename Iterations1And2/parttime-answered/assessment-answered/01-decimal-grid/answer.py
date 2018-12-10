from random import uniform

for r in range(0, 5):
    for c in range(10, 60, 10):
        num = uniform(0.0, 20.0)
        print("{:6.3f} ".format(num), end="")
    print()