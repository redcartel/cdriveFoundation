## Day 9 Quiz

#### Answer 3 of the following 5 questions:

* Use the following code:

```
dictionary = {
    "carter" : {
        "student-id" : 1,
        "gpa" : 2.8
    },
    "greg" : {
        "student-id" : 2,
        "gpa" : 3.3
    },
    "kenso" : {
        "student-id" : 3,
        "gpa" : 3.7
    }
}
```

Use a loop to print out each student's name, id, and gpa on one line.

```
carter, 1, 2.8
greg, 2, 3.3
kenso, 3, 3.7
```

* Starting with the code from problem #1, modify carter's gpa to be 2.5, then add a new student, kai, with a student id of 4 and a gpa of 3.9

* Starting with the code from problem #1, save the dictionary to a file call dictionary.json.

* Write a function that takes a dictionary like the one in problem #1 as its first argument, and a name as its second argument. It should return the student-id if the student exists or None if the student does not.

```
print(get_id(dictionary, "carter"))
# prints "1"

print(get_id(dictionary, "nikil"))
# prints "None"
```

* Load a dictionary from the provided example.json, and print the number of keys in that dictionary. ( len(dictionary) = number of keys in that dictionary)
