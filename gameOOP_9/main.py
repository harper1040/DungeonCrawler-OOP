"""
Joey Harper
2025-2-13
Main file to the game.

"""

import random
import sys
import player_class as PC
import my_utilities as MU
import location_classes as LC
import container_assignment as CC
import sound_control as SC

def main() -> None:
    """The main function clears the screen and runs a loop to generate characters and cards for them to be displayed on. 
    Then displays those cards and aske the user to choose one.
    """
    sys.stdout.write("\x1b[8;50;130t")
    sys.stdout.flush()
    #os.system('mode 147, 60')
    SC.change_songs("cover")
    animate_counter = 5
    MU.clear()
    PC.splash_screen()
    
    while True:    
        color_list: list = ["reds", "blues", "greens", "whites", "blacks"]
        color_choice: str = random.choice(color_list)
        character_1: PC.GameCharacter = PC.Character("lightpink1", "darkslategrey", "@", "Character")
        stats = PC.GameCharacter.gen_stats()
        character_1._attack = stats[0]
        character_1._defense = stats[1]
        character_1._health = stats[2]
        character_1.max_attack = stats[0]
        character_1.max_defense = stats[1]
        character_1.max_health = stats[2]
        #character_1.gen_stats()
        card: list = PC.card_print.draw_card(color_choice)
        card: list = character_1.populate_card(card, color_choice)
        
        
        
        MU.clear()
        card: list = PC.card_print.display_card(card)
        if animate_counter < 2:
            PC.card_print.slide_animate()
            card: list = PC.card_print.animate_card(card)
            animate_counter += 1
        else:
            card: list = PC.card_print.display_card(card)
        
        print(f"\n{character_1._name} \n")
        print(character_1._history + "\n")
        print(f"With {character_1._attack} attack {character_1._defense} defense and {character_1._health} health.")
        
        player_check: str = input("""\n
            Would you like to keep this card? (Y)
            Would you like to draw another card? (any key...except Y or Q)
            Would you like to quit? (Q)
                            """).upper()

        if player_check == "Y":
            MU.clear()
            card: list = PC.card_print.display_card(card)
            character_1.new_character(card)
            SC.change_songs("town")
            break
        elif player_check == "Q":
            MU.clear()
            MU.move_cursor(15, 45)
            input("YOU MAKE ME SAD! GOODBYE!")
            MU.clear()
            sys.exit(0)
        else:
            MU.clear()

    while True:
        character_1.container = CC.Container("Sachel", 2, 2, 30, 10)
        #character_1.container.add_item(CC.Item("Middle Finger Sculpture", 3, 2))
        for i in range(3):
            character_1.container.add_item((CC.Item("Health Potion", 2, 1)))
        character_1.container.add_item((CC.Item("Attack Potion", 2, 1)))
        character_1.container.add_item((CC.Item("Speed Potion", 2, 1)))
        
        town: LC.Town = LC.Town()
        town.add_location(LC.Palace(character_1))
        town.add_location(LC.Lumbermill(character_1))
        town.add_location(LC.Dungeon(40, 55))
        town.add_location(LC.Shop())
        leave = town.enter(character_1)
        if leave:
            sys.exit(0)

main()