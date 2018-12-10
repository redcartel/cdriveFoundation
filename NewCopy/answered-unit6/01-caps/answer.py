def terminal_answer(filename):
    file_object = open(filename, "r")
    for line in file_object:
        print(line.upper(), end="")
    file_object.close()

def file_answer(inputfile, outputfile):
    infile = open(inputfile, "r")
    outfile = open(outputfile, "w")
    for line in infile:
        print(line.upper(), end="", file=outfile)
    infile.close()
    outfile.close()

# terminal_answer("words.txt")

file_answer("words.txt", "output.txt")
