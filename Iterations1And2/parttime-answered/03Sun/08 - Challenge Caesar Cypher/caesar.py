a = ord("a")
A = ord("A")
z = ord("z")
Z = ord("Z")

message = input("Give me the message to encrypt:\n")
shift = int(input("Give me the shift distance: "))

output = ""
for letter in message:
    ordinal = ord(letter)
    if a <= ordinal <= z:
        neword = (ordinal - a + shift) % 26 + a
    elif A <= ordinal <= Z:
        neword = (ordinal - A + shift) % 26 + A
    else:
        neword = ordinal
    output = output + chr(neword)

print("\nThe coded message is:\n{}".format(output))