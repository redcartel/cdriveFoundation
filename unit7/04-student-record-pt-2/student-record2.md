# Student Record Part 2

* You will be building a dictionary and json file (called records.json) that looks like:
```
{
    "studentname" : {
        "Name" : "Firstname",
        "homework" : [90.0, 80.5, 79.9],
        "tests" : [77.0, 33.0, 87.5],
        "quizzes" : [78.0, 99.5, 65.8]
    },
    
    "studentname2" : {
        "Name" : "Anotherfirstname",
        ...

```

* When your program starts, open records.json if it exists, and load its dictionary into a dictionary called records. If the file doesn't exist, create an empty dictionary for records.

* Now prompt the user for a student's records.

* Ask for their first name

* Ask for homework grades, which can be any number of floats separated by spaces

* Ask for quiz grades, which can be any number of spaces

* Ask for test grades, which can be any number of spaces

* Then add a new key, the students name converted to lowercase, to records and its value should be a dictionary with "Name", "homework", "tests", and "quizzes" values. The grade input should be lists of floating point values.

* Now write records to records.json
