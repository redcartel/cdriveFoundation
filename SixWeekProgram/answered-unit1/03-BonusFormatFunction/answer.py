
first = 3
second = "little pigs"
print("The {} {}".format(first, second))

amount = 6.7
print("{:.3f}".format(amount))

name1 = "Nikil"
name2 = "Josephine"
formatstring = "Look at [{:<15}] now."
print(formatstring.format(name1))
print(formatstring.format(name2))

formatstring2 = "Look at [{:>15}] now."
print(formatstring2.format(name1))
print(formatstring2.format(name2))
