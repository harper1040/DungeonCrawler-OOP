"""
Joey Harper
2025-24-3
Hud class file
"""

import random
from time import time, strftime
import my_utilities as MU
import card_print
import player_class as PL
import List2
import container_assignment as CC

"""
    Create a player_window() method that displays the player stats.

"""
symbols: dict = {"side": "|", "side1": "〚", "side2": "〛", "side3": "∥", "bot": "≋", "top": "≛", "stone": "▓", "stone2":"▒"}
sys_messages: list = []
aux1_messages: list = []
aux2_messages: list = []

title: str = "░▒▓█ 𝓓𝓤𝓝𝓖𝓔𝓞𝓝 𝓒𝓡𝓐𝓦𝓛𝓔𝓡 █▓▒░"
sys_title: str = "░▒▓█►─═ 𝓢𝓨𝓢𝓣𝓔𝓜 ═─◄█▓▒░"
player_title: str = "░▒▓█►─═ 𝓟𝓛𝓐𝓨𝓔𝓡 ═─◄█▓▒░"
aux1_title = "░▒▓█►─═ 𝓐𝓤𝓧 1 ═─◄█▓▒░"
aux2_title = "░▒▓█►─═ 𝓐𝓤𝓧 2 ═─◄█▓▒░"
inv_title = "░▒▓█►─═ ℐ𝒩𝒱ℰ𝒩𝒯𝒪ℛ𝒴 ═─◄█▓▒░" #29
#title2: str = "░▒▓█►─═ 𝓓𝓤𝓝𝓖𝓔𝓞𝓝 𝓒𝓡𝓐𝓦𝓛𝓔𝓡 ═─◄█▓▒░"

