# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    # Initialize the keyword
    keyword = ""
    random_number = random.randint(0, len(FIVE_LETTER_WORDS))
    keyword = FIVE_LETTER_WORDS[random_number]

    def enter_action(s):
        # Check if the word is in the list of valid English words
        if s.lower() in FIVE_LETTER_WORDS:
            # Check if it is the keyword
            if s.lower() == keyword:
                # Handle the case when the correct keyword is entered
                gw.show_message("You win!")
            else:
                # It's not the keyword, check if there is another row to advance to
                current_row = gw.get_current_row()
                if current_row < N_ROWS - 1:
                    # Advance to the next row
                    gw.set_current_row(current_row + 1)
                    gw.show_message(f"Answer: {keyword}")
                else:
                    # You lost
                    gw.show_message("Better luck next time!")
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()