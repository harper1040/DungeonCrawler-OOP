"""
Joey Harper
2025-5-8
Final boss fight in pygame
"""

import pygame
import random
import math
from time import time
import sys
import os

import pygame.freetype

def start(board = None, character = None, stand_alone = False) -> None:
    """This allows the player to gain focus on the window to fight the boss and explains gameplay.

        Arguments:
        
        board -- The board we place the player on.
        character -- The players character.
        stand-alone -- Whether or not the file is loaded by itself or from another file.
        """
    pygame.init()
    height = 600
    width = 900
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Dungeon Crawler")
    #os.system("wmctrl -r :ACTIVE: -b toggle,above")
    

    running = True
    game_font = pygame.freetype.Font("BungeeSpice-Regular.ttf", 24)
    
    
    while running:
        screen.fill("white")
        game_font.render_to(screen, (50,200), "Prepare for battle W,A,S,D to move ", "red")
        game_font.render_to(screen, (50,250), "and space or mouse left to attack. Get close but keep your ", "red")
        game_font.render_to(screen, (50,300), "distance. Be quick don't die! press SPACE to begin.", "red")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if stand_alone:
                    running = False
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                
                running = False
                game(board, character, stand_alone)
        try:       
            pygame.display.update()
            pygame.display.flip()
        except:
             pass
        
    #pygame.quit()



