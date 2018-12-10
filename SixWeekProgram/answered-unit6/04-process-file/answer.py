def get_nums(filename, search_string):
    file_object = open(filename, "r")
    results = []
    for line in file_object:
        if search_string in line:
            words = line.split()
            number = float(words[-1])
            results.append(number)
    file_object.close()
    return results


def mysum(floatlist):
    total = 0.0
    for value in floatlist:
        total = total + value
    return total


floatlist = get_nums("mbox-short.txt", "X-DSPAM-Confidence:")
total = mysum(floatlist)
average = total / len(floatlist)

print("Total: {:.4f} Average: {:.4f}".format(total, average))
