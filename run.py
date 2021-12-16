import random
from words import words_list


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
        options = input("\n ")
        if options == "1":
            choices = True
            difficulty = "normal"
            return difficulty

        elif options == "2":
            choices = True

        elif options == "3":
            choices = True
            rules_of_game()

        else:
            print("Please choose 1, 2 or 3 to continue")


def collect_word():
    """
    Picks a random a word from word,py to 
    be used in the game for the play to guess.
    """
    random_word = random.choice(words_list)
    return random_word.upper()


def difficulty_selection():
    """
    Choices for the player to choose from Easy mode, Normal mode and Hard mode.
    """
    print("\n Choose Your Difficuly\n")
    print(" Choose 1 for Easy mode")
    print(" Choose 2 for Normal mode")
    print(" Choose 3 for Hard mode")

    difficulty = False
    while not difficulty:
        options = input("\n ").upper()
        if options == "1":
            difficulty = True
            tries = 10
            return tries

        elif options == "2":
            difficulty = True
            tries = 7
            return tries

        elif options == "3":
            difficulty = True
            tries = 5
            return tries

        else:
            print("\nPlease choose 1, 2 or 3 for your desired difficulty")


def start_game(random_word, tries):
    """
    Play game, which sets the initial amount of lives based on players choices.
    when the game is over, based on the outcome of the 
    players guesses graphics will be displayed. 
    Also when game is over gives the player options to 
    play again or navigate back to the main menu.
    """
    hidden_word = "_" * len(random_word)
    game_over = False
    guessed_letters = []
    lives = tries

    print("\n")
    print(" LET'S SAVE A LIFE!\n")
    print(f" Lives: {lives}\n")
    print(" Guess this word: " + " ".join(hidden_word) + "\n")
    while not game_over and lives > 0:
        player_guess = input(" Guess a letter:\n").upper()
        if len(player_guess) == 1 and player_guess.isalpha():

            if player_guess in guessed_letters:
                print(
                    " The", player_guess, "has already been used, try again.")

            elif player_guess not in random_word:
                print("\n")
                print(player_guess, "is not correct.")
                guessed_letters.append(player_guess)
                lives -= 1

            else:
                print("\n")
                print(" Great guess!", player_guess, "is in the word.")

                guessed_letters.append(player_guess)
                list_of_words = list(hidden_word)
                indices = [i for i, letter in enumerate(
                    random_word) if letter == player_guess]
                for index in indices:
                    list_of_words[index] = player_guess
                hidden_word = "".join(list_of_words)
                if "_" not in hidden_word:
                    game_over = True
        else:
            print("\n Sorry that is not a valid input,"
                  "please guess a letter from A-Z\n")
            continue

        print(hangman_display(lives))

        if lives > 0:
            print(f" Lives: {lives}\n")
            print(" Guess this word: " + " ".join(hidden_word) + "\n")
            print(" Letters guessed: " + ", ".join(sorted(player_guess)))
            print("\n")

    if game_over:
        print(" CONGRATULATIONS YOU WIN!")
        print(" YOU SAVED A LIFE TODAY!")
        winner()

    else:
        print(" OH NO!")
        print(" It's a very unfortante day,"
              "you was unable to save the man this time")
        print(" The correct word was " + random_word +
              "\n Maybe next time you will try harder.")
        hangman()

    game_restart(tries)


def hangman_display(lives):
    """
    Games hangman graphics which displays based on lives that are left.
    """
    remaining_lives = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |/     |
                   |      O
                   |     \\|/
                   |      |
                   |\\    / \\
                  ==========
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |\\    /
                  ==========
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |\\
                  ==========
                """,
                # head, torso, and one arm
                """
                   --------
                   |/     |
                   |      O
                   |     \\|
                   |      |
                   |\\
                  ==========
                """,
                # torso
                """
                   --------
                   |/     |
                   |      O
                   |      |
                   |      |
                   |\\
                  ==========
                """,
                # Noose, head & torso
                """
                   --------
                   |/     |
                   |      O
                   |      |
                   |
                   |\\
                  ==========
                """,
                # Noose & Head
                """
                   --------
                   |/     |
                   |      O
                   |
                   |
                   |\\
                  ==========
                """,
                # Noose
                """
                   --------
                   |/     |
                   |
                   |
                   |
                   |\\
                  ==========
                """,
                # Complete Hang stand
                """
                    --------
                    |/
                    |
                    |
                    |
                    |
                    |\\
                  ==========
                """,
                # Horizontal bar
                """
                    --------
                    |/
                    |
                    |
                    |
                    |
                    |
                  ==========
                """,
                # Support bar for horizontal bar
                """
                    |/
                    |
                    |
                    |
                    |
                    |
                   ==========
                """,
                # Vertical stand
                """
                    |
                    |
                    |
                    |
                    |
                   ==========
                """,
                # initial empty state
                """







                """
    ]
    return remaining_lives[lives]


def game_restart(tries):
    """
    Game restart, offers player to 
    play again or navigate back to the main menu.
    """
    restart_game = False

    while not restart_game:
        play_again = input("Play Again?  (Y/N) ").upper()

        if play_again == "Y":
            restart_game = True
            hangman_word = collect_word()
            start_game(hangman_word, tries)

        elif play_again == "N":
            restart_game = True
            main()

        else:
            print(f" You must type Y or N. You typed {(play_again)}")


def game_title():
    """
    Games title, which displays at the start of the game. 
    """
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
    """
    Games rules, which outlines all the basics on how to play the game.
    """
    print(
        """
        To be a hero today, your goal is simple.

        Guess all letter that make up the word that will save a life.

        If you guess wrong you will lose a life for every wrong guess.

        Be very mindful of your guesses, as too much wrong guesses
        will result in you reaching 0 lives.

        Once you have reached a total of 0 lives, you would have
        then missed your oppurtunity to save a life,
        resulting in the man being hanged.

        But we have faith that you will be amazing
        and save many lives today. GODSPEED!
        """
    )
    main = input("To Return To Main Menu, Press Enter.")
    print("\n")
    main()


def winner():
    """
    Displays You Win! Graphic.
    """
    print(
        """
         __   _____  _   _  __      _____ _  _   _
         \ \ / / _ \| | | | \ \    / /_ _| \| | | |
          \ V / (_) | |_| |  \ \/\/ / | || .` | |_|
           |_| \___/ \___/    \_/\_/ |___|_|\_| (_)
        """
    )


def hangman():
    """
    Displays Game Over! Graphics.
    """
    print(
        """
           ___   _   __  __ ___    _____   _____ ___   _
          / __| /_\ |  \/  | __|  / _ \ \ / / __| _ \ | |
         | (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   / |_|
          \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_\ (_)
        """
    )


def main():
    """
    Runs the game.
    """
    game_title()
    print(hangman_display(0))
    difficulty = game_menu()

    if difficulty == "normal":
        tries = 7

    else:
        tries = difficulty_selection()

    hangman_word = collect_word()
    start_game(hangman_word, tries)


main()