class HUD():

    """Hud class used to generate all HUD items.
    
    Functions:
    draw_hud  -- Draws all the frames for the games HUD.
    player_window  -- Displays character info in the player pane.
    aux1_message  -- Displays message in the aux1 message pane.
    aux2_message  -- Displays message in the aux2 message pane.
    system_message  -- Displays message in the system message pane.
    """

    def draw_hud(card_color: str) -> None:
        """This function draws all the framework for the HUD.
        """

        color: str = getattr(MU.term, "gray90_on_grey55")
        if card_color["background"] == "indianred1":
            title_color: str = getattr(MU.term, "snow_on_dodgerblue4")
        else:
            title_color: str = getattr(MU.term, "aliceblue_on_webmaroon")
        background: str = getattr(MU.term, "on_" + card_color["inner_border"])
        
        for row in range(1, 54):
            print(background(" " * 105))

        
        #This loop draws the sides of the frames
        for row in range(54):
            MU.move_cursor(row, 0)
            print(color(symbols["stone2"]))
            if row < 44:
                MU.move_cursor(row, 58)
                print(color(symbols["stone2"]))
            MU.move_cursor(row, 105)
            print(color(symbols["stone2"]))


        #This loop draws the top and bottoms of the frames as well as name tags
        for col in range(106):
            #Top Bar
            if col >= 92:
                MU.move_cursor(0, col)
                print(color(symbols["top"]))
            elif col >= 70:
                MU.move_cursor(0, col)
                print(title_color(player_title[col - 70]))
            elif col >= 40:
                MU.move_cursor(0, col)
                print(color(symbols["top"]))
            elif col >= 15:
                MU.move_cursor(0, col)
                print(title_color(title[col - 15]))
            else:
                MU.move_cursor(0, col)
                print(color(symbols["top"]))

            #Draws Middle Bar under the dungeon map.
            if col >= 37:
                MU.move_cursor(44, col)
                print(color(symbols["bot"]))
            elif col >= 15:
                MU.move_cursor(44, col)
                print(title_color(sys_title[col - 15]))

            else:
                MU.move_cursor(44, col)
                print(color(symbols["bot"]))    

            #Draws Bottom most bar.
            MU.move_cursor(53, col)
            print(color(symbols["bot"]))

        #This loop draws the Top bar of the Aux 1
        for col in range(47):
            if col >= 34:
                MU.move_cursor(15, col + 58)
                print(color(symbols["bot"]))
            elif col >= 13:
                MU.move_cursor(15, col + 58)
                print(title_color(aux1_title[col - 13]))

            else:
                MU.move_cursor(15, col + 58)
                print(color(symbols["bot"]))

        #This loop draws the Top bar of the Aux 2
        for col in range(47):
            if col >= 34:
                MU.move_cursor(24, col + 58)
                print(color(symbols["bot"]))
            elif col >= 13:
                MU.move_cursor(24, col + 58)
                print(title_color(aux2_title[col - 13]))

            else:
                MU.move_cursor(24, col + 58)
                print(color(symbols["bot"]))

        #Draws top bar of Inventory
        for col in range(47):
            if col >= 34:
                MU.move_cursor(33, col + 58)
                print(color(symbols["bot"]))
            elif col >= 13:
                MU.move_cursor(33, col + 58)
                print(title_color(inv_title[col - 13]))

            else:
                MU.move_cursor(33, col + 58)
                print(color(symbols["bot"]))
            """MU.move_cursor(33, col + 58)
            print(color(symbols["bot"]))"""

        #This section draws the background of the frame cells
        color2: str = getattr(MU.term, "on_" + card_color["background"])
        start_row: int = 46
        start_col: int = 2

        #System Messages
        for clear in range(6):
            MU.move_cursor(start_row + clear, start_col)
            print(color2(" " * 102))
        
        #Aux 1
        for clear in range(6):
            MU.move_cursor(17 + clear, 60)
            print(color2(" " * 44))

        #Aux 2
        for clear in range(6):
            MU.move_cursor(26 + clear, 60)
            print(color2(" " * 44))

        #Inventory
        for clear in range(8):
            MU.move_cursor(35 + clear, 60)
            if clear == 0:
                print(color2("_" * 44))
            else:
                print(color2(" " * 44))

        #Player Stats
        for clear in range(12):
            MU.move_cursor(2 + clear, 60)
            print(color2(" " * 44))

    def color_validate(card_color, fore_color: str = "snow", back_color: str = "darkmagenta") -> str:
        """This function chooses a good color to use for foreground based on the cards color scheme.

        Arguments:

        card_color -- The color dictionary of the the players character card.
        fore_color -- Optional if you chose to use a different color
        back_color -- Optional if you chose to use a different color        
        """

        if card_color["background"] == "blanchedalmond":
            color: str = getattr(MU.term, "grey20_on_" + card_color["background"])
        elif card_color["background"] == "gray39":
            color: str = getattr(MU.term, "snow_on_" + card_color["background"])
        elif card_color:
            color: str = getattr(MU.term, "black_on_" + card_color["background"])
        else:
            color: str = getattr(MU.term, f"{fore_color}_on_{back_color}")

        return color

    def player_window(character: dict, steps = False, damage = False) -> None:
        """This is what prints the players stats for the moment it's just a reprint of the player card
        
        Arguments:
        character -- The character in the dungeon
        """

        start_row: int = 2
        start_col: int = 60
        fatime: int = 0
        fstime: int = 0

        timevar = 5

        color: str = HUD.color_validate(character._card[-1])

        if damage:
            MU.move_cursor(start_row + 1, start_col + 23)
            print(color(" " * 12))
        
        MU.move_cursor(start_row + 1, start_col + 1)
        print(color(f"{character._name} \t ♥ {character._health}"))
        MU.move_cursor(start_row + 3, start_col + 1)
        print(color(f"Att: {character._attack}   Def: {character._defense}   Steps: {character.steps}"))
        if character.augment["stime"] > 0 or character.augment["atime"] > 0:
            fatime: float = time() - character.augment["atime"]
            fstime: float = time() - character.augment["stime"]
            

            if fatime > 60:
                fatime = 0
            if fstime > 60:
                fstime = 0
        MU.move_cursor(start_row + 5, start_col + 1)
        print(color(f" " * 42))
        MU.move_cursor(start_row + 5, start_col + 1)
        print(color(f"Spd Boost Time: {int(fstime)}   Atk Boost Time: {int(fatime)}"))

        if steps:
            MU.move_cursor(5, 87)
            print(color(" " * 16))
            MU.move_cursor(5, 87)
            print(color(str(character.steps)))
        

    def inventory_window(card, container, first = True, world = None, world_color = None) -> None:
        """This controls the hud's inventory window that shows the player's stuff.

        
        """
         
        
        if world:
            color: str = getattr(MU.term, world_color[0] + "_on_" + world_color[1])

            for clear in range(11):
                MU.move_cursor(5 + clear, 43)
                if clear == 0:
                    print(color("_" * 50))
                else:
                    print(color(" " * 50))

        
        
            MU.move_cursor(5, 45)
            print(color("NAME"))
            MU.move_cursor(5, 73)
            print(color("WEIGHT"))
            MU.move_cursor(5, 82)
            print(color("SLOTS"))
            
            if first:
                items = CC.Container.trunc_name(container.itemsHeld)
                
                if items:
                    for i in range(len(items)):
                        item = items[i]
                        if i >= 10:
                            break
                        MU.move_cursor(6 + i, 43)
                        print(color(item.name)) #22 max Length needs handled
                        MU.move_cursor(6 + i, 70)
                        print(color(str(item.weight)))
                        MU.move_cursor(6 + i, 79)
                        print(color(str(item.slots)))

        else:
            color2: str = getattr(MU.term, "on_" + card["background"])

            for clear in range(8):
                MU.move_cursor(35 + clear, 60)
                if clear == 0:
                    print(color2("_" * 44))
                else:
                    print(color2(" " * 44))

            
            color = HUD.color_validate(card)
            MU.move_cursor(35, 68)
            print(color("NAME"))
            MU.move_cursor(35, 86)
            print(color("WEIGHT"))
            MU.move_cursor(35, 96)
            print(color("SLOTS"))
            
            if first:
                items = CC.Container.trunc_name(container.itemsHeld)
                
                if items:
                    for i in range(len(items)):
                        item = items[i]
                        if i >= 6:
                            break
                        MU.move_cursor(36 + i, 61)
                        print(color(item.name)) #22 max Length needs handled
                        MU.move_cursor(36 + i, 89)
                        print(color(str(item.weight)))
                        MU.move_cursor(36 + i, 98)
                        print(color(str(item.slots)))

        
    def aux1_message(message: str, fore_color: str = "snow", back_color: str = "darkmagenta", card: dict = None) -> None:
        """Truncates and prints to the first auxilary panel.
        
        Arguments:
        message -- The message to be printed in this case a list of them.
        fore_color -- the text color to use in this cell.
        back_color -- The background color to use in this cell.
        card -- Default is none but can be put in to match the cards backgrounds
        """

        color: str = HUD.color_validate(card, fore_color, back_color)

        start_row: int = 17
        start_col: int = 61

        if len(aux1_messages) == 6:
                aux1_messages.pop(0)
        aux1_messages.append([])
        aux1_messages[-1].append(message)
        aux1_messages[-1].append(color)

        for clear in range(6):
            MU.move_cursor(start_row + clear, start_col)
            print(color(" " * 43))
        for num in range(len(aux1_messages)):
            MU.move_cursor(start_row + num, start_col)
            if len(aux1_messages[num][0]) > 37:
                for i in range(37):
                    print(aux1_messages[num][1](aux1_messages[num][0][i]), end = "")
                print("...")
            else:
                print(aux1_messages[num][1](aux1_messages[num][0]))
        
    def aux2_message(message: str, fore_color: str = "snow", back_color: str = "darkmagenta", card: dict = None) -> None:
        """Truncates and prints to the second auxilary panel.
        
        Arguments:
        message -- The message to be printed in this case a list of them.
        fore_color -- the text color to use in this cell.
        back_color -- The background color to use in this cell.
        card -- Default is none but can be put in to match the cards backgrounds
        """

        color: str = HUD.color_validate(card, fore_color, back_color)

        start_row: int = 26
        start_col: int = 61
        

        if len(aux2_messages) == 6:
                aux2_messages.pop(0)
        aux2_messages.append([])
        aux2_messages[-1].append(message)
        aux2_messages[-1].append(color)

        for clear in range(6):
            MU.move_cursor(start_row + clear, start_col)
            print(color(" " * 43))
        for num in range(len(aux2_messages)):
            MU.move_cursor(start_row + num, start_col)
            if len(aux2_messages[num][0]) > 37:
                for i in range(37):
                    print(aux2_messages[num][1](aux2_messages[num][0][i]), end = "")
                print("...")
            else:
                print(aux2_messages[num][1](aux2_messages[num][0]))
            
    def system_message(message: str, fore_color: str = "snow", back_color: str = "darkmagenta", card: dict = None) -> None:
        """This function clears the system message field and prints the last 6 or less messages adding new messages to the master list.
        
        Arguments:
        message -- The message to be printed in this case a list of them.
        fore_color -- the text color to use in this cell.
        back_color -- The background color to use in this cell.
        card -- Default is none but can be put in to match the cards backgrounds
        """

        color: str = HUD.color_validate(card, fore_color, back_color)

        start_row: int = 46
        start_col: int = 3

        if len(sys_messages) == 6:
                sys_messages.pop(0)
        sys_messages.append([])
        sys_messages[-1].append(message)
        sys_messages[-1].append(color)

        for clear in range(6):
            MU.move_cursor(start_row + clear, start_col)
            print(color(" " * 101))
        for num in range(len(sys_messages)):
            MU.move_cursor(start_row + num, start_col)
            print(sys_messages[num][1](sys_messages[num][0]))

    def truncate_menu(text, row, col, color) -> int:
        """This takes in item names and shortens them so they fit in the hud windows.
        
        Arguments:
        text -- Text needing truncated
        row -- coordinate
        col -- coordinate
        color -- for text and background
        
        """
        
        to_print = ""
        count = 0
        increment = 2
        for char in text:
            if count == 33:
                to_print += char
                MU.move_cursor(row + increment, col)
                print(color(to_print))
                increment += 1
                count = 0
                to_print = ""
            else:
                to_print += char
                count += 1
        if len(to_print) < 33:
            MU.move_cursor(row + increment, col)
            print(color(to_print))
        
        return row + increment

    def world_menu(color, player, menu = None, location = None) -> None:
        """"This creates the menu that the player call up throughout the town area's.
        
        Arguments:
        color -- Text and back color
        player -- The character
        menu -- A number to index which menu to show.
        location -- Location the menu was called in to populate location variables such as name.
        
        """
        MU.clear()
        

        color_frame: str = getattr(MU.term, "gray90_on_grey55")
        color_player: str = getattr(MU.term, f"{player.fc}_on_" + player.bc)
        color: str = getattr(MU.term, f"{color[0]}_on_" + color[1])

        row: int = 2
        col: int = 2

        for rows in range(2, 40):
            for cols in range(2, 120):
                MU.move_cursor(rows, cols)
                if menu == None:
                    print(color_player(" "))
                else:
                    print(color(" "))


        for i in range(38):
            MU.move_cursor(row, 2)
            print(color_frame(symbols["stone2"]))
            MU.move_cursor(row, 120)
            print(color_frame(symbols["stone2"]))
            row += 1
            
        MU.move_cursor(2,2)
        for i in range(2):
            print(color_frame(symbols["top"] * 119))
            MU.move_cursor(40, 2)

        if menu == None:
            row = 4
            for i in range(35):
                MU.move_cursor(row, 40)
                print(color_frame(symbols["side3"]))
                row += 1
            MU.move_cursor(42, 2)
            print("Inputs: E - Leave, Letter to Select")
            HUD.world_fill(player)
        elif menu == 0:
            MU.move_cursor(4, 4)
            week = player.date['week']
            season = location.seasons[player.date['season'] - 1]
            for i in range(0, 8):
                if i == 0:
                    print(color(List2.menu_prompt[menu] % (location.repeats, location.name, location.manager)))
                elif i == 7:
                    print(color(List2.menu_prompt[menu + i] % (week, season)))
                else:
                    print(color(List2.menu_prompt[menu + i]))

        elif menu == 8:
            MU.move_cursor(4, 4)
            for i in range(6):
                if i == 0:
                    print(color(List2.menu_prompt[menu] % (location.gold, player.gold)))
                else:
                    print(color(List2.menu_prompt[menu + i]))

        elif menu == 14:
            MU.move_cursor(4, 4)
            print(color(List2.menu_prompt[menu] % (location.manager)))
            print(color(List2.menu_prompt[menu + 1] % (location.rate, location.capacity, location.stock)))

        elif menu == 16:
            MU.move_cursor(4, 4)
            for i in range(6):
                if i == 0:
                    print(color(List2.menu_prompt[menu] % (location.manager))+ "\n")
                else:
                    print(color(List2.menu_prompt[menu + i] ))

        if menu != None:
            MU.move_cursor(20, 4)
            print(color_frame(symbols["bot"] * 115))

        MU.move_cursor(22, 5)

    def world_fill(player) -> None:
        """"This fills in the player information in the world menu.
        
        Arguments:
        player -- The player's character.
        
        """
        color = getattr(MU.term, f"{player.fc}_on_" + player.bc)
        row = 5
        MU.move_cursor(row, 5)
        print(color(player._name))

        row = HUD.truncate_menu(player._history, row, 5, color)

        row += 2
        MU.move_cursor(row, 5)
        print(color(f"Health: {player._health}"))

        row += 2
        MU.move_cursor(row, 5)
        print(color(f"Attck: {player._attack}"))

        row += 2
        MU.move_cursor(row, 5)
        print(color(f"Defense: {player._defense}"))

        row += 2
        if player.augment["speed"]:
            MU.move_cursor(row, 5)
            print(color(f"Speed Boost: {int(time() - player.augment["stime"])}"))

        row += 2
        if player.augment["attack"]:
            MU.move_cursor(row, 5)
            print(color(f"Attack Boost: {int(time() - player.augment["atime"])}"))

        
        
        

        
        


def main() -> None:
    """The main for testing this page."""
    HUD.world_menu(["red", "blue"], "player")
    input()

if __name__ == "__main__":
    main()