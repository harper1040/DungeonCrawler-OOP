"""
Joey Harper
Player Class
2025-1-21
"""
import sys
import random
from time import time
import math
import my_utilities as MU
import dungeon1 as DG
import card_print #passthrough don't remove
import container_assignment as CC
import List2
import hud
import sound_control as SC

class GameCharacter:
    """This class creates and controls a game character object
    
    Functions:
    __init__ -- Creates the character object
    __str__ -- String method for printing clean character information.
    gen_character -- Pulls the name and history information and uses it to create a character object.
    gen_stats -- Rolls dice to decide what the character's attack, defense and health stats are
    gen_name -- Randomly generates name text
    new_character -- Adds character and character card to a list.
    populate_card -- Takes the character information and appends it to the card lists
    upkeep -- Makes changes based on passage of time.
    """
    
    
    def __init__(self) -> None:
        """Initializes a character object.
        
        Arguments:
        name -- Character's name
        history -- Character's history
        title -- Character's title
        """

        self._name: str = GameCharacter.gen_name()
        self._attack: int = 0
        self._defense: int = 0
        self._health: int = 0
        self.max_attack: int = 0
        self.max_defense: int = 0
        self.max_health: int = 0
        self._card: list = []
        self.gold: int = 50
        self.date: dict = {"season": 1, "week": 1}
        self.container = {}
        self.crystal = None
        self.tile = ""
        self.equipped = {"Rusty Armor": False, "Small Sword": False}
        

    

    def gen_character() -> str:
        """Runs generator functions and takes the returned values to create a character object."""

        name = Character.gen_name()
        history, title = Character.gen_history()
        character: Character = Character(name, history, title)
        

        return character
    
    def gen_stats() -> None:
        """Rolls dice to pick the character's attack, defense, and health stats."""

        attack = MU.die_roller(3, 6) + MU.die_roller(5, 4)
        defense = MU.die_roller(3, 6) + MU.die_roller(5, 4)
        health = MU.die_roller(5, 6) + MU.die_roller(5, 4)

        return attack, defense, health

    def gen_name() -> str:
        """Chooses randomly from lists to create a name for the character object."""

        f_name: str = random.choice(List2.namesList)
        l_name: str = random.choice(List2.namesList2)

        name: str = f"{f_name}{l_name}"
        return name

    def new_character(self, card) -> None:
        """Add the character chosen and the card representation to lists for use later.
        
        Arguments:
        card -- Take a pre generated card and adds it to a list.
        """

        self._card = card
        Character.character_list.append(self)
        

    def populate_card(self, card, choice) -> list:
        """This takes all the character information (name, history, etc) and places it in the card where it belongs.
        
        Arguments:
        card -- Pre generated card
        choice -- Color choice for the card
        """

        col: int = 3
        text_color: str = "gray2" + "_on_" + card[-1][choice]["background"]   
        #Populate the name field
        if len(self._name) < 30:#30 3 -8
            for i in range(len(self._name)):
                card[2][col] = getattr(MU.term, text_color) + self._name[i] + MU.term.normal
                col += 1

        col: int = 37
        row: int = 2
        #Populates the health attack and defense areas.
        if self._health > 9:
            for i in range(2):
                card[row][col] = getattr(MU.term, text_color) + str(self._health)[i] + MU.term.normal
                col += 1
        elif self._health > 99:
            for i in range(3):
                card[row][col] = getattr(MU.term, text_color) + str(self._health)[i] + MU.term.normal
                col += 1

        col: int = 37
        row: int = -5
        for i in range(2):
                card[row][col] = getattr(MU.term, text_color) + str(self._attack)[i] + MU.term.normal
                col += 1
        card[row][col] = getattr(MU.term, text_color) + "/" + MU.term.normal
        col += 1
        for i in range(2):
                card[row][col] = getattr(MU.term, text_color) + str(self._defense)[i] + MU.term.normal
                col += 1
        
        count: int = 0
        col: int = 3
        row: int = 17
        #This populates the history section.
        if len(self._history) > 34:#34> *8\/  17, 3
                      
            sep: list = self._history.split(" ")
            for i in sep:
                count += len(i) + 1
                if count > 35:
                    row += 1
                    col: int = 3
                    count: int = 0
                    if row > 23:
                        for p in range(3):
                            card[row][col] = getattr(MU.term, text_color) + "." + MU.term.normal
                            col += 1
                            break
                col += 1
                for j in i:
                    card[row][col] = getattr(MU.term, text_color) + j + MU.term.normal
                    col += 1
             
        else:
            col: int = 3
            row: int = 17
            for i in self._history:
                card[row][col] = getattr(MU.term, text_color) + i + MU.term.normal
                col += 1

        col: int = 5
        row: int = 14
        for i in self.title:
            card[row][col] = getattr(MU.term, text_color) + i + MU.term.normal
            col += 1

        card[-1] = card[-1][choice]

        return card
        
    def upkeep(self) -> None:
        """This progesses time forware when the player rests.

        Arguments:
        self -- Take in a player object.
        """
        if self.date["week"] == 13:
            self.date["week"] = 1
            if self.date["season"] == 4:
                self.date["season"] = 1
            else:
                self.date["season"] += 1
        else:
            self.date["week"] += 1

   
                

