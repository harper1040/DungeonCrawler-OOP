"""
Joey Harper
2025-1-24
Card Printing
"""

import random
from time import sleep
import turtle
import my_utilities as MU
import Lists


SYMBOLS: dict = {"left_line":"▏", "right_line":"▕", "bottom_line": "▁", "top_line": "▔", "full_heart": "♥", "full_heart2": "♡", "set_symbol": "⌨", "copy_right": "©", "infinite": "∞"}
RARITY: list = ["★", "♦", "⬤"]

colors: dict = {"reds" : {"frame": "darkred", "inner_border": "firebrick2", "background": "indianred1"},
                "blues" : {"frame": "blue1", "inner_border": "blue", "background": "steelblue1"},
                "greens" : {"frame": "green4", "inner_border": "chartreuse4", "background": "mediumseagreen"},
                "whites" : {"frame": "gray5", "inner_border": "lightslategray", "background": "blanchedalmond"},
                "blacks" : {"frame": "gray11", "inner_border": "gray17", "background": "gray39"}}

#Functions that build a card with a supplied color.
def image_fill(card) -> dict:
    """This fills in the text box with background color and text
    
    Arguments:
    card -- Take in a pre generated card.
    """

    scroll: list = []
    for i in range(len(Lists.dungeon)):
        scroll.append([])
        for j in range(len(Lists.dungeon[0])):
            if Lists.dungeon[i][j] == "":
                scroll[i].append(getattr(MU.term, "on_mediumorchid4")+ " " + MU.term.normal)
            elif Lists.dungeon[i][j] == " ":
                scroll[i].append(getattr(MU.term, "on_gray3")+ " " + MU.term.normal)
            else:
                scroll[i].append(getattr(MU.term, "gray3_on_mediumorchid4")+ Lists.dungeon[i][j] + MU.term.normal)
    
    row: int = 4
    col: int = 3
    for i in range(len(Lists.dungeon)):
        for j in range(len(Lists.dungeon[0])):#39 X 9
            card[row][col] = scroll[i][j]
            col += 1
    
        col: int = 3
        row += 1

   
    return card

def textbox_fill(fill, card) -> dict:
    """This fills in the text box with background color and text
    
    Arguments:
    fill -- Color options
    card -- Take in a pre generated card.
    """

    on_back: str = "on_" + fill["background"]
    for i in range(17, 27):
        for j in range(3, len(card[0]) - 3):
            card[i][j] = getattr(MU.term, on_back)+ " " + MU.term.normal

    return card
           
def stat_box(fill, card) -> dict:
    """This draws the stat box where the attack and defense will go.
    
    Arguments:
    fill -- Color options
    card -- Take in a pre generated card.
    """

    frame_inner = fill["frame"] + "_on_" + fill["background"]
    #Top and bottom of stat box

    for i in range(37, 43):
        card[-5][i] = getattr(MU.term, frame_inner)+ "▁" + MU.term.normal
        if i == 37:
            card[-4][i] = getattr(MU.term, frame_inner)+ "▏" + MU.term.normal
        elif i == 43:
            card[-4][i] = getattr(MU.term, frame_inner)+ "▏" + MU.term.normal
        else:
            card[-4][i] = getattr(MU.term, frame_inner)+ " " + MU.term.normal

    return card


def framing(fill, card) -> dict:
    """This function draws the framing lines for the two content areas of the card, history text and the image.
    
    Arguments:
    fill -- Color options
    card -- Take in a pre generated card.
    """

    frame_inner: str = fill["frame"] + "_on_" + fill["background"]
    #Top and bottom frame lines for the image section set to a darker hue of the card color
    for i in range(2, len(card[0]) - 3):
        card[13][i] = getattr(MU.term, frame_inner)+ "▁" + MU.term.normal
        card[16][i] = getattr(MU.term, frame_inner)+ "▔" + MU.term.normal
        card[-4][i] = getattr(MU.term, frame_inner)+ "▁" + MU.term.normal

    for i in range(2, len(card) - 3):
        card[i][2] = getattr(MU.term, frame_inner)+ "▏" + MU.term.normal
        card[i][-3] = getattr(MU.term, frame_inner)+ "▕" + MU.term.normal
        print(getattr(MU.term, frame_inner)+ "▁" + MU.term.normal)

    return card

  
