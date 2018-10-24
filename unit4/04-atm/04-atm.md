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

* They input the value and then are shown their balance, given a prompt for how much to withdraw, or how much to deposit. If they try to withdraw more money than they have, they get an error. Then they see the list of options again and it exits.

* The balance should begin at 1000.00 and update after each input. That is, if I withdraw 500.00 and then check my balance, it should reflect the new total.

* One of the challenges is going to be having each function know the value of the balance. There are a few ways to accomplish this, one of which is to use the ``` global ``` keyword with a variable defined outside of the function.

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
