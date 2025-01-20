import random

choices = ["rock", "paper", "scissors"]
computer = random.choices(choices)

player = input("Choose ROCK, PAPER OR SCISSORS: ")

if player == computer:
    print("Tie")
elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
    print("you won")
else: 
    print(f"You lost, Computer won. Compute chose {computer}")
