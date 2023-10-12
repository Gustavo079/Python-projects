import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 & {x}: "))
        if guess < random_number:
            print("sorry,to low. guess again")
        elif guess > random_number:
            print("sorry, to high. Guess again")
    print(f"Yeah, you guess the number {random_number}")

guess(10)