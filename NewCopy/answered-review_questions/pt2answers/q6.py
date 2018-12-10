
file_object = open("thisis.txt", "r")

def transform(line):
    # capitalize all one or two letter words in line
    words = line.split()
    newwords = []
    for string in words:
        if len(string) <= 2:
            newwords.append(string.upper())
        else:
            newwords.append(string)
    outputline = " ".join(newwords)
    return outputline

for i in file_object:
    outputline = transform(i)
    print(outputline)

file_object.close()