class Actor:
    """This class creates and controls an actor object
    
    Functions:
    __init__ -- Creates the character object
    place_actor -- 
    interact -- 
    death -- 
    """

    def __init__(self, fore_color, back_color, symbol, title) -> None:
        """Initializes an actor.

        Arguments:
        self -- The actor
        fore_color -- text color
        back_color -- background color
        symbol -- The actor symbol
        title -- What the actor is called when occupying a space.
        """
        self.fc = fore_color
        self.bc = back_color
        self.symbol = symbol
        self.title: str = title
        self.current_coord = []
     
    def place_actor(self, board, mimic = []) -> dict:
        """This chooses where to place the player on the board.

        Arguments:
        board -- The board we place the player on.
        character -- The player character.
        """

        actor: DG.Tile = DG.Tile(self.symbol, self.fc, self.bc, False)
        actor.occupied = self.title
        while True:
            row: int = random.randint(0, len(board) - 1)
            col: int = random.randint(0, len(board[0]) - 1)
            
            if self.title == "Mimic":
                board[mimic[0]][mimic[1]] = actor
                self.current_coord = [mimic[0], mimic[1]]
                return board, self
            elif board[row][col].passable and board[row][col].occupied == None:
                board[row][col] = actor
                self.current_coord = [row, col]
                return board, self

    def move_actor(self, board, target, direction = None) -> None:

        """This will allow the player to move his character around the map.
        
        Arguments:
        board -- The board we want to move around.
        character -- The players character we're moving.
        direction -- the direction the character is to be moved if able.
        """
        coords: list = []
        coords.append(self.current_coord[0])
        coords.append(self.current_coord[1])
        #hud.HUD.aux1_message(f"{coords}, player {character.current_coord}", card = character._card[-1])
        direct = ["UP", "DOWN", "RIGHT", "LEFT"]
        player_tile: DG.Tile = DG.Tile(self.symbol, self.fc, self.bc, False)
        blank_tile: DG.Tile = DG.Tile(".", "lightpink1", "darkmagenta", True)
        gate_tile: DG.Tile = DG.Tile("∏","lightgoldenrodyellow", "firebrick4", True)
        crystal_tile = DG.Tile("⍒", "khaki1", "magenta2", True)
        item = DG.Tile("ⁱ", "snow", "grey3", True)

        player_tile.occupied = self.title

        if self.title == "Mimic":
            if self.runner:
                pass
            else:
                direction = None
        elif self.title != "Character":
            direction = random.choice(direct)
        
        
        match direction:
            case "UP":
                #row - 1
                
                if board.board[coords[0] - 1][coords[1]].occupied != None:
                        if self.title == "Character":
                            for mon in target:
                                if mon.current_coord[0] == coords[0] - 1 and mon.current_coord[1] == coords[1]:
                                    self.interact(board, mon)
                        else:
                            if target.current_coord[0] == coords[0] - 1 and target.current_coord[1] == coords[1]:
                                    self.interact(board, target)

                if board.board[coords[0] - 1][coords[1]].passable and board.board[coords[0] - 1][coords[1]].occupied == None:
                    
                    if coords == board.gate:
                        board.board[coords[0]][coords[1]] = gate_tile
                    elif coords == board.crystal:
                        if self.crystal == None:
                            board.board[coords[0]][coords[1]] = crystal_tile
                        else:
                            board.board[coords[0]][coords[1]] = blank_tile
                            board.crystal = [0, 0]
                    elif coords in board.item_locate:
                        board.board[coords[0]][coords[1]] = item
                    else:
                        board.board[coords[0]][coords[1]] = blank_tile
                    
                    board.board[coords[0] - 1][coords[1]] = player_tile
                    self.current_coord = [coords[0] - 1, coords[1]]

                    
                    MU.move_cursor(coords[0] + 2, coords[1] + 2)
                    board.board[coords[0]][coords[1]].display_tile()
                    MU.move_cursor(coords[0] + 1, coords[1] + 2)
                    board.board[coords[0] - 1][coords[1]].display_tile()

                    if self.title == "Character":
                        if self.current_coord[0] == board.gate[0] and self.current_coord[1] == board.gate[1]:
                            if self.crystal == None:
                                hud.HUD.system_message("You need an ancient crystal to activate the gate!", card = self._card[-1])
                            else:
                                hud.HUD.system_message("Use the ancient crystal to open the gate!", card = self._card[-1])

                        if self.current_coord[0] == board.crystal[0] and self.current_coord[1] == board.crystal[1]:
                            if self.crystal == None:
                                hud.HUD.system_message("What's that shining on the ground?!", card = self._card[-1])
                            
                    
                        self.steps += 1
                        hud.HUD.player_window(self, steps = True)
                    
                
            case "DOWN":
                #row + 1
                #hud.HUD.aux1_message(f"This is {direction}!!", card = character._card[-1])
                
                if board.board[coords[0] + 1][coords[1]].occupied != None:
                        if self.title == "Character":
                            for mon in target:
                                if mon.current_coord[0] == coords[0] + 1 and mon.current_coord[1] == coords[1]:
                                    self.interact(board, mon)
                        else:
                            if target.current_coord[0] == coords[0] + 1 and target.current_coord[1] == coords[1]:
                                self.interact(board, target)

                if board.board[coords[0] + 1][coords[1]].passable and board.board[coords[0] + 1][coords[1]].occupied == None:
                    if coords == board.gate:
                        board.board[coords[0]][coords[1]] = gate_tile
                    elif coords == board.crystal:
                        if self.crystal == None:
                            board.board[coords[0]][coords[1]] = crystal_tile
                        else:
                            board.board[coords[0]][coords[1]] = blank_tile
                            board.crystal = [0, 0]
                    elif coords in board.item_locate:
                        board.board[coords[0]][coords[1]] = item
                    else:
                        board.board[coords[0]][coords[1]] = blank_tile
                    #elif coords[0] == board.items["Mon"][1][0] and coords[1] == board.items["Mon"][1][1]:
                        #board.board[coords[0]][coords[1]] = item
                    
                    
                    board.board[coords[0] + 1][coords[1]] = player_tile
                    self.current_coord = [coords[0] + 1, coords[1]]

                    
                    MU.move_cursor(coords[0] + 2, coords[1] + 2)
                    board.board[coords[0]][coords[1]].display_tile()
                    MU.move_cursor(coords[0] + 3, coords[1] + 2)
                    board.board[coords[0] + 1][coords[1]].display_tile()

                    if self.title == "Character":   
                        if self.current_coord[0] == board.gate[0] and self.current_coord[1] == board.gate[1]:
                            if self.crystal == None:
                                hud.HUD.system_message("You need an ancient crystal to activate the gate!", card = self._card[-1])
                            else:
                                hud.HUD.system_message("Use the ancient crystal to open the gate!", card = self._card[-1])

                        if self.current_coord[0] == board.crystal[0] and self.current_coord[1] == board.crystal[1]:
                            if self.crystal == None:
                                hud.HUD.system_message("What's that shining on the ground?!", card = self._card[-1])
                        
                        self.steps += 1
                        hud.HUD.player_window(self, steps = True)
                    #hud.HUD.aux2_message(f"{coords}, player {character.current_coord}", card = character._card[-1])
            case "LEFT":
                #col - 1

                if board.board[coords[0]][coords[1] - 1].occupied != None:
                        if self.title == "Character":
                            for mon in target:
                                if mon.current_coord[0] == coords[0] and mon.current_coord[1] == coords[1] - 1:
                                    self.interact(board, mon)
                        else:
                            if target.current_coord[0] == coords[0] and target.current_coord[1] == coords[1] - 1:
                                    self.interact(board, target)


                if board.board[coords[0]][coords[1] - 1].passable and board.board[coords[0]][coords[1] - 1].occupied == None:
                    if coords == board.gate:
                        board.board[coords[0]][coords[1]] = gate_tile
                    elif coords == board.crystal:
                        if self.crystal == None:
                            board.board[coords[0]][coords[1]] = crystal_tile
                        else:
                            board.board[coords[0]][coords[1]] = blank_tile
                            board.crystal = [0, 0]
                    elif coords in board.item_locate:
                        board.board[coords[0]][coords[1]] = item
                    else:
                        board.board[coords[0]][coords[1]] = blank_tile
                    
                    board.board[coords[0]][coords[1] - 1] = player_tile
                    self.current_coord = [coords[0], coords[1] - 1]

                    

                    MU.move_cursor(coords[0] + 2, coords[1] + 1)
                    board.board[coords[0]][coords[1] - 1].display_tile()
                    
                    MU.move_cursor(coords[0] + 2, coords[1] + 2)
                    board.board[coords[0]][coords[1]].display_tile()

                    if self.title == "Character":
                        if self.current_coord[0] == board.gate[0] and self.current_coord[1] == board.gate[1]:
                            if self.crystal == None:
                                hud.HUD.system_message("You need an ancient crystal to activate the gate!", card = self._card[-1])
                            else:
                                hud.HUD.system_message("Use the ancient crystal to open the gate!", card = self._card[-1])

                        if self.current_coord[0] == board.crystal[0] and self.current_coord[1] == board.crystal[1]:
                            if self.crystal == None:
                                hud.HUD.system_message("What's that shining on the ground?!", card = self._card[-1])
                        
                        self.steps += 1
                        hud.HUD.player_window(self, steps = True)
                    #hud.HUD.aux1_message(f"{coords}, player {character.current_coord}", card = character._card[-1])
            case "RIGHT":
                #col + 1

                if board.board[coords[0]][coords[1] + 1].occupied != None:
                        if self.title == "Character":
                            for mon in target:
                                if mon.current_coord[0] == coords[0] and mon.current_coord[1] == coords[1] + 1:
                                    self.interact(board, mon)
                        else:
                            if target.current_coord[0] == coords[0] and target.current_coord[1] == coords[1] + 1:
                                    self.interact(board, target)

                if board.board[coords[0]][coords[1] + 1].passable and board.board[coords[0]][coords[1] + 1].occupied == None:
                    if coords == board.gate:
                        board.board[coords[0]][coords[1]] = gate_tile
                    elif coords == board.crystal:
                        if self.crystal == None:
                            board.board[coords[0]][coords[1]] = crystal_tile
                        else:
                            board.board[coords[0]][coords[1]] = blank_tile
                            board.crystal = [0, 0]
                    elif coords in board.item_locate:
                        board.board[coords[0]][coords[1]] = item
                    else:
                        board.board[coords[0]][coords[1]] = blank_tile
                    
                    
                    board.board[coords[0]][coords[1] + 1] = player_tile
                    self.current_coord = [coords[0], coords[1] + 1]

                    

                    MU.move_cursor(coords[0] + 2, coords[1] + 3)
                    board.board[coords[0]][coords[1] + 1].display_tile()
                    
                    MU.move_cursor(coords[0] + 2, coords[1] + 2)
                    board.board[coords[0]][coords[1]].display_tile()

                    if self.title == "Character":
                        if self.current_coord[0] == board.gate[0] and self.current_coord[1] == board.gate[1]:
                            if self.crystal == None:
                                hud.HUD.system_message("You need an ancient crystal to activate the gate!", card = self._card[-1])
                            else:
                                hud.HUD.system_message("Use the ancient crystal to open the gate!", card = self._card[-1])

                        if self.current_coord[0] == board.crystal[0] and self.current_coord[1] == board.crystal[1]:
                            if self.crystal == None:
                                hud.HUD.system_message("What's that shining on the ground?!", card = self._card[-1])
                        
                        self.steps += 1
                        hud.HUD.player_window(self, steps = True)
                    #hud.HUD.aux1_message(f"{coords}, player {character.current_coord}", card = character._card[-1])   

    def interact(self, board, target) -> None:
        """This does things when two actors bump into or intereact with one another.

        Arguments:
        self -- The actor initiating the bumping.
        board -- The board we place the player on.
        target -- The target of the attack.
        """

        direct = ["UP", "DOWN", "RIGHT", "LEFT"]

        if self.title == "Character":
            damage = math.floor(self._attack / 5)
            self.damage = damage
            if self.augment["attack"] and time() - self.augment["atime"] < 60:
                damage += 3
            if self.equipped["Small Sword"]:
                damage += 2
            SC.sound_effect("hit")
            if target.title == "Mimic":
                if random.randint(1, 100) > 60:
                    self._health -= 3
                    hud.HUD.aux2_message(f"Mimic did 3 damage.", card = self._card[-1])
                    hud.HUD.player_window(self, damage = True)
                
            if damage >= 0:
                if target.title == "Slime":
                    hud.HUD.aux1_message(f"Eww it's a {target.title}, it's all sticky...", card = self._card[-1])
                    SC.sound_effect("slime")
                else:
                    target._health -= damage
                    hud.HUD.aux1_message(f"{target.title} took {damage} damage! {target._health}", card = self._card[-1])
        elif self.title == "Mimic":
            pass
        elif self.title == "Slime":
            hud.HUD.aux1_message(f"{self.title} go 'Blooub!'", card = target._card[-1])
        else:
            hud.HUD.aux1_message(f"{self.title} go 'I'm Walkin ere!'", card = target._card[-1])

        if target.title == "Mimic":
            
            
            if target._health > 0:
                target.runner = True
                locate = target.current_coord
                new_coord = target.current_coord
                d: int = math.sqrt(abs(new_coord[0] - locate[0])**2 + abs(new_coord[1] - locate[1])**2)
                move = random.choice(direct)
                wrong_way = []
                while True:
                    
                    for i in range(4):
                        target.move_actor(board, self, move)
                        new_coord = target.current_coord
                        if new_coord == locate:
                            move = random.choice(direct)
                                                    
                    
                    break
                board.crystal = target.current_coord
        
        elif target.title == "Character":
            damage = self._attack
            if target.equipped["Rusty Armor"]:
                damage -= 3
            target._health -= damage
            hud.HUD.aux2_message(f"{self.title} did {damage} damage!", card = target._card[-1])

                    


        
        

    def death(self, board, card = None, player = None) -> dict:
        """This is where we kill things off.

        Arguments:
        self -- The one to be shuffled off.
        board -- The board we place the player on.
        card -- If I don't have play to access the player card for color properties I load it in here.
        """

        if self.title != "Character":
            blank_tile: DG.Tile = DG.Tile(".", "lightpink1", "darkmagenta", True)
            crystal: DG.Tile = DG.Tile("⍒", "khaki1", "magenta2", True)

            if self.title == "Mimic" or self.key == True:
                board.board[self.current_coord[0]][self.current_coord[1]] = crystal
                board.board[self.current_coord[0]][self.current_coord[1]].display_tile([self.current_coord[0] + 2, self.current_coord[1]  + 2])
                board.crystal = [self.current_coord[0], self.current_coord[1]]
                board.monster_key = False
                board.mimic = False
            elif self.container:
                self.container.use_item(0, board,  drop = True, locate = self.current_coord)
            else:
                board.board[self.current_coord[0]][self.current_coord[1]] = blank_tile
                board.board[self.current_coord[0]][self.current_coord[1]].display_tile([self.current_coord[0] + 2, self.current_coord[1] + 2])
            hud.HUD.aux1_message(f"{self.title} Died!", card = card)
            if random.randint(1, 100) >= 50:
                if self.gold and player:
                    gold = random.randint(3, 10)
                    player.gold += gold
                    hud.HUD.aux1_message(f"You got {gold} gold! Good for you!'", card = card)
        else:
            MU.clear()
            MU.move_cursor(20, 45)
            color = getattr(MU.term, "red_on_grey3")
            input(color("You LOSE!! LOSER!!"))
            MU.clear()

        return self
        

