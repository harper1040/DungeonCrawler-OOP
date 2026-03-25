"""
Joey Harper
2025-4-15
Sound control document which uses pygame to run sounds.
"""

import pygame

pygame.init()


cover: str = "Sounds/creepy1.wav"
town: str = "Sounds/town2.wav"
dungey: str = "Sounds/Dungeon1.wav"
portal: str = "Sounds/portal1.wav"
key: str = "Sounds/pickup1.wav"
slime: str = "Sounds/slime1.wav"
hit: str = "Sounds/hit.wav"

def change_songs(song):
    """This changes songs being played or stops the music if a random value is given, but stop also works.
    
    Arguments:
    song -- Which song you need to play
    """

    pygame.mixer.stop()
    pygame.mixer.music.unload()

    match song:
        case "cover":
            pygame.mixer.music.load(cover)
        case "town":
            pygame.mixer.music.load(town)
            pygame.mixer.music.set_volume(0.4)
        case "dungeon":
            pygame.mixer.music.load(dungey)
            pygame.mixer.music.set_volume(0.4)
        case _:
            return
    
    pygame.mixer.music.play(-1, 0, 500)

def sound_effect(sound):
    """This plays chosen sounds when called.
    
    Arguments:
    sound -- Which sound you need to play
    """
    
    match sound:
        case "portal":
            pygame.mixer.Sound(portal).play()
        case "key":
            pygame.mixer.Sound(key).play()
            #pygame.mixer.Sound.set_volume(0.5)
        case "change":
            pygame.mixer.Sound(dungey).play()
            #pygame.mixer.Sound.set_volume(0.5)
        case "slime":
            pygame.mixer.Sound(slime).play()
        case "hit":
            pygame.mixer.Sound(hit).play()
        case _:
            return