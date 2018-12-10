def takeattendance(prompt):
    attendancelist = []
    while True:
        inputvalue = input(prompt)
        if inputvalue == "done":
            break
        else:
            attendancelist.append(inputvalue)
    return attendancelist

def writefile(filename, namelist):
    with open(filename, 'w') as outputfile:
        for name in namelist:
            print(name, file=outputfile)

if __name__ == "__main__":
    attendancelist = takeattendance("Input a name: ")
    writefile("attendance.txt", attendancelist)