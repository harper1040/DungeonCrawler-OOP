"""
Joey Harper
2025-1-30
Container Class
"""
import uuid
from time import time
import my_utilities as MU
import hud
import dungeon1 as DG
import sound_control as SC
import pygame_boss as PB

FRAME_PARTS = ["✹","︽","︾","﹎","﹊","⑇","︴","﹏","﹋","﹌", "⌥", "⍊", "⍑", "⋙", "⋘"]

class Item:
    """Creates and controls item objects
    
    Functions:
    __init__ -- Initializes a item object
    __str__ -- String method for a clean print out of an item
    """

    def __init__(self,name: str, wt: int, slots: int, stat: int = None):
        """Initializes item objects

        :param name = Name of the item
        :param weight = Weight of the item
        :param slots = Number of slots item takes up
        """
        self.id: int= uuid.uuid4() #Generate unique UUID for all items
        self.name: str = name
        self.weight: int = wt
        self.slots: int = slots

    def __str__(self) -> str:
        """String function to print out item information."""
        
        returnString: str = ""
        returnString += "Name: "+self.name+"\t\t"
        returnString += "Weight: "+str(self.weight)+"\t"
        returnString += "Slots: "+str(self.slots)
        return returnString

class Container(Item):  
    """Creation and functions of a container object which is a subclass of the item class
    
    Functions:
    __init__ -- Initializer
    __str__ -- String method for a clean print out of a container
    add_item -- Adds items to a container
    remove_item -- Removes an item in a container from that container
    manage_items -- Allows the user to view a container and choose to remove items

    Arguments:
    Item -- Takes in the item class as container is a subclass of item.
    """ 

    def __init__(self, name: str, wt: int, slots: int, mw: int, ms: int):
        """Initializes a container object which is a child of the item class

            :param name = Name of the container
            :param weight = Weight of the container
            :param slots = Number of slots container takes up
            :param max weight = Maximum weight the container can hold
            :param max slots = Maximum number of slots the container has
        """
        super().__init__(name,wt,slots)
        """Super function initialize the parent classes parameters"""

        self.maxWeight: int = mw        
        self.maxSlots: int = ms
        self.weightUsed: int = 0
        self.slotsUsed: int = 0
        self.itemsHeld: list = []
       
    def add_item(self, item: Item) -> bool:
        """Verify there is room in the container and if so add the item to the container if not return False.

            item = The item object to be added to a container.
        """
        if item.slots > self.maxSlots - self.slotsUsed:
            return False
        else:
            if item.weight > self.maxWeight - self.weightUsed:
                return False
            else:
                self.weightUsed += item.weight
                self.slotsUsed += item.slots
                self.itemsHeld.append(item)
                return True

    def remove_item(self, index: int) -> Item:
        """Checks for the item to exist and pops it off the list.

            index = The index of an item you want to remove from a container
        """
        #item = index - 1
        
        if self.itemsHeld[index]:
            self.weightUsed -= self.itemsHeld[index].weight
            self.slotsUsed -= self.itemsHeld[index].slots
            return self.itemsHeld.pop(index)

    def use_item(self, index: int, board: list= None, player: dict = None,  drop: bool = False, locate: list = [], cud = "dungeon") -> None:
        """Allows the player to use their items.
        
        Arguments:
        self -- The container the item is in.
        index -- Index of the item in the container.
        board -- The board
        player -- The character
        drop -- True means an item was dropped by a monster.
        locate -- The coordinates of the monster when it died and where the item will be.
        cud -- hud was taken but this is to see where the item was used for feedback printing purposes.
        
        """
        item = DG.Tile("ⁱ", "snow", "grey3", True)
        if board and drop:
            board.items.append(self.itemsHeld[0])
            if [0, 0] in board.item_locate:
                board.item_locate = [locate]
            else:
                board.item_locate.append(locate)
            board.board[locate[0]][locate[1]] = item
            board.board[locate[0]][locate[1]].display_tile([locate[0] + 2, locate[1] + 2])
        else:
            used_item = self.itemsHeld[index]
            match used_item.name:
                case "Health Potion":
                    if (player.max_health - player._health) < 5:
                        player._health = player.max_health
                    else:
                        player._health += 5
                        if cud == "dungeon":
                            hud.HUD.aux2_message("+ 5 health", card = player._card[-1])
                        elif cud == "world":
                            return "Health"
                case "Attack Potion":
                    player.augment["attack"] = True
                    player.augment["atime"] = time()
                    if cud == "dungeon":
                        hud.HUD.aux2_message("Attack Boost", card = player._card[-1])
                    elif cud == "world":
                        return "Attack"
                    
                case "Speed Potion":
                    player.augment["speed"] = True
                    player.augment["stime"] = time()
                    if cud == "dungeon":
                        hud.HUD.aux2_message("Speed Boost", card = player._card[-1])
                    elif cud == "world":
                        return "Speed"
                    
                case "Rusty Armor":
                    player.equipped["Rusty Armor"] = True
                    return
                
                case "Small Sword":
                    player.equipped["Small Sword"] = True
                    return
            

    def item_handle(board, player) -> None:
        """Called whenever something needs to happen with or because of the gate.

        Arguments:
        self -- The board.
        player -- The player character.
        """
        #This code handles whether or not you pick up an item.

        if player.current_coord[0] == board.board.crystal[0] and player.current_coord[1] == board.board.crystal[1]:

            if player.crystal == None:
                hud.HUD.system_message("You found an ancient crystal! I wonder what it's for?", card = player._card[-1])
                SC.sound_effect("key")
                if not player.container.add_item(Item("Ancient Crystal", 1, 1)):
                    hud.HUD.system_message("You cannont carry this many items!", card = player._card[-1])
                player.crystal = "crystal"
                
        elif player.current_coord in board.board.item_locate:
            for i in range(0, len(board.board.item_locate)):
                if player.current_coord == board.board.item_locate[i]:
                    hud.HUD.system_message(f"Hey it's {board.board.items[i].name}!", card = player._card[-1])
                    if not player.container.add_item(board.board.items[i]):
                        hud.HUD.system_message("You cannot carry this many items!", card = player._card[-1])
                    else:
                        board.board.items.pop(i)
                        if len(board.board.item_locate) == 1:
                            board.board.item_locate = [[0, 0]]
                        else:
                            board.board.item_locate.pop(i)
                        break
                        
                    
        else:
            hud.HUD.system_message("Nothing here!", card = player._card[-1])
                    
        hud.HUD.inventory_window(player._card[-1], player.container)            


        #If you walk over a gate or crystal this code sends system message to inform you what's what.
            
        if player.current_coord[0] == board.board.gate[0] and player.current_coord[1] == board.board.gate[1]:
            if player.crystal == None:
                hud.HUD.system_message("Looks like an ancient gate of some kind...", card = player._card[-1])
            else:
                hud.HUD.system_message("You opened the portal OMG you went through and found a boss battle! Hmm...", card = player._card[-1])
                if player.crystal:
                    #hud.HUD.system_message(f"{player.container.itemsHeld[i].name}", card = player._card[-1])
                    
                    SC.sound_effect("portal")
                    PB.main(board, player)



    def manage_items(self) -> int:
        """Lets player choose an item to delete or move or whatever options are available for items."""
        
        INFO_TEXT = "Select an item with your up and down arrow keys and hit enter, or Q to quit. \n\n"
        Container.draw_frame(self)  
        Container.draw_screen(self)

        row: int = 6
        col: int = 13
        index: int = 0


        while True:
            
            key: int = MU.get_key()
            if key == 113:
                MU.clear()
                return "No Selection"
            elif key == 72: #72 up, 80 down, 13 enter, 113 Q
                if index == 0:
                    pass
                else:
                    Container.draw_frame(self)
                    #MU.clear()
                    #print(INFO_TEXT)
                    count: int = 1
                    index_math: int = index - 1
                    for i in self.itemsHeld:
                        MU.move_cursor(row, col)
                        if index_math < 0:
                            print(str(count) + ": " + getattr(MU.term, "gray3_on_mediumorchid4")+ str(self.itemsHeld[0]) + MU.term.normal)
                        elif i == self.itemsHeld[index_math]:
                            print(str(count) + ": " + getattr(MU.term, "gray3_on_mediumorchid4")+ str(self.itemsHeld[index_math]) + MU.term.normal)
                        else:
                            print(f"{count}: {i}")
                        count += 1
                        row += 1
                    index -= 1
                    row: int = 6

                    
            elif key == 80:
                if index == len(self.itemsHeld) - 1:
                    pass
                else:
                    
                    Container.draw_frame(self)
                    #MU.clear()
                    #print(INFO_TEXT)
                    count: int = 1
                    for i in self.itemsHeld:
                        MU.move_cursor(row, col)
                        if i == self.itemsHeld[index + 1]:
                            print(str(count) + ": " + getattr(MU.term, "gray3_on_mediumorchid4")+ str(self.itemsHeld[(index + 1)]) + MU.term.normal)
                        else:
                            print(f"{count}: {i}")
                        count += 1
                        row += 1
                    index += 1
                    row: int = 6

                    
                    
            elif key == 13:
                MU.clear()
                return index
            
    def draw_screen(self) -> None:
        """Draws the item selection menu.
        
        Arguments:
        self -- container to display.
        """


        row: int = 6
        col: int = 13
        count: int = 1
        MU.move_cursor(row, col)

    
        for i in self.itemsHeld:
            MU.move_cursor(row, col)
            if i == self.itemsHeld[0]:
                print(str(count) + ": " + getattr(MU.term, "gray3_on_mediumorchid4")+ str(self.itemsHeld[0]) + MU.term.normal)
            else:
                print(f"{count}: {self.itemsHeld[count - 1]}")
            count += 1
            row += 1

    def draw_frame(self) -> None:
        """Draws the frame around the item selection menu.
        
        Arguments:
        self
        """

        MU.clear()
        INFO_TEXT: str = "Select an item with your up and down arrow keys and hit enter, or Q to quit."
        MU.move_cursor(0, 8)
        print(INFO_TEXT + "\n\n")

        row: int = 3
        col: int = 87
        f_col: int = 8

        MU.move_cursor(row, f_col)
        print(FRAME_PARTS[13] * 81)
        row += 1
        MU.move_cursor(row, f_col)
        print(FRAME_PARTS[0] + FRAME_PARTS[12] * 78 + FRAME_PARTS[0])
        row += 1
        
        for i in range(len(self.itemsHeld) + 5):
            MU.move_cursor(row, f_col)
            print(FRAME_PARTS[5], end = "")
            MU.move_cursor(row, col)
            print(FRAME_PARTS[5])
            row += 1
        MU.move_cursor(row, f_col)
        print(FRAME_PARTS[0] + FRAME_PARTS[11] * 78 + FRAME_PARTS[0])
        row +=1
        MU.move_cursor(row, f_col)
        print(FRAME_PARTS[13] * 81)

        
                
        

    def trunc_name(self) -> list:
        """Cuts down the str so it fits in the window
        
        """
        
        trunc_items = []
        filler = ""
        for item in self:
            trunc_items.append(item)
            if len(item.name) > 22:
                for i in range(19):
                    filler += item.name[i]
                filler += "..."
                trunc_items[-1].name = filler
        return trunc_items
    
    def redraw_menu(self, base_color, sel_color, index, row, col, direction, world = False) -> None:
        """redraws the menu as it scrolls. Updates layout to move past the visible 7 slots.
        
        """
        if world:
            try:
                var = self[index].name
            except IndexError:
                return
            MU.move_cursor(row, col[0])
            print(base_color(" " * 50))
        else:

            MU.move_cursor(row, col[0])
            print(base_color(" " * 44))

        MU.move_cursor(row, col[1])
        print(base_color(self[index].name))
        MU.move_cursor(row, col[2])
        print(base_color(str(self[index].weight)))
        MU.move_cursor(row, col[3])
        print(base_color(str(self[index].slots)))

        if direction == "UP":
            try:
                if world:
                    MU.move_cursor(row - 1, col[0])
                    print(sel_color(" " * 50))
                else:

                    MU.move_cursor(row - 1, col[0])
                    print(sel_color(" " * 44))

                MU.move_cursor(row - 1, col[1])
                print(sel_color(self[index - 1].name))
                MU.move_cursor(row - 1, col[2])
                print(sel_color(str(self[index - 1].weight)))
                MU.move_cursor(row - 1, col[3])
                print(sel_color(str(self[index - 1].slots)))
            except:
                pass
        else:
            try:
                if world:
                    MU.move_cursor(row + 1, col[0])
                    print(sel_color(" " * 50))
                else:
                    MU.move_cursor(row + 1, col[0])
                    print(sel_color(" " * 44))

                MU.move_cursor(row + 1, col[1])
                print(sel_color(self[index + 1].name))
                MU.move_cursor(row + 1, col[2])
                print(sel_color(str(self[index + 1].weight)))
                MU.move_cursor(row + 1, col[3])
                print(sel_color(str(self[index + 1].slots)))
            except:
                pass

    def scroll(self, base_color, sel_color, card, col, index, list_length, direction, world = None) -> None:
        """Draws the highlighted selector in the inventory pane
        
        Arguments:
        self -- Container to scroll throug
        base_color -- Main color
        sel_color -- Color of the selector
        card -- Player card
        col -- Start col
        index -- Index of the item in the container
        list_length -- Length of the list
        direction -- Whether your moving up or down.
        """
        start_index = index - 5
        second_index = index - 1

        if world:
            if direction == "DOWN":
                if index == list_length - 1:
                    pass
                else:
                    hud.HUD.inventory_window(card, self, False)

                    for rows in range(7):
                        MU.move_cursor(5 + rows, col[1])
                        print(base_color(self[start_index + rows].name))
                        MU.move_cursor(5 + rows, col[2])
                        print(base_color(str(self[start_index + rows].weight)))
                        MU.move_cursor(5 + rows, col[3])
                        print(base_color(str(self[start_index + rows].slots)))

                    MU.move_cursor(16, col[0])
                    print(sel_color(" " * 44))

                    MU.move_cursor(16, col[1])
                    print(sel_color(self[index + 1].name))
                    MU.move_cursor(16, col[2])
                    print(sel_color(str(self[index + 1].weight)))
                    MU.move_cursor(16, col[3])
                    print(sel_color(str(self[index + 1].slots)))

            else:
                if index == 0:
                    pass
                else:
                    hud.HUD.inventory_window(card, self, False)

                    for rows in range(7):
                        MU.move_cursor(5 + rows, col[1])
                        print(base_color(self[second_index + rows].name))
                        MU.move_cursor(5 + rows, col[2])
                        print(base_color(str(self[second_index + rows].weight)))
                        MU.move_cursor(5 + rows, col[3])
                        print(base_color(str(self[second_index + rows].slots)))

                    MU.move_cursor(5, col[0])
                    print(sel_color(" " * 44))

                    MU.move_cursor(5, col[1])
                    print(sel_color(self[index - 1].name))
                    MU.move_cursor(5, col[2])
                    print(sel_color(str(self[index - 1].weight)))
                    MU.move_cursor(5, col[3])
                    print(sel_color(str(self[index - 1].slots)))






        else:
            if direction == "DOWN":
                if index == list_length - 1:
                    pass
                else:
                    hud.HUD.inventory_window(card, self, False)

                    for rows in range(7):
                        MU.move_cursor(36 + rows, col[1])
                        print(base_color(self[start_index + rows].name))
                        MU.move_cursor(36 + rows, col[2])
                        print(base_color(str(self[start_index + rows].weight)))
                        MU.move_cursor(36 + rows, col[3])
                        print(base_color(str(self[start_index + rows].slots)))

                    MU.move_cursor(42, col[0])
                    print(sel_color(" " * 44))

                    MU.move_cursor(42, col[1])
                    print(sel_color(self[index + 1].name))
                    MU.move_cursor(42, col[2])
                    print(sel_color(str(self[index + 1].weight)))
                    MU.move_cursor(42, col[3])
                    print(sel_color(str(self[index + 1].slots)))
            else:
                if index == 0:
                    pass
                else:
                    hud.HUD.inventory_window(card, self, False)

                    for rows in range(7):
                        MU.move_cursor(36 + rows, col[1])
                        print(base_color(self[second_index + rows].name))
                        MU.move_cursor(36 + rows, col[2])
                        print(base_color(str(self[second_index + rows].weight)))
                        MU.move_cursor(36 + rows, col[3])
                        print(base_color(str(self[second_index + rows].slots)))

                    MU.move_cursor(36, col[0])
                    print(sel_color(" " * 44))

                    MU.move_cursor(36, col[1])
                    print(sel_color(self[index - 1].name))
                    MU.move_cursor(36, col[2])
                    print(sel_color(str(self[index - 1].weight)))
                    MU.move_cursor(36, col[3])
                    print(sel_color(str(self[index - 1].slots)))
    
    def selector(self, player, board, second = False) -> None:
        """Draws the item selection menu.
        
        Arguments:
        self -- container to display.
        card -- To grab color profile.
        """

        start_row: int = 36
        row: int = 36
        col: list = [60, 61, 89, 98]

        index: int = 0

        list_length: int = len(self.itemsHeld)

        color: str = hud.HUD.color_validate(player._card[-1])

        select_color: str = getattr(MU.term, "snow_on_slateblue2")

        items = Container.trunc_name(self.itemsHeld)

        MU.move_cursor(row, col[0])
        print(select_color(" " * 44))

        if second:
            pass
        else:
            MU.move_cursor(row, col[1])
            print(select_color(items[index].name))
            MU.move_cursor(row, col[2])
            print(select_color(str(items[index].weight)))
            MU.move_cursor(row, col[3])
            print(select_color(str(items[index].slots)))

        while True:

            match MU.get_key():
                case 119:
                    if row == 36:
                        
                        
                        Container.scroll(items, color, select_color, player._card[-1], col, index, list_length, "UP")
                        if index == 0: 
                            pass
                        else:
                            index -= 1
                    else:

                        Container.redraw_menu(items, color, select_color, index, row, col, "UP")
                        
                        row -= 1
                        index -= 1

                    #hud.HUD.aux2_message(f"{row}, {index}", card = card)

                case 115:
                    if row >= 42:
                        
                        
                        Container.scroll(items, color, select_color, player._card[-1], col, index, list_length, "DOWN")
                        if index == len(items) - 1:
                            pass
                        else:
                            index += 1
                    else:
                        
                        Container.redraw_menu(items, color, select_color, index, row, col, "DOWN")

                        row += 1
                        index += 1

                        
                    #hud.HUD.aux2_message(f"{row}, {index}", card = card)
                
                case 101:
                    hud.HUD.inventory_window(player._card[-1], self)
                    break

                case 13:
                    #This is where we choose to use or discard our items.
                    match items[index].name:
                        case "Ancient Crystal":
                            hud.HUD.aux2_message("Such a strange old crystal...", card = player._card[-1])
                            
                        case _:
                            hud.HUD.aux2_message(f"You used {items[index].name}.", card = player._card[-1])
                            self.use_item(index, board, player = player)
                            player.container.remove_item(index)
                            hud.HUD.inventory_window(player._card[-1], self)
                            hud.HUD.player_window(player, damage = True)
                            break
                
                case 114:
                    hud.HUD.aux2_message(f"Remove {items[index].name}?", card = player._card[-1])
                    if MU.get_key() == 121:
                        
                        hud.HUD.aux2_message(f"{items[index].name} removed", card = player._card[-1])
                        player.container.remove_item(index)
                        hud.HUD.inventory_window(player._card[-1], self)
                    break

                             

    
    
    def world_selector(self, board, player, color) -> None:
        """Provides a menu and option for the player to make an input to use items.
        
        Arguments:
        self -- The container
        board -- The board
        player -- The character
        color -- Text and back color
        
        """

        #hud.HUD.world_menu(color, player)
        colors = getattr(MU.term, f"{player.fc}_on_{player.bc}")
        row = 5
        col = 43
        number = 0
        letters = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L"]

        

        while True:
            hud.HUD.world_menu(color, player)
            index = None

            for rows in range(20):
                for cols in range(50):
                    MU.move_cursor(row + rows, col + cols)
                    print(colors(" "))

            for i in player.container.itemsHeld:
                MU.move_cursor(row, col)
                print(colors(f"{letters[number]}: {i.name}"))
                row += 1
                number += 1
            row = 5
            number = 0

            match MU.get_key():
                #97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108
                case 97:
                    index = 0
                case 98:
                    index = 1
                case 99:
                    index = 2
                case 100:
                    index = 3
                case 101:
                    return
                case 102:
                    index = 4
                case 103:
                    index = 5
                case 104:
                    index = 6
                case 105:
                    index = 7
                case 106:
                    index = 8
                case 107:
                    index = 9
                case 108:
                    index = 10
                case _:
                    continue
            if index:
                try:
                    var = player.container.itemsHeld[index]
                    message = player.container.use_item(index, board, player, cud = "world")
                    player.container.remove_item(index)

                    MU.move_cursor(30, 45)
                    print(colors(" ") * 50)
                    MU.move_cursor(30, 45)
                    print(colors(f"{message} Boosted"))
                except IndexError:
                    MU.move_cursor(30, 45)
                    print(colors(" ") * 50)
                    MU.move_cursor(30, 45)
                    print(colors("Choose a letter on the list please."))
            input("")
            
                
            

def main():
    """This is the main function for the container file used to run the functions for the item and container classes."""

    con: Container = Container("Box",2,4,20,10)
    if not con.add_item(Item("Unmatched Shoe",3,2)):
        print("Too big or heavy for container")
    if not con.add_item(Item("Dead Rat",1,1)):
        print("Too big or heavy for container")
    if not con.add_item(Item("Space Station",1000000,10000000)):
        print("'Space Station' was too big or heavy for container \n")
    if not con.add_item(Item("McGuffin",4,2)):
        print("Too big or heavy for container")
    if not con.add_item(Item("Match Book",1,1)):
        print("Too big or heavy for container")
    if not con.add_item(Item("Plumbus",4,3)):
        print("Too big or heavy for container")
    choice: int = con.manage_items()
    if choice == "No Selection":
        input("You chose to quit!")
    else:
        input("You chose item number " + str(choice + 1))
        con.remove_item(choice)
    choice = con.manage_items()


if __name__ == "__main__":
    main()