def title_bars(fill, card) -> dict:
    """This creates the title bars where the character name and the character title will be placed.
    
    Arguments:
    fill -- Color options
    card -- Take in a pre generated card.
    """

    #Top title bar to be used for the name of the character and the health
    color_back: str = "on_" + fill["background"] 
    frame_back: str = fill["frame"] + "_on_" + fill["background"]

    for i in range(2, len(card[0]) - 2):
        card[2][i] = getattr(MU.term, color_back)+ " " + MU.term.normal
        card[3][i] = getattr(MU.term, color_back)+ " " + MU.term.normal
        card[2][40] = getattr(MU.term, frame_back) + SYMBOLS["full_heart"] + MU.term.normal


    #Middle title bar to be used for the secondary history to describe who the character is basically a title for the character ("of the north" or "The Brave Traveller")
    for i in range(2, len(card[0]) - 2):
        card[14][i] = getattr(MU.term, color_back)+ " " + MU.term.normal
        card[15][i] = getattr(MU.term, color_back)+ " " + MU.term.normal

    return card
       

def inner_border(fill, card) -> dict:
    """This draws the inner border with shows the color of the card.
    
    Arguments:
    fill -- Color options
    card -- Take in a pre generated card.
    """

    COPY: str = "©Harper 2025"
    ran_num: int = random.randint(1,3000)
    number: str =  str(ran_num) + "/3000"
    rare = random.choice(RARITY)
    frame_inner: str = fill["frame"] + "_on_" + fill["inner_border"]
    other_inner: str = fill["frame"] + "_on_" + fill["background"]
    on_inner: str = "on_" + fill["inner_border"]
    gray: str = "gray2_on_" + fill["inner_border"]
    #Top and bottom border
    for i in range(1, len(card[0]) - 1):
        card[1][i] = getattr(MU.term, frame_inner)+ "▁" + MU.term.normal
        

    #right and left side borders
    for i in range(1, len(card) - 2):
        card[i][1] = getattr(MU.term, frame_inner)+ " " + MU.term.normal
        card[i][-2] = getattr(MU.term, frame_inner)+ " " + MU.term.normal
    

    #double thickness bottom border
    for i in range(1, len(card[0]) - 1):
        if i == 37:
            card[-3][i] = getattr(MU.term, other_inner)+ "▏" + MU.term.normal
        elif i > 37 and i < 43:
            card[-3][i] = getattr(MU.term, other_inner)+ "▁" + MU.term.normal
        elif i == 43:
            card[-3][i] = getattr(MU.term, frame_inner)+ "▏" + MU.term.normal
        else:
            card[-3][i] = getattr(MU.term, on_inner)+ " " + MU.term.normal
        card[-2][i] = getattr(MU.term, on_inner)+ " " + MU.term.normal
    
    col: int = 32
    for i in COPY:
        card[-2][col] = getattr(MU.term, gray)+ i + MU.term.normal
        col += 1
    
    col: int = 3
    if ran_num == 3000:
        card[-2][col] = getattr(MU.term, gray)+ SYMBOLS["infinite"] + MU.term.normal
        col += 1
    else:
        card[-2][col] = getattr(MU.term, gray)+ rare + MU.term.normal
        col += 1
    for i in number:
        card[-2][col] = getattr(MU.term, gray)+ i + MU.term.normal
        col += 1


    return card


def out_border(card) -> list:
    """Here we draw the out border which sets the size of the card.
    
    Arguments:
    card -- Take in a pre generated card.
    """

    #Top and bottom border
    TOP: str =getattr(MU.term, "snow_on_grey13")+ "▔" + MU.term.normal
    BOTTOM: str = getattr(MU.term, "snow_on_grey13")+ "▁" + MU.term.normal
    RIGHT: str = getattr(MU.term, "snow_on_grey13")+ "▕" + MU.term.normal
    LEFT: str = getattr(MU.term, "snow_on_grey13")+ "▏" + MU.term.normal

    for i in range(len(card[0])):
        #MU.move_cursor(3, i)
        card[0][i] = TOP
        card[-1][i] = BOTTOM        

    #right and left border
    for i in range(len(card)):
        #MU.move_cursor(i, 50)
        card[i][0] = LEFT
        card[i][-1] = RIGHT

    
    return card

