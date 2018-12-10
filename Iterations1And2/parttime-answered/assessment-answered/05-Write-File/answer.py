grid = [
    [  0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
    [  1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
    [  2,  3,  4,  5,  6,  7,  8,  9, 10, 11],
    [  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
    [  4,  5,  6,  7,  8,  9, 10, 11, 12, 13],
    [  5,  6,  7,  8,  9, 10, 11, 12, 13, 14],
    [  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
    [  7,  8,  9, 10, 11, 12, 13, 14, 15, 16],
    [  8,  9, 10, 11, 12, 13, 14, 15, 16, 17],
    [  9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
]

with open("output.csv", "w") as file_object:
    for row in grid:
        line = []
        for element in row:
            line.append(str(element))
        file_object.write(",".join(line) + "\n")
        

## Save the numbers in a file called output.csv
## that looks like
## 0,1,2,3,4...
## 1,2,3,4,5...
## 2,3,4,5,6...
## ...