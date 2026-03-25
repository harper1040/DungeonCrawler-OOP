"""
Joey Harper
2025-2-25
Dungeon 1
"""

import random
import math
import os
import math
import my_utilities as MU
import hud
import container_assignment as CC
import sound_control as SC


class Tile:
    """Creation and functions of a tile object.
    
    Functions:
    __init__ -- Initializer
    display_tile -- Displays a tile given to it on the screen.
    """ 
    def __init__(self, symbol: str, fore_color: str, back_color: str, passable: bool) -> None:
        """This initializes a tile object.
        
        Arguments:
        self --This takes a board object as self
        fore_color -- This is the text color of the tile.
        back_color -- This is the background color of the tile.
        passble -- This is a bool to tell if the tile is passable (walkable) or not.
        """

        self.symbol: str = symbol
        self.fore_color: str = fore_color
        self.back_color: str = back_color
        self.passable: bool = passable
        self.gate_here: bool = False
        self.occupied: str = None

    def display_tile(self, coords = False) -> None:
        """This takes in a tile object and prints it to the screen.
        
        Arguments:
        self --This takes a tile object as self
        """

        character_tile: Tile = Tile("@", "lightpink1", "darkmagenta", False)
        zombie_tile: Tile = Tile("Z", "limegreen", "darkmagenta", False)
        rat_tile: Tile = Tile("R", "grey3", "darkmagenta", False)
        mimic_tile: Tile = Tile("⍒", "khaki1", "magenta3", False)
        character_tile: Tile = Tile("@", "lightpink1", "darkmagenta", False)
        #player_tile: Tile = Tile(self.symbol, self.fc, self.bc, False)
        blank_tile: Tile = Tile(".", "lightpink1", "darkmagenta", True)
        gate_tile: Tile = Tile("⍓", "red", "green", True)
        crystal = Tile("⍒", "khaki1", "magenta3", True)
        
        if coords:
            MU.move_cursor(coords[0], coords[1])

        color: str = getattr(MU.term, self.fore_color + "_on_" + self.back_color)
        print(color(self.symbol), end = color(""))

        
        """if self.occupied:
            print(color(self.symbol), end = color(""))
        elif self.stairs_here:
            print(color(self.symbol), end = color(""))
        else:
            print(color(self.symbol), end = color(""))"""

   
