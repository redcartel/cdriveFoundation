
userinput = None
while userinput == None or userinput != "done":
    userinput = input("Input a number or 'done' to quit: ")
    if userinput != "done":
        try:
            number = int(userinput)
            if number % 2 == 0:
                print("{} is even.".format(number))
            else:
                print("{} is odd.".format(number))
        except ValueError:
            print("Please input an integer or 'done.'")
