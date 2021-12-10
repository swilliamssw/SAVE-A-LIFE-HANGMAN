import random
from words import words_list

def collect_word():
    word = random.choice(words_list)
    return word.upper()

def game_menu(): 
 """
 Choices for user to start, choose difficulty & and view the rules of the game
 """
print(words_list)
print("Choose" + "1" + "to play game")
print("Choose" + "2" + "to choose game difficulty")
print("Choose" + "3" + "to read game rules")



#Logic 

# 1. Display menu 

# 2. handle choice
# 3. get random word
# 4. display 'hidden word' e.g _ _ _ _ _ _ 
# 5. let user guess 
# 6. validate tht e guess, M§AUST be a letter value
# 7. check if guessed letter has already been guessed
# 8. check secret word to see if letter appears 
# 9a. if true then reveal letters in 'hidden word'
# 9b. else lose a life and hang the man 
# 10a. check if the word has been guessed fully 
# 10b. if true win, else lose if no lives are left 
# 11. keep guessing and repeat until 10a
# 12. finish game allow the player to restart the game