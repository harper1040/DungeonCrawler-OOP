"""
Joey Harper 
2025-2-13
location classes
"""

#from typing import self
import random
from time import time
import player_class as PC
import my_utilities as MU
import dungeon1 as DU
import hud
import Lists
import container_assignment as CC
import sound_control as SC


class Location:
    """Creation and functions of a location object.
    
    Functions:
    __init__ -- Initializer
    enter -- This prints a message and provides a menu for the player.
    upkeep -- This runs the various upkeep functions when the player rests.
    add_location -- Adds a location to the list of locations
    """ 

    def __init__(self) -> None:
        """The class initialization function.

        Arguments:
        Self
        """

        self.manager: PC.Character = PC.Character.gen_name()
        self.fore_color: str = "white"
        self.back_color: str = "black"
        self.locations: list = []
        self.name: str = "Defaultington"

    def enter(self, player: PC.Character) -> None:
        """The enter function provides a greeting and or a menu of options on how to proceed.

        Arguments:
        Self
        player -- This is the character entering the location.
        """

        color: str = getattr(MU.term, self.fore_color + "_on_" + self.back_color)
        print(color("Hello, my name is " + self.manager))

    def upkeep(self):
        """Default upkeep function.

        Arguments:
        Self
        """

        pass

    def add_location(self, location) -> None:
        """Adds a location object to a list to keep track of these objects.

        Arguments:
        Self
        location -- The location object being added to the list.
        """

        self.locations.append(location)

class Town(Location):
    """Creation and functions of a town object which is a subclass of the location class
    
    Functions:
    __init__ -- Initializer
    enter -- This prints a message and provides a menu for the player.
    upkeep -- This runs the various upkeep functions when the player rests.

    Arguments:
    Location -- Takes in Location as the parent class.
    """ 

    def __init__(self) -> None:
        """This initializes a town object.
        
        Arguments:
        self 
        """

        super().__init__()
        self.fore_color: str = "rosybrown"
        self.back_color: str = "black"
        self.name: str = "Town McTownington"
        self.repeats: str = ""
        self.seasons: list = ["spring", "Summer", "Fall", "Winter"]

    def enter(self, player: PC.Character) -> None:
        """The enter function provides a greeting and or a menu of options on how to proceed.

        Arguments:
        Self
        player -- This is the character entering the location.
        """

        
        visit: int = 0
        color: str = getattr(MU.term, self.fore_color + "_on_" + self.back_color)
        seasons: list = ["spring", "Summer", "Fall", "Winter"]
        self.locations[2].board.board, player = player.place_actor(self.locations[2].board.board)
        

        while True:
            MU.clear()
            if visit > 0:
                self.repeats: str = "back"
            MU.move_cursor(0,0)
            self.locations[2].board.card = player._card[-1]
            hud.HUD.world_menu([self.fore_color, self.back_color], player, 0, self)
            
            option = MU.get_key()
            while True:
                match option:
                    case 113:
                
                        input("See Ya Next Time!")
                        MU.clear()
                        return True
                    case 101:
                        player.container.world_selector(self.locations[2].board, player, [self.fore_color, self.back_color])
                        break
                    case 108:
                        Lumbermill.enter(self.locations[1], player)
                        break
                    case 112:
                        rest: bool = Palace.enter(self.locations[0], player)
                        if rest:
                            Town.upkeep(self, player)
                        break
                    case 100:
                        Dungeon.enter(self.locations[2], player)
                        if player._health <= 0:
                            return True
                        if self.locations[2].board.boss == False:
                            self.locations[2] = Dungeon(40, 55)
                            reset_dungeon(player, self.locations[2])
                        break
                    case 115:
                        Shop.enter(self.locations[3], player)
                            
                        break
                    case _:
                        input("Please choose a valid option!")
                        break
                
            visit += 1
            
        #provide menu of locations and ask user which to enter call .enter() on selected location in a loop (Option to break loop)
        #Check for upkeep if so call town upkeep()
      
    def upkeep(self, player: PC.Character) -> None:
        """Town upkeep runs after the player rests and runs all other upkeeps to advance time or progress in other locations.

        Arguments:
        Self
        player -- This is the character at the location.
        """

        self.seasons: list = ["spring", "Summer", "Fall", "Winter"]
        player.upkeep()
        self.locations[1].upkeep(player)
        input(f"You have rested and progressed one week. It is now week {player.date["week"]} of {self.seasons[player.date["season"] - 1]}")
        #call .upkeep() on all locations and advance time
        pass
        

