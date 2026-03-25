"""
Joey Harper
2025-1-14
my_utilities.py
Collection of various functions useful in a variety of projects.
"""
import os
import blessed
import random
import msvcrt

#Start blessed terminal. Needed for MoveCursor and any other blessed related commands.
term: blessed.win_terminal.Terminal = blessed.Terminal() 



def move_cursor(row :int, col :int) -> None:
    """Moves cursor. This is a wrapper function to swap row and col for ease of use.
    
    Arguments:
    row -- Takes in an int to use as the row or 'x' coordinate.
    col -- Takes in an int to use as the col or 'y' coordinate.
    """ 

    print(term.move_xy(col, row), end="")

def get_key() -> int:
    """Gets a key press without having to press enter"""

    while True:
        if msvcrt.kbhit():
            userInput: bytes = msvcrt.getch()
            userInput: int = ord(userInput)
            return userInput

def die_roller(times :int, sides :int) -> int:
    """Rolls {times} number of dice with {sides} number of sides. Returns sum of all rolls
    
    Arguments:
    times -- Takes an int to signify how many times to roll a die.
    sides -- Takes an int to signify the number of sides the die has.
    """

    ans: int = 0
    for i in range(int(times)):
      num: int = random.randint(1,int(sides))
      ans += num
    return ans


def target_roller(times :int, sides :int, target :int) -> int:
    """Rolls {times} number of dice with {sides} number of sides against {target} number. Returns number of dice that meet or beat {target}
    
    Arguments:
    times -- Takes an int to signify how many times to roll a die.
    sides -- Takes an int to signify the number of sides the die has.
    target -- This is an int that is the chosen value the user wants to roll.
    """

    ans: int = 0
    for i in range(int(times)):
      num: int = random.randint(1,int(sides))
      if num >= int(target):
        ans += 1
    return ans


def clear() -> None:
    """Cross platform screen clearing"""
        
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
