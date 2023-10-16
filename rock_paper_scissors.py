import random

def RPS():
    user = input("Choice one: 'R' for Rock, 'P' for Paper,'S' for Scissors: ")
    computer = random.choice(['r','p','s'])

    # r > s, s > p, p > r
    if user == computer:
        return 'tie'

    if is_win(user,computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    #return True is player wins
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
        return True
    
print(RPS())