
name = input("What is your name? ")

if name.upper() == "Carter".upper():
    print("Hi Carter!")
    print("How's it going?")
    if name[0] == "C":
        print("Oh, we're being formal")
    else:
        print("What is going on?")
    print("OK")
elif name.upper() != "Carter" and name.upper() == "Greg".upper():
    print("Hi Greg")
elif name.upper() == "Kenso".upper():
    print("Hi Kenso")
elif name.upper() == "Carter".upper():
    print("Here we go again") # you won't see this
else:
    print("I don't know you")


print("Goodbye.")