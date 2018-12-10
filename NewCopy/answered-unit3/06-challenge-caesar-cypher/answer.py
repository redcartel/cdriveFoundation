phrase = input("Enter a phrase to encrypt: ")
shift = int(input("Input the shift value: "))

VAL_a = ord('a')
VAL_z = ord('z')
VAL_A = ord('A')
VAL_Z = ord('Z')

output_message = []
newmessage = ""

for char in phrase:
    val = ord(char)
    if VAL_a <= val and val <= VAL_z:
        newval = (val - VAL_a + shift) % 26 + VAL_a
    elif VAL_A <= val and val <= VAL_Z:
        newval = (val - VAL_A + shift) % 26 + VAL_A
    else:
        newval = val
    output_message.append(chr(newval))
    newmessage = newmessage + chr(newval)

print("".join(output_message))
