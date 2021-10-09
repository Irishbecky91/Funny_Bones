import random
from word_list import spooky_words


# List of variables to be used in functions.
word_choice = random.choice(spooky_words)


# List of Functions to run game.
def choose_spooky_word(word_choice):
    """
    This function will be used to choose a random word from
    the external list of words in the word_list.py file.
    This will be the word the user must guess before running
    out of tries.
    """
    if word_choice == str.isalpha():
        return word_choice.upper


def start_game():
    """
    This function will start the game, using the other
    functions where needed.
    """
    pass


def input_prev_guessed():
    """
    This function will check if the letter of word input
    has been input previously. If so, an error message will
    be displayed and the user will be asked to enter another
    character.
    """
    pass


def alpha_only_input():
    """
    This function will check that the user's input character
    is alpha only. If there is a non-alpha or numeric
    character, an error message will be displayed and the user
    will be asked to input another character.
    """
    pass


def game_over():
    """
    This function will check if the user has run out of tries,
    input all letters in the word, or entered the correct word.
    If the user runs out of tries, a lose message will be displayed.
    If the user enters all letter or a whole word correctly, a
    win message will be displayed.
    """
    pass


def tries_remaining():
    """
    This function contains the images associated with the remaining
    tries. If the user has used up all tries, Funny Bones will be
    fully formed on the screen and the userr will lose.
    """
    pass


def main():
    "This function runs all other functions as needed"
    pass


if __name__ == "__main__":
    main()
