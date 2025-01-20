from random import randint

number = randint(1, 10)
attempts = 0

print("Choose a number between 1 and 10")

while attempts !=3:
    guess = int(input("Enter a number: "))
    
    if guess > number:
        print("Wrong, the number is too low")
        attempts +=1
    elif guess < number:
        print("Wrong, the number is too high")
        attempts +=1
    else:
        print(f"YESSIR, correct number: {number}")
        exit()