def splash_screen() -> None:
    """Prints the splash screen prompting the player to start their game.
    """

    
    color: str = "lawngreen_on_gray6"

    for i in range(5, 29):
        for j in range(3, 145):
            MU.move_cursor(i, j)
            print(getattr(MU.term, "blue") + "." + MU.term.normal)
   

    MU.move_cursor(8, 20)
    count: int = 0
    for i in range(8, 16):
        MU.move_cursor(i, 20)
        word: str = getattr(MU.term, color) + List2.splash[count] + MU.term.normal
        print(word)
        count += 1
    

    MU.move_cursor(17, 45)
    
    for i in range(17, 26):
        MU.move_cursor(i, 45)
        word: str = getattr(MU.term, color) + List2.splash[count] + MU.term.normal
        print(word)
        count += 1

    print("\n\n\t\t\t\t\t\tPress Any Key To Start Or Q to Leave! ")
    print("\n\n\t\t\t\t\t\tFor Better result use MS Gothic font and Sound!")

    start_game = MU.get_key()
    if start_game == 113:
        print("\n\n")
        sys.exit(0)

class Character(GameCharacter, Actor):
    """This class creates and controls a character object which is the players avatar.
    
    Functions:
    __init__ -- Creates the character object
    gen_history -- Randomly selects history text
    move_actor -- This moves the player character

    Inherits:
    Gamecharacter Class
    Actor Class
    """

    character_list = []

    def __init__(self, fore_color, back_color, symbol, title) -> None:
        """Initializes a player character inherits from GameCharacter and Actor

        Arguments:
        self -- The player character
        fore_color -- text color
        back_color -- background color
        symbol -- The player character symbol
        title -- What the player character is called when occupying a space.
        """
        super().__init__()
        Actor.__init__(self, fore_color, back_color, symbol, title)
        self._history: str = Character.gen_history()[0]
        self.steps = 0
        self.xp = 0
        self.indexed = 0
        self.augment = {"attack": False, "speed": False, "atime": 0, "stime": 0}
        self.damage = 5

    def gen_history() -> str:
        """Chooses randomly from lists to create a history and title for the character object."""

        history: str = random.choice(List2.historyList)
        title: str = random.choice(List2.characterTitle)

        return history, title

    

