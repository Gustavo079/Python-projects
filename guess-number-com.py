import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be  high b/c low = high
        feedback = input(f"is {guess} too high (H), too low(L), or correct(C)? ")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"yeah! The computer guessed the number, {guess}")

computer_guess(10)