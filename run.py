import random
from word_list import spooky_words


# List of variables to be used in functions.
word_choice = random.choice(spooky_words)
hidden_word = "_" * len(word_choice)
guessed_letters = []
guessed_words = []


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


def play_game(word_choice):
    """
    This function will start the game, using the other
    functions where needed.
    """
    global tries
    global guessed
    tries = 6
    guessed = False
    play_game = input("Do you want to play?")

    print("WELCOME TO FUNNY BONES!!")
    print("\n")
    print("To play the game you must guess the letters that make up the")
    print("hidden word. If you think you know what the word is, you can")
    print("enter it and find out. BUT, if you get a letter or word wrong")
    print("you better watch out... Because Funny Bones will will come for")
    print("you! You can only guess wrong six times, so be careful!")
    print("\n")
    print(play_game)

    while not guessed and tries > 0:
        global users_input
        users_input = input("Please enter your guess here: ").upper()
        input_guess()


def input_guess():
    """
    This function will check if the letter or word input is alpha only, and
    has not been input previously. If it either/both are false, an error
    message will be displayed and the user will be asked to enter another
    character.
    """
    if len(users_input) == 1 and users_input.isalpha():
        if users_input in guessed_letters:
            print("You already guessed ", users_input, ". Please try again.")
        elif users_input not in word_choice:
            print(
                "Uh-oh! ", users_input, " is not in the word. Please try again"
                )
            global tries
            tries -= 1
            guessed_letters.append(users_input)
        else:
            print("Nice one! ", users_input, " is in the word!")
            add_to_hidden_word()


def add_to_hidden_word():
    global hidden_word
    guessed_letters.append(word_choice)
    word_choice_as_list = list(hidden_word)
    indices = [
        i for i, letter in enumerate(word_choice) if letter == users_input
    ]
    for index in indices:
        word_choice_as_list[index] = users_input
    hidden_word = "".join(word_choice_as_list)
    if "_" not in hidden_word:
        global guessed
        guessed = True


def game_over():
    """
    This function will check if the user has run out of tries, input all
    letters in the word, or entered the correct word. If the user runs out
    of tries, a lose message will be displayed. If the user enters all
    letter or a whole word correctly, a win message will be displayed.
    """
    if guessed:
        print("You did it, you guessed the word correctly! You win!")
    else:
        print(
            "Sorry, you didn't win this time. The word was \n"
            + word_choice + ". Maybe next time!"
            )


def tries_remaining():
    """
    This function contains the images associated with the remaining tries.
    If the user has used up all tries, Funny Bones will be fully formed on
    the screen and the userr will lose.
    """
    pass


def main():
    "This function runs all other functions as needed"
    pass


if __name__ == "__main__":
    main()
