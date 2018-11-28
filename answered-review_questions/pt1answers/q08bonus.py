import random

possibilities = ["rock", "paper", "scissors"]
index = random.randint(0,2)
cpu_choice = possibilities[index]

choice = input("rock, paper, or scissors? ")

if choice not in ["rock", "paper", "scissors"]:
    print("bad input")
elif choice == cpu_choice:
    print("it's a tie.")
elif (choice == "rock" and cpu_choice == "scissors") or (choice == "scissors" and cpu_choice == "paper") or (choice == "paper" and cpu_choice == "rock"):
    print("user wins!")
else:
    print("computer wins!")
print("cpu picked", cpu_choice)