def draw_card(color) -> list:
    """This runs the various finctions used to draw and populate a character card.
    
    Arguments:
    color -- Chosen color set for the card.
    """

    card: list = []
    for i in range(31):
        card.append([]) 
        for j in range(45):
            card[i].append(" ")

    MU.clear()
    card: list = out_border(card)
    card: list = textbox_fill(colors[color], card)
    card: list = inner_border(colors[color], card)
    card: list = title_bars(colors[color], card)
    card: list = framing(colors[color], card)
    card: list = stat_box(colors[color], card)
    card: list = image_fill( card)
    card.append(colors)
    #cells = [card[4][3], card[5][4]]
    #print(cells)
    
    return card

#These functions display the card provided to them.

def animate_card(card) -> list:
    """This is used to write out an animation of the cards picture because... I can?
    
    Arguments:
    card -- Take in a pre generated card.
    """

    obfiscate: dict = card.pop(-1)
    row: int = 7
    col: int = 55
    index_row: int = 0
    index_col: int = 0
    for i in range(len(Lists.dungeon)):
        for j in range(len(Lists.dungeon[0])):#39 X 9
            MU.move_cursor(row, col)
            print(getattr(MU.term, "on_mediumorchid4")+ " " + MU.term.normal)
            col += 1
            index_col += 1
        col: int = 55
        row += 1
        index_row += 1
    
    row: int = 7
    col: int = 55
    for i in range(len(Lists.dungeon[0])):
        for j in range(len(Lists.dungeon)):   
            MU.move_cursor(row, col)
            if Lists.dungeon[j][i] == "":
                print(getattr(MU.term, "on_mediumorchid4")+ " " + MU.term.normal)
            if Lists.dungeon[j][i] == " ":
                print(getattr(MU.term, "on_gray3")+ " " + MU.term.normal)
            row += 1
        row: int = 7
        col += 1
        sleep(.03)    #Animation time

    MU.move_cursor(34, 3)
    card.append(obfiscate)

    return card

def line_print(row, col, row_num, i) -> int:
    """Supposed to print each col of an array, but needs work.
    
    Arguments:
    row -- An int use to for the row or 'x' coordinate of the cursor.
    col -- An int use to for the col or 'y' coordinate of the cursor.
    row_num -- Variables to keep track of where the row is.
    i -- Incremented variable from slide_animate function.
    """
    for j in range(0, row_num):
        for p in range(len(Lists.dungeon) - 1):
            MU.move_cursor(row, col)
            if Lists.dungeon[p][i] == "":
                print(getattr(MU.term, "on_mediumorchid4")+ " " + MU.term.normal, end = "")
            elif Lists.dungeon[p][i] == " ":
                print(getattr(MU.term, "on_gray3")+ " " + MU.term.normal, end = "")
            row += 1
        col += 1
        row = 7
    return row, col, row_num

def slide_animate() -> list:
    """Begins a slide animation meant to have text slide in from the right. Needs work."""
    
    col_base = 93
    row = 7
    col = 93
    row_num = 1


    for i in range(len(Lists.dungeon[0]) - 1):
        MU.move_cursor(row, col)
        row, col, row_num = line_print(row, col, row_num, i)
                
        col = col_base - row_num
        row_num += 1
            
        sleep(.02)

def display_card(card, row:int = 3, col:int = 52) -> list:
        """This displays the card on the screen.
        
        Arguments:
        card -- Take in a pre generated card.
        """
        #c: int = 3
        obfiscate: dict = card.pop(-1)
        for i in range(len(card)):
            MU.move_cursor(row, col)
            for j in range(len(card[0])):
                if i == len(card) - 1 and j == len(card[0]) - 1:
                    print(card[i][j])
                    
                else:
                    print(card[i][j], end = "")
                    
            row += 1

        card.append(obfiscate)

        return card