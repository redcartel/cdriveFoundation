
def insert(number, thelist):
    if number < thelist[0]:
        return
    thelist[0] = number
    i = 1
    while i < len(thelist) and number > thelist[i]:
        thelist[i-1], thelist[i] = thelist[i], number

if __name__ == "__main__":
    testlist = [0, 0, 0, 0, 0]
    while True:
        print("Current list: ", testlist)
        theinput = input("Input an integer, 'done' to exit: ")
        if theinput == 'done':
            break
        try:
            number = int(theinput)
        except ValueError:
            continue
        insert(theinput, testlist)