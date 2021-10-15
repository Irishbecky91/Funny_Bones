"""
This is the submission project for Portfolio Project 3.
The programme made by the developer is a hangman type
game using a halloween theme and a skeleton instead of
a hanged man.
"""
import random
from word_list import spooky_words

# List of variables to be used in functions.
WORD_CHOICE = ""
HIDDEN_WORD = ""
guessed_letters = []
guessed_words = []
TRIES = 6
GUESSED = False
GUESS = ""


# List of Functions to run game.
def choose_spooky_word():
    """
    This function will be used to choose a random word from
    the external list of words in the word_list.py file.
    This will be the word the user must guess before running
    out of tries.
    """
    global WORD_CHOICE
    WORD_CHOICE = random.choice(spooky_words).upper()
    return WORD_CHOICE


def add_to_hidden_word(GUESS):
    """
    This function adds the correct letter or word to the hidden word
    in the terminal. It changes the hidden word into a list and adds
    the letters to the correct index within the list, or shows the
    correctly guessed word and ends the game.
    """
    global GUESSED, HIDDEN_WORD
    guessed_letters.append(GUESS)
    word_choice_as_list = list(HIDDEN_WORD)
    indices = [
        i for i, letter in enumerate(WORD_CHOICE) if letter == GUESS
    ]
    for index in indices:
        word_choice_as_list[index] = GUESS
        HIDDEN_WORD = "".join(word_choice_as_list)
    if "_" not in HIDDEN_WORD:
        GUESSED = True


def input_letter(GUESS):
    """
    This function will check if the letter input is alpha only, and
    has not been input previously. If it either/both are false, an error
    message will be displayed and the user will be asked to enter another
    character.
    """
    if GUESS in guessed_letters:
        print("You already guessed ", GUESS, ". Please try again.")
    elif GUESS not in WORD_CHOICE:
        print(
            GUESS, "is not in the word. Please try again"
            )
        global TRIES
        TRIES -= 1
        guessed_letters.append(GUESS)
    else:
        global HIDDEN_WORD
        print("Well done! ", GUESS, "is in the word!")
        add_to_hidden_word(GUESS)


def input_word(GUESS):
    """
    This function checks if a guessed word has been guessed previously,
    is in the word choice, or if it is the hidden word.
    """
    global GUESSED, HIDDEN_WORD, WORD_CHOICE, TRIES
    if GUESS in guessed_words:
        print("You already guessed ", GUESS, ". Please try again.")
    elif GUESS != WORD_CHOICE:
        print(
            GUESS, "is not the word. Please try again"
            )
        TRIES -= 1
        guessed_words.append(GUESS)
    else:
        GUESSED = True
        HIDDEN_WORD = WORD_CHOICE
        print("Congratulations, you won!! You defeated Funny Bones before \
            he could rise up and take over Halloween.")


def users_input(GUESS):
    """
    This function checks if the user input a letter, a word,
    or an invalid entry. Each condition will activate a different
    function.
    """
    if len(GUESS) == 1 and GUESS.isalpha():
        input_letter(GUESS)
    elif len(GUESS) == len(WORD_CHOICE) and GUESS.isalpha():
        input_word(GUESS)
    else:
        print("This is not a valid guess. Please try again.")
    print(tries_remaining(TRIES))
    print(HIDDEN_WORD)
    print("\n")


def game_over():
    """
    This function will check if the user has run out of tries, input all
    letters in the word, or entered the correct word. If the user runs out
    of tries, a lose message will be displayed. If the user enters all
    letter or a whole word correctly, a win message will be displayed.
    """
    if GUESSED:
        print("You did it, you guessed the word correctly! You win!")
    else:
        print(
            "Sorry, you didn't win this time. The word was " +
            WORD_CHOICE + ". Maybe next time!"
            )


