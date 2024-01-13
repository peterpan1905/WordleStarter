# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    # Choose random word from FIVE_LETTER_WORDS list as the solution
    key_word = random.choice(FIVE_LETTER_WORDS).upper()

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Set row and column starting index values to 0
    row = 0
    col = 0

    # Loop through each letter in the key_word and put it in it's proper row and column
    for ch_position in range(len(key_word)):
        ch = key_word[ch_position]

        gw.set_square_letter(row, col, ch)

        col += 1


# Startup code

if __name__ == "__main__":
    wordle()
