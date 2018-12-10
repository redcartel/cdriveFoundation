## Foundation Assessment, Pt. 2

Answer 3 of the following questions

To exempt Byte Academy entrace requirements, you must answer the final two questions.

* Input a string from the user. Break the string into words and then print each word contained in angle braces (<>).

```
Input a string: Some data for the question

<Some>
<data>
<for>
<the>
<question>
```

* Write the three following functions:

A function that returns every other element of a list.

A function that takes a string as an argument returns a new string that is that string repeated 3 times.

A function that takes a list of numbers and returns a list of those numbers turned into strings.

```
# everyother([1,2,3,4,5]) returns [1,3,5])

# repeat3('Value') returns 'ValueValueValue'

# stringify([1,2,3,4]) returns ['1', '2', '3', '4']
```


* Use the following code:
```
d = {
    'Carter': 'value',
    'Greg': ['list', 'value'],
    'Kenso': 'VALUE'
}
```
Add the key 'Nikhil' with the value 'another value' to the dictionary.

Print the value of 'Carter'

Print the second element of the value of 'Greg'

Write an if statement that tests if the dictionary has a key called 'Kai'

* Use the following code:
```
A = ord('A')
dic = {}
for code in range(A, A+26):
    letter = chr(code)
    dic[letter] = code
```

print each key in dic followed by its value. The order of the keys does not matter

*For exemption only:* Print the key, value pairs with the keys in alphabetical order.

```
F 70
G 71
I 73
M 77
J 74
E 69
C 67
Y 89
...
```

* Write a function that takes a string as its argument and returns a string that is the first two letters of the argument string.

```
# firsttwo('Test') returns 'Te'
```

Use while and input to input strings from the user until the user types 'done.' 

Create a list that is your function applied to each input.

Print out each element of that list on its own line.
```
Input a string, 'done' to quit: Carter
Input a string, 'done' to quit: Greg
Input a string, 'done' to quit: Kenso
Input a string, 'done' to quit: Nikhil
Input a string, 'done' to quit: done

Ca
Gr
Ke
Ni
```