def play_game(WORD_CHOICE):
    """
    This function will start the game, using the other
    functions where needed.
    """
    global HIDDEN_WORD
    print("WELCOME TO FUNNY BONES!!")
    print("\n")
    print("To play the game you must guess the letters that make up the")
    print("hidden word. If you think you know what the word is, you can")
    print("enter it and find out. BUT, if you get a letter or word wrong")
    print("you better watch out... Because Funny Bones will will come for")
    print("you! You can only guess wrong six times, so be careful!")
    print("\n")
    print("Let's Play!")
    print(tries_remaining(TRIES))
    print(HIDDEN_WORD)
    print(WORD_CHOICE)
    print("\n")
    # If the user has not run out of tries,
    # continue to request additional inputs
    while not GUESSED and TRIES > 0:
        # global guess
        GUESS = input("Please enter your guess here: \n").upper()
        users_input(GUESS)


def tries_remaining(TRIES):
    """
    This function contains the images associated with the remaining tries.
    If the user has used up all tries, Funny Bones will be fully formed on
    the screen and the user will lose.
    """
    various_stages = [  # Seventh and final Image - Full Skeleton
                        # No tries remaining.
                      """
                                         _____
                                       /       \\
                                      | |\\   /| |
                         \\ || /        \\   Δ   /       \\ || /
                          \\||/_     o===|+++++|===o    _\\||/
                            \\\\    //   ___||___   \\\\    //
                             \\\\  //    ___||___    \\\\  //
                              \\\\//     ___||___     \\\\//
                                o       __||__       o
                                       |______|
                                o=======o    o=======o
                                 \\\\                 //
                                  \\\\               //
                                   \\\\             //
                                    \\\\           //
                                =====o           o=====
                      """,
                        # Sixth Image - Torso, legs and arms
                        # One try remaining
                      """
                         \\ || /                         \\ || /
                          \\||/_     o============o      _\\||/
                            \\\\    //   ___||___   \\\\    //
                             \\\\  //    ___||___    \\\\  //
                              \\\\//     ___||___     \\\\//
                                o       __||__       o
                                       |______|
                                o=======o    o=======o
                                 \\\\                 //
                                  \\\\               //
                                   \\\\             //
                                    \\\\           //
                                =====o           o=====
                      """,
                        # Fifth Image - Torso, legs and arm
                        # Two tries remaining
                      """
                         \\ || /
                          \\||/_    o============o
                            \\\\    //   ___||___
                             \\\\  //    ___||___
                              \\\\//     ___||___
                                o       __||__
                                       |______|
                                o=======o    o=======o
                                 \\\\                 //
                                  \\\\               //
                                   \\\\             //
                                    \\\\           //
                                =====o           o=====

                      """,
                        # Fourth Image - Torso and legs
                        # Three tries remaining.
                      """
                             o============o
                                ___||___
                                ___||___
                                ___||___
                                 __||__
                                |______|
                         o=======o    o=======o
                          \\\\                 //
                           \\\\               //
                            \\\\             //
                             \\\\           //
                         =====o           o=====
                      """,
                        # Third Image - Torso and leg
                        # Four tries remaining.
                      """
                             o============o
                                ___||___
                                ___||___
                                ___||___
                                 __||__
                                |______|
                         o=======o
                          \\\\
                           \\\\
                            \\\\
                             \\\\
                         =====o
                      """,
                        # Second Image - Torso
                        # Five tries remaining.
                      """
                         o============o
                            ___||___
                            ___||___
                            ___||___
                             __||__
                            |______|
                      """,
                        # First Image - Blank
                        # Six tries remaining
                      """
                      """
                      ]
    return various_stages[TRIES]


def main():
    "This function runs all other functions as needed"
    global HIDDEN_WORD, WORD_CHOICE
    WORD_CHOICE = choose_spooky_word()
    HIDDEN_WORD = "_" * len(WORD_CHOICE)
    play_game(WORD_CHOICE)
    while input("Would you like to play again? (Y/N) \n").upper() == "Y":
        global guessed
        guessed = False
        WORD_CHOICE = choose_spooky_word()
        HIDDEN_WORD = "_" * len(WORD_CHOICE)
        play_game(WORD_CHOICE)


if __name__ == "__main__":
    main()