class Palace(Location):
    """Creation and functions of a palace object which is a subclass of the location class.
    
    Functions:
    __init__ -- Initializer
    enter -- This prints a message and provides a menu for the player.
    deposit -- This allows the player to deposit coin into their palace for safe keeping.
    withdraw -- This allows the player to take any coin they may have deposited.
    rest -- This sets the rest flag to True to run upkeep.

    Arguments:
    Location -- Takes in Location as the parent class.
    """ 

    def __init__(self, player: PC.Character) -> None:
        """The initializer for the palace location.

        Arguments:
        Self
        player -- This is the character entering the location.
        """
        super().__init__()
        self.fore_color: str = "yellow2"
        self.back_color: str = "grey31"
        self.name: str = "Home"
        self.manager: str = player._name
        self.gold: int = 0
        self.color = getattr(MU.term, self.fore_color + "_on_" + self.back_color)

    def enter(self, player: PC.Character) -> None:
        """The enter function provides a greeting and or a menu of options on how to proceed.

        Arguments:
        Self
        player -- This is the character entering the location.
        """

        while True:
            MU.clear()
            hud.HUD.world_menu([self.fore_color, self.back_color], player, 8, self)
            
            
            choice = MU.get_key()
            match choice:
                case 113:
                    break
                case 101:
                    player.container.world_selector(None, player, [self.fore_color, self.back_color])
                    break
                case 100:
                    Palace.deposit(self, player)
                case 119:
                    Palace.withdraw(self, player)
                case 114:
                    rest: bool = Palace.rest(self, player)
                    return rest
                case _:
                    print("Please choose a valid option!")

    def deposit(self, player: PC.Character) -> None:
        """This allows the player to deposit gold into their palace for safe keeping.

        Arguments:
        Self
        player -- This is the character at the location.
        """
        if player.gold == 0:
                input("\nOOh a moth flew out of your purse try and catch it!")
                return
        while True:
            MU.clear()
            print(self.color(f"Palace Balance {self.gold} Player Balance {player.gold}\n"))
            value: str = input(self.color("How much will you deposit? "))
            if value.upper() == "Q":
                return
            else:
                
                try:
                    value = int(value)
                    if value <= player.gold :
                        self.gold += value
                        player.gold -= value
                        break
                    else:
                        input("Please enter a valid ammount.")
                except TypeError:
                    input("Please enter a valid integer or quit!")
           

    def withdraw(self, player: PC.Character) -> None:
        """This allows the player to withdraw gold stored in their palace.

        Arguments:
        Self
        player -- This is the character at the location.
        """
        if self.gold == 0:
                input("\nYou don't seem to have a nest egg...")
                return
        while True:
            MU.clear()
            print(self.color(f"Palace Balance {self.gold} Player Balance {player.gold}\n"))
            value: int = input(self.color("How much will you take? "))
            if value.upper() == "Q":
                return
            try:
                value = int(value)
                if value <= self.gold:
                    player.gold += value
                    self.gold -= value
                    break
                else:
                    input("Please enter a valid amount!")
            except TypeError:
                input("Please enter a valid integer!")

    def rest(self, player: PC.Character) -> bool:
        """Rest triggers upkeeps to progress the game. This gives the player an option to rest and sets a flag to run the upkeep.

        Arguments:
        Self
        player -- This is the character at the location.
        """
        rest = input("Would you like to rest?(Y/N) ").upper()
        if rest == "Y":
            return True
        else:
            return False

class Lumbermill(Location):
    """Creation and functions of a lumbermill object which is a subclass of the location class
    
    Functions:
    __init__ -- Initializer
    enter -- This prints a message and provides a menu for the player.
    upkeep -- This runs math on the lumber processing when the player rests.

    Arguments:
    Location -- Takes in Location as the parent class.
    """ 

    def __init__(self, player: PC.Character) -> None:
        """Initialization function for the lumberyard.

        Arguments:
        Self
        player -- This is the character at the location.
        """

        super().__init__()
        self.fore_color: str = "lightgoldenrod"
        self.back_color: str = "tomato4"
        self.name: str = "I've Got Wood... Mill."
        self.manager: str = "Thomas Birtch"
        self.rate: int = 5
        self.stock: int = 0
        self.capacity: int = 50

    def enter(self, player: PC.Character) -> None:
        """The enter function provides a greeting and or a menu of options on how to proceed.

        Arguments:
        Self
        player -- This is the character entering the location.
        """

        color = getattr(MU.term, self.fore_color + "_on_" + self.back_color)
        MU.clear()
        hud.HUD.world_menu([self.fore_color, self.back_color], player, 14, self)
        match MU.get_key():
            case 113:
                return
    
    def upkeep(self, player: PC.Character) -> None:
        """This is trigger after a player rests and calculates wood numbers.

        Arguments:
        Self
        player -- This is the character at the location.
        """

        if self.stock < self.capacity:
            if self.stock + self.rate > self.capacity:
                self.stock = self.capacity
            else:
                self.stock += self.rate