def game(board = None, character = None, stand_alone = False) -> None:
    """This is the main game that creates the player and boss sprites to battle.

        Arguments:
        
        board -- The board we place the player on.
        character -- The players character.
        stand-alone -- Whether or not the file is loaded by itself or from another file.
        """

    pygame.init()
    height = 600
    width = 900
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Dungeon Crawler")
    #os.system("wmctrl -r :ACTIVE: -b toggle,above")
    

    running = True
    b_start_x = 700
    b_start_y = 200
    p_start_x = 350
    p_start_y = 400
    bp_speed = 6
    boss_speed = 3
    game_font = pygame.freetype.Font("BungeeSpice-Regular.ttf", 24)



    background = pygame.image.load("img/Background.gif").convert()

    def damage_calc(attacker, defender) -> None:
        """This calculates the damage dealt to a defender.
        
        Arguments:
        attacker -- The person innitiating the attack.
        defender -- The person getting attacked
        
        """

        damage = attacker.damage
        if defender.title == "character":
            if defender.equipped["Rusty Armor"]:
                damage -= 3
            defender._health -= damage
            
        else:
            if attacker.augment["attack"]:
                damage += 3
            if attacker.equipped["Small Sword"]:
                damage += 2
            defender._health -= damage
            
                    
                
       
        

    class Player(pygame.sprite.Sprite):
        """This class creates and controls players sprite.
    
            Functions:
            __init__ -- Creates the character object
            player_rotate -- Gets player sprite rotation
            input -- Get player input. 
            is_attacking -- Attack cooldown
            Movement -- moves the players sprite 
            update -- Runs all the functions to move player.
            """

        def __init__(self) -> None:
            """Initialization function for the player.

            Arguments:
            Self
            
            """

            super().__init__()
            self.pos = pygame.math.Vector2(p_start_x, p_start_y)
            self.image = pygame.transform.rotozoom(pygame.image.load("img/player.png").convert_alpha(), 0, .2)
            self.base_image = self.image
            self.hitbox_rect = self.base_image.get_rect(center= self.pos)
            self.rect = self.hitbox_rect.copy()
            self.attack_cooldown = 0
            self.speed = bp_speed
            self.range = 100
            self.attack = False

        def player_rotate(self) -> None:
            """Rotates the player sprite to face the mouse cursor."""
            self.mouse_coord = pygame.mouse.get_pos()
            self.x_mouse_change = (self.mouse_coord[0] - self.hitbox_rect.centerx)
            self.y_mouse_change = (self.mouse_coord[1] - self.hitbox_rect.centery)
            self.angle = math.degrees(math.atan2(self.y_mouse_change, self.x_mouse_change))
            self.image = pygame.transform.rotate(self.base_image, -self.angle)
            self.rect = self.image.get_rect(center = self.hitbox_rect.center)
            
            
        
        def input(self) -> None:
            """Get's the movement input from the player."""
            if character.augment["speed"]:
                self.speed += 1
            self.velocity_x = 0
            self.velocity_y = 0

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.velocity_y = -self.speed
            if keys[pygame.K_s]:
                self.velocity_y = self.speed
            if keys[pygame.K_d]:
                self.velocity_x = self.speed
            if keys[pygame.K_a]:
                self.velocity_x = -self.speed

            if self.velocity_x != 0 and self.velocity_y != 0:
                self.velocity_x /= math.sqrt(2)
                self.velocity_y /= math.sqrt(2)

            if keys[pygame.K_SPACE] or pygame.mouse.get_pressed() == (1, 0, 0):
                if self.hitbox_rect.colliderect(boss.hitbox_rect):
                    self.attack = True
                    self.is_attacking()
            else:
                self.attack = False

        def is_attacking(self) -> None:
            """Checks attack cooldown."""
            if self.attack_cooldown == 0:
                self.attack_cooldown = 20
                damage_calc(character, boss)
                """sword_pos = self.pos
                self.sword = Sword(sword_pos[0], sword_pos[1], self.angle)
                sword_group.add(self.sword)
                all_sprites.add(self.sword)"""

        def movement(self) -> None:
           """Moves the character based on movement speed."""
           self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)
           self.hitbox_rect.center = self.pos
           self.rect.center = self.hitbox_rect.center

        def update(self) -> None:
             """Runs all the character functions."""
             self.input()
             self.movement()
             self.player_rotate()
             if self.attack_cooldown > 0:
                self.attack_cooldown -= 1

    class Sword(pygame.sprite.Sprite):
        """This class creates and controls a sword sprite.
    
            Functions:
            __init__ -- Creates the character object
            player_rotate -- Gets player sprite rotation
            Movement -- moves the sword sprite 
            update -- Runs all the functions to move the sword.
            """

        def __init__(self, x, y, angle) -> None:
            """Initialization function for the sword.

            Arguments:
            Self
            x -- coordinate
            y -- coordinate
            angle -- sprite image rotation angle
            
            """

            super().__init__()
            self.image = pygame.image.load("img/sword.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.x = x
            self.y = y
            self.angle = angle
            self.speed = 10
            self.x_vel = math.cos(self.angle * (2*math.pi/360)) * self.speed
            self.y_vel = math.sin(self.angle * (2*math.pi/360)) * self.speed

        def movement(self) -> None:
            """Moves the character based on movement speed."""
            self.x = self.x_vel
            self.y = self.y_vel

            self.rect.x = int(self.x)
            self.rect.y = int(self.y)

        def update(self) -> None:
            """Runs all the character functions."""
            self.movement()

    class Boss(pygame.sprite.Sprite):
        """This class creates and controls a boss sprite.
    
            Functions:
            __init__ -- Creates the boss object
            boss_rotate -- Gets boss sprite rotation
            input -- chooses how to move the boss. 
            is_attacking -- Attack cooldown
            Movement -- moves the boss sprite 
            update -- Runs all the functions to move boss.
            """

        def __init__(self) -> None:
            """Initialization function for the boss.

            Arguments:
            Self
            
            """

            super().__init__()
            self.pos = pygame.math.Vector2(b_start_x, b_start_y)
            self.image = pygame.transform.rotozoom(pygame.image.load("img/troll.png").convert_alpha(), 0, .2)
            self.base_image = self.image
            self.hitbox_rect = self.base_image.get_rect(center= self.pos)
            self.rect = self.hitbox_rect.copy()
            self.count = 0
            self.speed = boss_speed
            self._health = 20
            self.damage = 5
            self.attack_cooldown = 0
            self.title = "boss"
            self.augment = {"attack": False, "speed": False, "atime": 0, "stime": 0}
            self.equipped = {"Rusty Armor": False, "Small Sword": False}


        def boss_rotate(self, player) -> None:
            """Rotates the boss sprite to face the player.
            
            Arguments:
            player -- the player character.
            """
            self.mouse_coord = pygame.mouse.get_pos()
            self.x_mouse_change = (player.hitbox_rect.centerx - self.hitbox_rect.centerx)
            self.y_mouse_change = (player.hitbox_rect.centery - self.hitbox_rect.centery)
            self.angle = math.degrees(math.atan2(self.y_mouse_change, self.x_mouse_change))
            self.image = pygame.transform.rotate(self.base_image, -self.angle)
            self.rect = self.image.get_rect(center = self.hitbox_rect.center)
            self.attack = False
            

        def movement(self) -> None:
           """Moves the character based on movement speed."""
           self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)
           self.hitbox_rect.center = self.pos
           self.rect.center = self.hitbox_rect.center

        def update(self, player) -> None:
             """Runs all the functions to move the boss.
             
            Arguments:
            player -- the player character.
             """
             self.input(player)
             self.movement()
             self.boss_rotate(player)
             if self.attack_cooldown > 0:
                self.attack_cooldown -= 1

        def is_attacking(self) -> None:
            """Checks attack cooldown."""
            if self.attack_cooldown == 0:
                self.attack_cooldown = 80
                damage_calc(self, character)

        def input(self, player) -> None:
            """Calculates where to move the boss based on player location.
            
            Arguments:
            player -- the player character.
            """
            self.velocity_x = 0
            self.velocity_y = 0

            keys = pygame.key.get_pressed()
            if player.hitbox_rect.centery < self.hitbox_rect.centery:
                self.velocity_y = -self.speed
            if player.hitbox_rect.centery > self.hitbox_rect.centery:
                self.velocity_y = self.speed
            if player.hitbox_rect.centerx > self.hitbox_rect.centerx:
                self.velocity_x = self.speed
            if player.hitbox_rect.centerx < self.hitbox_rect.centerx:
                self.velocity_x = -self.speed

            if self.velocity_x != 0 and self.velocity_y != 0:
                self.velocity_x /= math.sqrt(2)
                self.velocity_y /= math.sqrt(2)

            #if math.sqrt(abs(player.hitbox_rect.center[0] - self.hitbox_rect.center[0])**2 + abs(player.hitbox_rect.center[1] - self.hitbox_rect.center[1])**2) < 90:
            if self.hitbox_rect.colliderect(boss_player.hitbox_rect):
                if random.randint(1, 10) > 8:

                    self.attack = True
                    self.count += 1
                    self.is_attacking()
                    #game_font.render_to(screen, (50,360), str(self.count), "red")
            else:
                self.attack = False
        

    boss_player = Player()
    all_sprites = pygame.sprite.Group()
    sword_group = pygame.sprite.Group()
    boss = Boss()
    

    all_sprites.add(boss_player)
    
    while running:
        movement = []
        if character.augment["speed"] or character.augment["attack"]:
            if time() - character.augment["atime"] >= 60:
                character.augment["attack"] = False
            if time() - character.augment["stime"] >= 60:
                character.augment["speed"] = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if stand_alone:
                    running = False
                pygame.display.quit()
                return
            
                        

            
        
        #screen.fill("blue")
        clock.tick(60)
        
        screen.blit(background, (0, 0))
        screen.blit(boss_player.image, boss_player.rect)
        screen.blit(boss.image, boss.rect)
        game_font.render_to(screen, (400,0), str(boss._health), "red")
        game_font.render_to(screen, (100,0), str(character._health), "blue")
        boss_player.update()
        sword_group.update()
        
        boss.update(boss_player)

        if boss._health <= 0:
                if board:
                    board.board.boss = False
                    character.gold += random.randint(5, 20)
                    pygame.display.quit()
                    
                    return
                else:
                    running = False
        elif character._health <= 0:
            pygame.display.quit()
            return
        
        pygame.display.update()
        #pygame.display.flip()

    pygame.quit()

def main(board = None, character = None, stand_alone = False) -> None:
    """Main function to run the boss battle
    
    Arguments:
    board -- The dungeon board.
    character -- The player's character
    stand_alone -- Whether or not this is loaded by itself or from another file.
    
    """
    
    start(board, character, stand_alone)

if __name__ == "__main__":
    class Character:
        def __init__(self, health, damage):
            self._health = health
            self.damage = damage
            self.augment = {"attack": False, "speed": False, "atime": 0, "stime": 0}
            self.title = "character"
            self.equipped = {"Rusty Armor": False, "Small Sword": False}
    character = Character(30, 5)
    main(character = character, stand_alone = True)