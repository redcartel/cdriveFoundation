filename = "mbox-short.txt"
matchline = "X-DSPAM-Confidence:"

def getfloats(filename):
    floats = []
    with open(filename, "r") as file_object:
        for line in file_object:
            if matchline in line:
                parts = line.split()
                if len(parts) == 2:
                    floats.append(float(parts[1]))
    return floats

if __name__ == "__main__":
    floats = getfloats(filename)
    _n = len(floats)
    _sum = 0.0
    for value in floats:
        _sum += value
    _average = _sum / _n

    print("Average: ", _average)