class Shop(Location):
    """Creation and functions of a shop object which is a subclass of the location class
    
    Functions:
    __init__ -- Initializer
    enter -- This prints a message and provides a menu for the player.
    upkeep -- This runs math on the lumber processing when the player rests.

    Arguments:
    Location -- Takes in Location as the parent class.
    """ 

    def __init__(self) -> None:
        """Initialization function for the shop.

        Arguments:
        Self
        """
        super().__init__()
        self.fore_color: str = "darkolivegreen2"
        self.back_color: str = "midnightblue"
        self.manager: str = "Shopkeeper Roy"
        self.name: str = "The N Game Shop"

    def enter(self, player) -> None:
        """The enter function provides a greeting and or a menu of options on how to proceed.

        Arguments:
        Self
        player -- This is the character entering the location.
        """

        MU.clear()
        hud.HUD.world_menu([self.fore_color, self.back_color], player, 16, self)
        while True:
            match MU.get_key():

                case 49:
                    if not player.container.add_item(CC.Item("Health Potion", 2, 1)):
                        MU.move_cursor(12, 5)
                        print("You Don't have room for that.")
                    else:
                        MU.move_cursor(12, 5)
                        print("Thank you for your purchase")
                        player.gold -= 5
                        
                case 50:
                    if not player.container.add_item(CC.Item("Attack Potion", 2, 1)):
                        MU.move_cursor(12, 5)
                        print("You Don't have room for that.")
                    else:
                        MU.move_cursor(12, 5)
                        print("Thank you for your purchase")
                        player.gold -= 5
                case 51:
                    if not player.container.add_item(CC.Item("Speed Potion", 2, 1)):
                        MU.move_cursor(12, 5)
                        print("You Don't have room for that.")
                    else:
                        MU.move_cursor(12, 5)
                        print("Thank you for your purchase")
                        player.gold -= 5
                case 113:
                    break

    def upkeep(self, player):
        """This is trigger after a player rests and calculates wood numbers.

        Arguments:
        Self
        player -- This is the character at the location.
        """
        pass

