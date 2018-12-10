print("Input words until you are done. Hit Enter by itself to quit.")
while True:
    word = input("Input a word: ")
    if len(word) == 0:
        break
    if len(word) < 4:
        print("That's a short word.")
    elif len(word) > 8:
        print("That's a long word.")
    else:
        print("That's a pretty average word.")