class Monster(GameCharacter, Actor):
    """This class creates and controls a monster object.
    
    Functions:
    __init__ -- Creates the character object
    move_actor -- Move the monster

    Inherits:
    Gamecharacter Class
    Actor Class
    """

    def __init__(self, fore_color, back_color, symbol, title) -> None:
        """Initializes a monster inherits from GameCharacter and Actor

        Arguments:
        self -- The monster
        fore_color -- text color
        back_color -- background color
        symbol -- The monster symbol
        title -- What the monster is called when occupying a space.
        """
        super().__init__()
        Actor.__init__(self, fore_color, back_color, symbol, title)
        self.xp_value: int = 0
        self.type: str = ""
        self._defense = random.randint(8, 15)
        self.key: bool = False
        self.runner = False

    def gen_monsters(dungeon, amount) -> None:
        """This generates a set number of monsters. In the future this will take more arguements for difficulty.

        Arguments:
        dungeon -- The board we place the player on.
        amount -- how many monsters we want to spawn.
        """
        stats = GameCharacter.gen_stats()
        
        key_count: int = 0

        #Check if a mimic or monster has the key
        if dungeon.board.mimic == True:
            mimic: Monster = Monster( "khaki1", "magenta2", "⍒", "Mimic")
            amount -= 1
            mimic._attack = 0
            mimic._defense = 14
            mimic._health = random.randint(8, 15)
            
            mimic.current_coord = dungeon.board.mimic_locate
            dungeon.board.monsters.append(mimic)
            
            dungeon.board.board, mimic = mimic.place_actor(dungeon.board.board, mimic = dungeon.board.mimic_locate)
        elif dungeon.board.monster_key == True:
            
            amount -= 1
        
        #60% chance of a passive slime monster
        if random.randint(1, 50) > 15:
            monster: Monster = Monster("blue", "grey5", "S", "Slime")
            amount -= 1
            dungeon.board.monsters.append(monster)
            monster.place_actor(dungeon.board.board)
            monster._health = 10000

        #randomly gen monsters or place key holders
        for i in range(amount):
            roll: int = MU.die_roller(1, 100)
            if roll < 34:
                monster: Monster = Monster("limegreen", "darkmagenta", "Z", "Zombie")
            else:
                monster: Monster = Monster("grey3", "darkmagenta", "R", "Rat")
            
            if dungeon.board.monster_key == True and key_count == 0:
                monster.key = True
                #monster.fc = "blue"
                key_count: int = 1
            
            if random.randint(0, 100) >= 40:
                item = random.choice(List2.items)
                monster.container = CC.Container("Mon", 2, 1, 10, 10)
                monster.container.add_item(CC.Item(item[0], item[1], item[2]))
                
                
            monster._attack = random.randint(1, 5)
            monster._defense = 14
            monster._health = random.randint(12, 20)

            dungeon.board.monsters.append(monster)
            monster.place_actor(dungeon.board.board)
    



def main():
    """Test main for this file
    
    """
    
    tom = Character("red", "blue", "@", "Player")
    
    tom.current_coord = [12,23]
    
    print(tom._attack, tom._defense, tom._health, tom.place_actor)

if __name__ == "__main__":
    main()