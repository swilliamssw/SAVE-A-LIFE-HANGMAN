import random
from words import words_list

# 1. Display menu
def game_menu():
    """
    Choices for user to start,
    choose difficulty & view the rules of the game.
    """
    print("Choose 1 to play game")
    print("Choose 2 to choose game difficulty")
    print("Choose 3 to read game rules")
    choices = False
    while not choices:
        options = input("/n ")
        if options == "1":
            choices = True

        elif options == "2":
            choices = True

        elif options == "3":
            choices = True
            rules_of_game()

        else:
            print("Please choose 1, 2 or 3 to continue")

# 2. handle choice

# 3. get random word


def collect_word():
    random_word = random.choice(words_list)
    while "_" in random_word or " " in random_word:
        return random_word.upper()

# 4. display 'hidden word' e.g _ _ _ _ _ _
def start_game(random_word):
    hidden_word = "_" * len(random_word)
    game_over = False
    guessed_letters = []
    guessed_word = []
    new_lives = 7
    lives = new_lives
    print("Save a life today by guessing the correct letters to complete the word!")
    print(hidden_word)
    print("\n")
    while not game_over and new_lives > 0:
        player_guess = input("Please guess a letter:\n").upper()

        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in guessed_letters:
                print(
                    "That letter has already been guessed", player_guess, "please try another")
            elif player_guess not in random_word:
                print(player_guess, "is not a valid word.")
                lives -= 1
                guessed_letters.append(player_guess)
            else:
                print("Great guess!", player_guess, "is one of the letters")
                guessed_letters.append(player_guess)
                list_of_words = list(hidden_word)
                indices = [i for i, letter in enumerate(
                    random_word) if letter == player_guess]
                for index in indices:
                   list_of_words[index] = player_guess
                hidden_word = "".join(list_of_words)
                if "_" not in hidden_word:
                    game_over = True
        elif len(player_guess) == len(random_word) and player_guess.alpha():

            if player_guess in guessed_word:
                print("You already guessed", player_guess)
            elif player_guess != hidden_word:
                print(player_guess, "Is not the word")
                lives -= 1
                guessed_word.append(player_guess)
            else:
                game_over = True
                hidden_word = random_word    
        else:
            Print("Sorry that is not a valid input, please guess a letter from A-Z")
        Print(hangman_display(lives))
        print(hidden_word)
        print("\n")
        continue

        print(hangman_display(lives))

    if lives > 0:
        print(f"Lives:{lives}\n")
        print("Letters guessed: " + ", ".join(sorted(player_guess)) + "\n")
        print("Word to be guessed: " + " ".join(word_temp) + "\n")

    if game_over:
        print("CONGRATULATIONS!")
        print("YOU WIN!")
        print("YOU SAVED A LIFE TODAY!")

    else:
        print("OH NO!")
        print("It's a very unfortante day, you was unable to save the man this time")
        print("The correct word was" + hidde_word +
              "Maybe next time you will try harder :(")

def hangman_display(lives):
    remaining_lives = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                  =========
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                  =========
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                  =========
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                  =========
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                  =========
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                  =========
                """,
                # Noose
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                  =========
                """,
                # initial empty state
                """
                   --------
                   |
                   |
                   |
                   |
                   |
                  =========
                """
    ]
    return remaining_lives[lives]


def game_restart(new_lives):
    hidden_word = collect_word()
    start_game(collect_word)
    restart_game = False

    # while not restart_game:
        # reset = input ("Would You Like To Try An Save Another Life? (Y/N) ") == "Y"
        # collect_word = correct_word()
        # start_game(collect_word)

        # try:
            # if reset == "Y"
              # restart_game = True


def Game_title():
    print(
        """
          ___   ___   _____     _     _    ___ ___ ___
         / __| /_\ \ / / __|   /_\   | |  |_ _| __| __|
         \__ \/ _ \ V /| _|   / _ \  | |__ | || _|| _|
         |___/_/ \_\_/ |___| /_/ \_\ |____|___|_| |___|
             _  _   _   _  _  ___ __  __   _   _  _
            | || | /_\ | \| |/ __|  \/  | /_\ | \| |
            | __ |/ _ \| .` | (_ | |\/| |/ _ \| .` |
            |_||_/_/ \_\_|\_|\___|_|  |_/_/ \_\_|\_|
        """
    )

def rules_of_game():
    print(
        """
        To be a hero today, your goal is simple.
        Guess all letter that make up the word that will save a life.
        If you guess wrong you will lose a life for every wrong guess.
        Be very mindful of your guesses, as too much wrong guess will result in you reaching 0 lives.
        Once you have reached a total of 0 lives you would have then missed your oppurtunity to save a life, resulting in the man being hanged.
        GAME OVER!

        But we have faith in you, that you will be amazing and save many lives today, Godspeed!
        """
    )
    back_to_menu = input("To Return To Main Menu, Press Enter.")

    main()

def winner():
    print(
        """
         __   _____  _   _  __      _____ _  _   _
         \ \ / / _ \| | | | \ \    / /_ _| \| | | |
          \ V / (_) | |_| |  \ \/\/ / | || .` | |_|
           |_| \___/ \___/    \_/\_/ |___|_|\_| (_)
        """
    )

def game_over():
    print(
        """
           ___   _   __  __ ___    _____   _____ ___   _
          / __| /_\ |  \/  | __|  / _ \ \ / / __| _ \ | |
         | (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   / |_|
          \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_\ (_)
        """
    )

def main():
    Game_title()
    print(hangman_display(0))

    hangman_word = collect_word()
    start_game(hangman_word)

main()

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
