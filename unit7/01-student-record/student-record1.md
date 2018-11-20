## Student records

* Copy this code to the top of a new python file:

```
lloyd = {
      "name": "Lloyd",
        "homework": [90.0,97.0,75.0,92.0],
          "quizzes": [88.0,40.0,94.0],
            "tests": [75.0,90.0]
}
alice = {
      "name": "Alice",
        "homework": [100.0, 92.0, 98.0, 100.0],
          "quizzes": [82.0, 83.0, 91.0],
            "tests": [89.0, 97.0]
}
tyler = {
      "name": "Tyler",
        "homework": [0.0, 87.0, 75.0, 22.0],
          "quizzes": [0.0, 75.0, 78.0],
            "tests": [100.0, 100.0]
}

students = ["lloyd", "alice", "tyler"]
```

* For each student in your students list, print out that student's data, as follows:

print the student's name

print the student's homework

print the student's quizzes

print the student's tests

* Write a function called ```get_average(student_name)``` that returns a students weighted average grade. The weights are 10% Homework, 30% Quizzes, and 60% Tests

* Write a function that converts a numerical grade between 00.0 and 100.0 to a letter grade. Follow the same rules as we did on the assignment from week 1.

* For each student add a "letter grade" key to their dictionary with the letter grade that corresponds to their weighted average.
