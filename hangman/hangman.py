import random 
import string
from words import words

def get_word(words):
    word = random.choice(words) #computer chooses somthing from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed 

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letter used
        print("you have used these letters: ", " ".join(used_letters))

        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 #takes away a life if wrong
                print("Letter is not in the word.You have", lives, "lives")

        elif user_letter in used_letters:
            print("you have already used that character.please try again.")
        
        else:
            print("Invalid character. please try again.")
    #gets here when len(words_letters) == 0 or when lives == 0
    if lives == 0:
        print("You die, The word was: ",word)
    else:
        print("You guessed the word:", word, "!!")

hangman()