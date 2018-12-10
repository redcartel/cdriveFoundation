
def caps(filename):
    with open(filename, 'r') as file_object:
        for line in file_object:
            print(line.upper(), end="")


if __name__ == "__main__":
    caps("words.txt")