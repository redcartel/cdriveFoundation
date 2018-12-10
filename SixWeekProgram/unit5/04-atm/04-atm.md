## Exercise 4 - ATM

#### Time for something bigger

* You are going to make an ATM

* The user will be presented with a list of options

```
C - check balance

W - withdrawal

D - deposit

Q - quit

Input your choice: 
```

* They input the choice and then are shown their balance, given a prompt for how much to withdraw, or how much to deposit.

* Use a global variable to keep track of their balance. The balance should be 1000.0 when the program starts.

* If they try to withdraw more money than they have, they get an error and their balance does not change.

* The balance should update after each input. That is, if I withdraw 500.00 and then check my balance, it should reflect the new total.

* Break the design into several functions so you don't have one big hard-to-debug mess of code.

* Example:

```
C - check balance

W - withdrawal

D - deposit

Q - quit

Input your choice: C

You have $1000.00

C - check balance

W - withdrawal

D - deposit

Q - quit

Input your choice: W

How much would you like to withdraw?

Input your choice: 250.00

C - check balance

W - withdrawal

D - deposit

Q - quit

Input your choice: D

How much would you like to deposit?

Input your choice: 500.00

C - check balance

W - withdrawal

D - deposit

Q - quit

Input your choice: C

You have $1250.00

C - check balance

W - withdrawal

D - deposit

Q - quit

Input your choice: W

How much would you like to withdraw?

Input your choice: 2000.00

You do not have enough money.

C - check balance

W - withdrawal

D - deposit

Q - quit

Input your choice: Q

Goodbye
```
