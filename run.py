import random
from word_list import spooky_words

word_choice = random.choice(spooky_words)

def choose_spooky_word():
    return word_choice.upper


def play_funny_bones():
    complete_word = "_" * len(word_choice)
    guessed_letters = []
    guessed_words = []
    guessed = False
    lives = 6

    print("WELCOME TO FUNNY BONES!")
    print("\n")
    print("To play 'Funny Bones', you must guess the correct letters")
    print("to create the word. If you think you know the word, feel")
    print("free to guess! Just remember though,every wrong letter or")
    print("word resurrects the Funny Bones! Don't let him catch you!")
    print("\n")
    print(funny_bones_lives(lives))
    print(complete_word)
    print("\n")


def funny_bones_lives(lives):
    levels = ["""
         _____
       /       \\
      |  0   0  |
       \\   Δ   /
        |+++++|
          | |         |||
      o==========o   \\|||
     || ___||___ ||  //
     || ___||___ || //
     || ___||___ ||//
     ||    ||     o/
     ||  __||__
     || |______|
    //   o    o
        ||    ||
        ||    ||
        ||    ||
        o|    |o
        ||    ||
        ||    ||
        ||    ||
     ====o ====o
    """,
    """
                      |||
      o==========o   \\|||
     || ___||___ ||  //
     || ___||___ || //
     || ___||___ ||//
     ||    ||     o/
     ||  __||__
     || |______|
    //   o    o
        ||    ||
        ||    ||
        ||    ||
        o|    |o
        ||    ||
        ||    ||
        ||    ||
     ====o ====o
    """,
    """
      o==========o
     || ___||___
     || ___||___
     || ___||___
     ||    ||
     ||  __||__
     || |______|
    //   o    o
        ||    ||
        ||    ||
        ||    ||
        o|    |o
        ||    ||
        ||    ||
        ||    ||
     ====o ====o
    """,
    """
     o==========o
       ___||___
       ___||___
       ___||___
          ||
        __||__
       |______|
        o    o
       ||    ||
       ||    ||
       ||    ||
       o|    |o
       ||    ||
       ||    ||
       ||    ||
    ====o ====o
    """,
    """
     o==========o
       ___||___
       ___||___
       ___||___
          ||
        __||__
       |______|
        o    o
       ||    ||
       ||    ||
       ||    ||
       o|    |o
       ||    ||
       ||    ||
       ||    ||
    ====o ====o
    """,
    """
    o==========o
      ___||___
      ___||___
      ___||___
         ||
       __||__
      |______|
       o    o
    """
    ]


def main():
    print("hi")


main()
