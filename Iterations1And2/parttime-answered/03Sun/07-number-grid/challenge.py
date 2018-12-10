total = int(input("What number should I grid? "))


# step 1, find the factor of total that is closest to its square root
i = 1
factor = 1
while i * i <= total:
    if total % i == 0:
        factor = i
    i = i + 1

# step 2 determine the number of rows and number of columns
nrows = factor
ncols = total // nrows

# there will be #nrows rows, each with #ncols numbers in them

for row in range(0, nrows):
    for col in range(0, ncols):
        row_value = row * ncols
        value = row_value + col
        print("{:<4}".format(value), end="")
    print()