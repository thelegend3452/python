import random

def roll_dice():
    return random.randint(1, 6)

print("Rolling dice..")
print(f"Rolled dice is {roll_dice()}")