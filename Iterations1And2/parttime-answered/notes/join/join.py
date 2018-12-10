
numbers = [0, 1, 2, 3, 4, 5]

substrings = []
for number in numbers:
    substrings.append(str(number))

substrings = [str(value) for value in numbers if value % 2 == 0]

output = " {(* wow *)} ".join(substrings)

print(output)