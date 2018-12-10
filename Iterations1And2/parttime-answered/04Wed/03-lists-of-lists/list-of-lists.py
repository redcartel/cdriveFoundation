rows = []
for rowindex in range(0,70,10):
    individual_row = []
    for columnindex in range(0,10):
        individual_row.append(rowindex + columnindex)
    rows.append(individual_row)

print("Length of rows: {}".format(len(rows)))
print("rows[2]: {}".format(rows[2]))
print()

for row in rows:
    for element in row:
        print("{:<3}".format(element), end="")
    print()

print()
print("fifth row, seventh column is {}".format(rows[4][6]))

# Answer:

for individual_row in rows[2:5]:
    for element in individual_row[3:8]:
        print("{:3}".format(element), end="")
    print()