class Board:
    """Creation and functions of a board object.
    
    Functions:
    __init__ -- Initializer
    create_board -- Creates a 2D array to use as a game board
    make_room -- Takes in size and location information to carve a room out of the overall board.
    place_gate -- Randomly choose an open unoccupied space to place gate
    show_board -- This Runs through the items in the board array and passes them to the display_tile func to print the board.

    """ 
    def __init__(self, width: int, height: int) -> None:
        """This creates the board object.
        
        Arguments:
        self --This take a board object as self
        height -- The height of the board.
        width -- Th width of the board.
        """

        self.height: int = height
        self.width: int = width
        self.board: list = self.create_board(height, width)
        self.boss_room = None
        self.midpoint: list = []
        self.card = []
        self.gate = []
        self.crystal = []
        self.boss = True
        self.monsters = []
        self.mimic = False
        self.mimic_locate = []
        self.monster_key = False
        self.items = []
        self.item_locate = [[0, 0]]



    def create_board(self, width: int, height: int) -> list:
        """This creates a 2d array to be used as a game board within the board object. It places # unpassable tiles in each spot of the board.
        
        Arguments:
        self --This take a board object as self
        height -- The height of the board
        width -- Th width of the board.
        """
        board = []
        
        for row in range(height):
            board.append([])
            for col in range(width):
               tile = Tile("#", "darkolivegreen", "indigo", False)
               board[row].append(tile)
        return board 

    def create_rooms(self, rooms) -> dict:
        """This takes in a number of rooms and randomly attempts to place them in the dungeon if they fit -
          they are sent to make_room and added to the dungeon.
          
          Arguments:
          self -- Dungeon
          rooms -- Number of rooms to be created.
          """
        
        min_measure: int = 4
        max_measure: int = 9

        start_row: int = 1 #1 When not using Credit_room
        start_col: int = 1

        col: int = len(self.board[0]) - 2
        row: int = len(self.board) - 2

        count: int = 0
        exist_room: list = []

        #self.credit_room()

        while True:
            room_width: int = ([random.randint(min_measure, max_measure) for x in range(10)][random.randint(0, 9)])
            room_height: int = ([random.randint(min_measure, max_measure) for x in range(10)][random.randint(0, 9)])
            place_row: int = random.randint(start_row, row) 
            place_col: int = random.randint(start_col, col)


            if abs(place_row + room_height) <= row:
                if abs(place_col + room_width) <= col:
                            
                    self.make_room( room_width, room_height, place_row, place_col, count)
                    exist_room.append([place_row, place_col, place_row + room_width, place_col + room_height])
                    count += 1
                    
                    if count == rooms:
                        break
        
        for i in range(rooms - 1):#add a -1 when not using credit_room
            tile: Tile = Tile(".", "lightpink1", "darkmagenta", True)
            for row in range(abs(self.midpoint[i][0] - self.midpoint[i + 1][0]) + 1):
                
                if self.midpoint[i][0] > self.midpoint[i + 1][0]:
                    self.board[self.midpoint[i][0] - row][self.midpoint[i][1]] = tile
                    #MU.move_cursor(self.midpoint[i][0] - j, self.midpoint[i][1])
                else:
                    self.board[self.midpoint[i][0] + row][self.midpoint[i][1]] = tile
                    #MU.move_cursor(self.midpoint[i][0] + j, self.midpoint[i][1])
            
            for col in range(abs(self.midpoint[i][1] - self.midpoint[i + 1][1])): 
                if self.midpoint[i][1] > self.midpoint[i + 1][1]:
                    self.board[self.midpoint[i + 1][0]][self.midpoint[i][1] - col] = tile
                    #MU.move_cursor(self.midpoint[i][0] - j, self.midpoint[i][1])
                else:
                    self.board[self.midpoint[i + 1][0]][self.midpoint[i][1] + col] = tile
                
            
        return self
    
    
    def credit_room(self) -> list:
        """This is my attempt at extra credit. This room is awful but I tried.
        
        Arguments:
        self
        """
        
        tile: Tile = Tile(".", "lightpink1", "darkmagenta", True)
        coords = [[5, 1], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [2, 3], [3, 3], [7, 3], [1, 4], [2, 4], [7, 4], 
                  [1, 5], [7, 5], [2, 6], [3, 6], [4, 6], [6, 6], [7, 6], [2, 7], [4, 7], [5, 7], [6, 7], [8, 7], [9, 7],
                  [2, 8], [5, 8], [8, 8], [9, 8], [10, 8], [11, 8], [2, 9], [3, 9], [7, 9], [8, 9], [11, 9], [3, 10], 
                  [4, 10], [6, 10], [7, 10], [10, 10], [11, 10], [4, 11], [5, 11], [9, 11], [10, 11], [5, 12], [6, 12], 
                  [7, 12], [8, 12], [9, 12]]

        for i in range(len(coords)):
            self.board[coords[i][0]][coords[i][1]] = tile

        self.midpoint.append([9, 11])
        return self


    def make_room(self,  width: int, height: int, row: int, col: int, index: int = None) -> dict:
        """This makes a room within the game board.
        
        Arguments:
        self --This takes a board object as self
        height -- This is the height of the room.
        width -- This is the width of the room.
        row -- This is the starting row where you place the top left corner of the room on the board.
        col -- This is the starting column where you place the top left corner of the room on the board.
        """
        
        for row_iter in range(height):
            
            for col_iter in range(width):
                tile = Tile(".", "lightpink1", "darkmagenta", True)
                self.board[row + row_iter][col + col_iter] = tile

        self.midpoint.append([math.ceil(height / 2) + row, math.ceil(width / 2) + col])
        return self


    def place_gate(self) -> list:
        """This randomly places a portal gate on the board in a room.
        
        Arguments:
        self --This takes a board object as self
        """
        
        crystal: Tile = Tile("⍒", "khaki1", "magenta2", True)
        gate: Tile = Tile("∏", "lightgoldenrodyellow", "firebrick4", True)
        mimic: Tile = Tile("⍒", "khaki1", "magenta2", True)
        count: int = 0
        while True:
            row: int = random.randint(1, len(self.board) -2)
            col: int = random.randint(1, len(self.board[0]) - 2)
            if self.board[row][col].passable and self.board[row][col].occupied == None:
                
                gate.gate_here = True
                self.board[row][col] = gate
                self.gate = [row, col]
                #MU.move_cursor(row, col)
                #self.board[row][col].display_tile()
                break
            count += 1
        
        while True:
            row: int = random.randint(1, len(self.board) -2)
            col: int = random.randint(1, len(self.board[0]) - 2)
            d: int = math.sqrt(abs(row - self.gate[0])**2 + abs(col - self.gate[1])**2)
            if self.board[row][col].passable and self.board[row][col].occupied == None and self.gate != [row, col]:
                if d > 20:
                    die = MU.die_roller(1, 100)
                    if die <= 33:
                        self.board[row][col] = crystal
                        self.crystal = [row, col]
                    elif die <= 66:
                        
                        self.mimic = True
                        self.mimic_locate = [row, col]
                        self.crystal = [0, 0]
                    else:
                        self.monster_key = True
                        self.crystal = [0, 0]
        
                    return self

    
    def show_board(self) -> None:
        """This shows the game board
        
        Arguments:
        self --This takes a board object as self
        """

        MU.move_cursor(2, 2)
        move_col: int = 2
        start: int = 2
       
        for row in range(len(self.board)):
            MU.move_cursor(row + start, move_col)
            for col in range(len(self.board[0])):
                self.board[row][col].display_tile()
            
                



class Dungeon:
    """Creation and functions of a dungeon object which is a subclass of the item class. Note this class is for text purposes.
    The final "main" dungeon class is in the location_class.py file for simplicity of use throughout the program as a whole.
    
    Functions:
    __init__ -- Initializer

    Arguments:
    None here
    Location -- Take the Location argument as this is a subclass of Location in the location_class.py file.
    """ 
    def __init__(self, height: int, width: int) -> None:
        """Initiallizes a dungeon creating a game board.
        """

        self.height: int = height
        self.width: int = width
        self.board: Board = Board(height, width)



def main() -> None:
    """The main file to test that this file is working as intended.
    """
    os.system('mode 140, 60')
    while True:

        board: Dungeon = Dungeon(40, 55)
        color_dict = {"blacks" : {"frame": "gray11", "inner_border": "gray17", "background": "gray39"}}
        
        
        max_num: int = 8
        min_num: int = 3
        board: Dungeon = board.board.create_rooms(5)
        #board: Dungeon = board.make_room(6, 8, 2, 10)
        board: Dungeon = board.place_gate()
        hud.HUD.draw_hud(color_dict["blacks"])
        board.show_board()
        
        MU.move_cursor(55, 0)
        #ordered = board.midpoint.sort()
        leave = MU.get_key()
        if leave == 113:
            break


if __name__ == "__main__":
    main()
