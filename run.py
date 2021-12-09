import random
from words import words_list

def collect_word():
    word = random.choice(words_list)
    return words.upper()

def initial_game(): 
 """
 Choices for user to start, choose difficulty & and view the rules of the game
 """
print(words_list)
print("Choose" + "1" + "to play game")
print("Choose" + "2" + "to choose game difficulty")
print("Choose" + "3" + "to read game rules")