import random
from word_list import spooky_words

# List of variables to be used in functions.
word_choice = random.choice(spooky_words)
hidden_word = "_" * len(word_choice)
guessed_letters = []
guessed_words = []
tries = 6
guessed = False


# List of Functions to run game.
def choose_spooky_word():
    """
    This function will be used to choose a random word from
    the external list of words in the word_list.py file.
    This will be the word the user must guess before running
    out of tries.
    """
    global word_choice
    return word_choice.upper()


def add_to_hidden_word():
    """
    This function adds the correct letter or word to the hiddn word
    in the terminal. It changes the hidden word into a list and adds
    the letters to the correct index within the list, or shows the
    correctly guessed word and ends the game.
    """
    global guessed, hidden_word
    guessed_letters.append(guess)
    word_choice_as_list = list(hidden_word)
    indices = [
        i for i, letter in enumerate(word_choice) if letter == guess
    ]
    for index in indices:
        word_choice_as_list[index] = guess
        hidden_word = "".join(word_choice_as_list)
    if "_" not in hidden_word:
        guessed = True


def input_letter(guess):
    """
    This function will check if the letter input is alpha only, and
    has not been input previously. If it either/both are false, an error
    message will be displayed and the user will be asked to enter another
    character.
    """
    if guess in guessed_letters:
        print("You already guessed ", guess, ". Please try again.")
    elif guess not in word_choice:
        print(
            guess, "is not in the word. Please try again"
            )
        global tries
        tries -= 1
        guessed_letters.append(guess)
    else:
        print("Well done! ", guess, "is in the word!")
        print("guess is correct and not previously used works")
        add_to_hidden_word()


def input_word(guess):
    """
    This function checks if a guessed word has been guessed previously,
    is in the word choice, or if it is the hidden word.
    """
    global guessed, hidden_word, word_choice, tries
    if guess in guessed_words:
        print("You already guessed ", guess, ". Please try again.")
    elif guess != word_choice:
        print(
            guess, "is not the word. Please try again"
            )
        tries -= 1
        guessed_words.append(guess)
    else:
        guessed = True
        hidden_word = word_choice


def users_input(guess):
    """
    This function checks if the user input a letter, a word,
    or an invalid entry. Each condition will activate a different 
    function.
    """
    if len(guess) == 1 and guess.isalpha():
        input_letter(guess)
    elif len(guess) == len(word_choice) and guess.isalpha():
        input_word(guess)
    else:
        print("This is not a valid guess. Please try again.")
    print(tries_remaining(tries))
    print(hidden_word)
    print("\n")


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
            "Sorry, you didn't win this time. The word was " +
            word_choice + ". Maybe next time!"
            )


def play_game(word_choice):
    """
    This function will start the game, using the other
    functions where needed.
    """
    print("WELCOME TO FUNNY BONES!!")
    print("\n")
    print("To play the game you must guess the letters that make up the")
    print("hidden word. If you think you know what the word is, you can")
    print("enter it and find out. BUT, if you get a letter or word wrong")
    print("you better watch out... Because Funny Bones will will come for")
    print("you! You can only guess wrong six times, so be careful!")
    print("\n")
    print("Let's Play!")
    print(tries_remaining(tries))
    print(hidden_word)
    print("The hidden word is " + word_choice)
    print("\n")
    # If the user has not run out of tries,
    # continue to request additional inputs
    while not guessed and tries > 0:
        global guess
        guess = input("Please enter your guess here: ").upper()
        users_input(guess)


def tries_remaining(tries):
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
                         o=======o    o=======o
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
    return various_stages[tries]


def main():
    "This function runs all other functions as needed"
    word_choice = choose_spooky_word()
    play_game(word_choice)
    while input("Would you like to play again? (Y/N) ").upper() == "Y":
        word_choice = choose_spooky_word()
        play_game(word_choice)


if __name__ == "__main__":
    main()
