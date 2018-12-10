n = int(input("number: "))

rows = 1
nrows = 0
while rows * rows <= n:
    if n % rows == 0:
        nrows = rows
    rows = rows + 1

ncols = n // nrows

for rnum in range(nrows):
    for cnum in range(ncols):
        rowstart = rnum * ncols
        print("{:<3}".format(rowstart + cnum), end="")
    print()