
# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():

    # Choose a random word from the list as the solution
    key_word = random.choice(FIVE_LETTER_WORDS).upper()

    def enter_action(s):
        
        # Convert the guess to uppercase
        guess = s.upper()
        
        # Get current row
        current_row = gw.get_current_row()

        # Check if the word is in the list of valid English words
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            return

        # Initialize a list to keep track of which letters in the key_word have been matched
        matched = [False] * len(key_word)

        # Check for correct and present letters
        for i in range(len(guess)):
            if guess[i] == key_word[i]:
                gw.set_square_color(current_row, i, CORRECT_COLOR)
                matched[i] = True
            elif guess[i] in key_word:
                present = False
                for j in range(len(key_word)):
                    if guess[i] == key_word[j] and not matched[j] and guess[j] != key_word[j]:
                        gw.set_square_color(current_row, i, PRESENT_COLOR)
                        matched[j] = True
                        present = True
                        break
                if not present:
                    gw.set_square_color(current_row, i, MISSING_COLOR)
            else:
                gw.set_square_color(current_row, i, MISSING_COLOR)

        # Check if the user guessed the word correctly
        if guess == key_word:
            gw.show_message("Congratulations! You've guessed the word!")
        else:
            if current_row == N_ROWS-1:
                gw.show_message("Game Over! The word was " + key_word)
            else:
                gw.set_current_row(current_row + 1)
                gw.show_message("Try another guess")
                
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