class Dungeon(Location):
    """Creation and functions of a dungeon object which is a subclass of the location class
    
    Functions:
    __init__ -- Initializer
    enter -- This prints a message and provides a menu for the player.

    Arguments:
    Location -- Takes in Location as the parent class.
    """ 

    def __init__(self, height: int, width: int) -> None:
        """Dungeon Initialization function creates a dungeon.

        Arguments:
        Self
        player -- This is the character entering the location.
        """

        super().__init__()
        self.height: int = height
        self.width: int = width
        self.board: DU.Board = DU.Board(height, width)
        #self.board = self.board.make_room(5, 9 , 1, 1)
        self.board = self.board.create_rooms(6)
        self.board = self.board.place_gate()
        
    
    def enter(self, player: PC.Character) -> dict:
        """The enter function provides a greeting and or a menu of options on how to proceed.

        Arguments:
        Self
        player -- This is the character entering the location.
        """

        count = 0
        color: str = getattr(MU.term, self.fore_color + "_on_" + self.back_color)
        MU.move_cursor(22, 5)
        input(color(f"""Welcome to your dungeon experience!! Try not to die, eh? We don't have insurance..."""))
        
        SC.change_songs("dungeon")

        if len(self.board.monsters) < 5:
            PC.Monster.gen_monsters(self, 10)
        MU.clear()
        hud.HUD.draw_hud(player._card[-1])
        hud.HUD.inventory_window(player._card[-1], player.container)
        self.board.show_board()
        
        hud.HUD.player_window(player)
        
        MU.move_cursor(55, 0)
        print("Type an option: (M)System Message, (1) Aux1, (2) Aux2, (E) Inventory (enter to select, R to remove), (W,A,S,D) Move, (Q) To Leave ") 
        
        while True:
            
            
            while True:
                
                choice = MU.get_key()
                match choice:
                    case 113:
                        SC.change_songs("town")
                        for mon in self.board.monsters:
                            self.board.board[mon.current_coord[0]][mon.current_coord[1]] = DU.Tile(".", "lightpink1", "darkmagenta", True)
                        MU.clear()
                        return
                        
                    case 109:#M
                        hud.HUD.system_message(Lists.sys_messages[random.randint(0, len(Lists.sys_messages) - 1)], card = player._card[-1])
                    case 49:#1
                        hud.HUD.aux1_message(Lists.sys_messages[random.randint(0, len(Lists.sys_messages) - 1)], card = player._card[-1])
                    case 50:#2
                        hud.HUD.aux2_message(Lists.sys_messages[random.randint(0, len(Lists.sys_messages) - 1)], card = player._card[-1])
                    case 119:#W
                        if player.augment["speed"]:
                            if time() - player.augment["stime"] > 60:
                                player.augment["stime"] = 0
                                player.augment["speed"] = False
                                
                            for i in range(3):
                                player.move_actor(self.board, self.board.monsters, "UP")
                        else:
                            player.move_actor(self.board, self.board.monsters, "UP")
                        hud.HUD.player_window(player)
                        break
                    case 97:#A
                        if player.augment["speed"]:
                            if time() - player.augment["stime"] > 60:
                                player.augment["stime"] = 0
                                player.augment["speed"] = False
                            for i in range(3):
                                player.move_actor(self.board, self.board.monsters, "LEFT")
                        else:
                            player.move_actor(self.board, self.board.monsters, "LEFT")
                        hud.HUD.player_window(player)
                        break
                    case 115:#S
                        if player.augment["speed"]:
                            if time() - player.augment["stime"] > 60:
                                player.augment["stime"] = 0
                                player.augment["speed"] = False
                            for i in range(3):
                                player.move_actor(self.board, self.board.monsters, "DOWN")
                        else:
                            player.move_actor(self.board, self.board.monsters, "DOWN")
                        hud.HUD.player_window(player)
                        break
                    case 100:#D
                        if player.augment["speed"]:
                            if time() - player.augment["stime"] > 60:
                                player.augment["stime"] = 0
                                player.augment["speed"] = False
                            for i in range(3):
                                player.move_actor(self.board, self.board.monsters, "RIGHT")
                        else:
                            player.move_actor(self.board, self.board.monsters, "RIGHT")
                        hud.HUD.player_window(player)
                        break
                    case 99:#C
                        hud.HUD.aux2_message(f"{self.board.mimic}, {self.board.monster_key}", card = player._card[-1])
                        if self.board.monster_key == True: [hud.HUD.aux2_message(f"{x.title}", card = player._card[-1]) for x in self.board.monsters if x.key == True]
                    case 98:#B
                        player.crystal = True
                        player.container.add_item(CC.Item("Ancient Crystal", 1, 1))
                        
                    case 110:#N
                        hud.HUD.system_message(f"{self.board.item_locate}, {len(self.board.item_locate)} , {player.current_coord}", card = player._card[-1])
                    case 101:#E
                        try:
                            player.container.selector(player, self)
                        except:
                            pass
                    case 13:#enter
                        CC.Container.item_handle(self, player)
                        if not self.board.boss:
                            SC.change_songs("town")
                            MU.clear()
                            MU.move_cursor(20, 10)
                            input("Good Job You beat the boss!! What you want something? How about the knowledge that you did a good thing? How about that?")
                            return
                        
            
            if player._health <= 0:
                SC.change_songs("none")
                player: PC.Character = player.death(self.board)
                return player

            dead: list = [died.death(self.board, player._card[-1], player = player) for died in self.board.monsters if died._health <= 0]

            for mon in dead:
                if mon in self.board.monsters:
                    self.board.monsters.remove(mon)
            for mon in self.board.monsters:
                damaged: list = []
                damaged.append(player._health)
                mon.move_actor(self.board, player)
                if player._health < damaged[0]:
                    hud.HUD.player_window(player, damage = True)

            if len(self.board.monsters) < 5:
                count += 1
                if count >= 10:
                    PC.Monster.gen_monsters(self, 5)
                    count: int = 0

                        

def reset_dungeon(player, board) -> None:
    """This resets various variables when the boss is defeated to wipe and create a new dungeon.

        Arguments:
        
        player -- This is the character.
        board -- The new board.
        """
    blank_tile: DU.Tile = DU.Tile(".", "lightpink1", "darkmagenta", True)
    to_remove = None
    for i in range(len(player.container.itemsHeld)):
        if player.container.itemsHeld[i].name == "Ancient Crystal":
            to_remove = i
    if to_remove:
        player.container.itemsHeld.pop(to_remove)
    
    
    board.board.board, player = player.place_actor(board.board.board)
    board.board.board[board.board.gate[0]][board.board.gate[1]] = blank_tile
    
    board.board.board[board.board.crystal[0]][board.board.crystal[1]] = blank_tile
    player.crystal = None
    board.board.place_gate()

