import random
from words import words_list

# 1. Display menu

def game_menu():
    """
    Choices for user to start, choose difficulty & and view the rules of the game
    """
print("Choose 1 to play game")
print("Choose 2 to choose game difficulty")
print("Choose 3 to read game rules")
choices = False
while not choices:
    options = input("/n ")
    if options == "1":
        choices = True
        difficulty = "default"
        return difficulty

    elif options == "2":
        choices = True

    elif options == "3":
        choices = True

    else: print("Please choose 1, 2 or 3 to continue")

# 2. handle choice

# 3. get random word
def collect_word(words_list):
    random_word = random.choice(words_list)
    while '_' in random_word or ' ' in random_word:
    return random_word.upper()

# 4. display 'hidden word' e.g _ _ _ _ _ _
def Start_game(collect_word):
    correct_word = " _ " * len(collect_word)
    guessed_letters = []
    lives = 7
    guessed = False
    print("Save a man's life by guessing the correct letters to complete the word!")
    print(correct_word)
    print("/n")
    while not guessed and live > 0:
        guess = input ("Please guess a letter: ")
    if len(guess) == 1 and guess.isalpha():
        
    elif len(guess) == len(correct_word) and guess.alpha():

    else: print("Sorry that is not a valid input, please guess a letter from A - Z")


        

# 5. let user guess
# 6. validate the guess, MUST be a letter value
# 7. check if guessed letter has already been guessed
# 8. check secret word to see if letter appears
# 9a. if true then reveal letters in 'hidden word'
# 9b. else lose a life and hang the man
# 10a. check if the word has been guessed fully
# 10b. if true win, else lose if no lives are left
# 11. keep guessing and repeat until 10a
# 12. finish game allow the player to restart the game
