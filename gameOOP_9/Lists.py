"""
Joey Harper
2024-12-2
The Lists!! These are lists for whatever I made need theme for.
"""
import random

menuStore = {"startScreen": ["""\n\t\t\tWelcome to Dungeon Crawler would you like a:
                                    (N)ew Game
                                    (C)ontinue a Saved Game
                                    (H)igh Scores
                    """, ["N", "C"]], 
            
            "battlePL": ["""\n
                (P)ower Attack
                (Q)uick Attack
                (C)ounter Attack
                (A)ttack
                (R)un!
                (B)ag of Holding!
            """, ["P", "Q", "C", "A"]], 

            "battlePLS": ["""\n
                (P)ower Attack
                (Q)uick Attack
                (C)ounter Attack
                (A)ttack
                (S)ic Em
                (R)un!
                (B)ag of Holding!
            """, ["P", "Q", "C", "A", "S"]],
            
            "battleBD": ["""\n
                (P)ower Attack
                (Q)uick Attack
                (C)ounter Attack
                (A)ttack
            """, ["P", "Q", "C", "A"]],
            
            "commandPL": ["""\t\tEnter W,S,A,D to move,
                      E for inventory 
                      or Q to quit. """, ["W","A","S","D", "Q"]], 
            
            "tavern": ["""
            ~~~~~~~~Adventurers Tavern~~~~~~~~~~
            {                                  }
             }    Welcome to the Tavern!!     { 
            {    How can I help you today?     }
             }     (S)ell Something           { 
            {      (B)uy Something             }
             }     (I)nformation              { 
            {      (J)ust Talk                 }
             }     (G)ame Mode                {
            {      (L)eave                     }           
             }                                {  
            ===================================           
                         """, ["S", "B", "I", "J", "L", "G"]], 
                         
            "noCake": ["""\n
                        Enter:
                    (C)haracter Bio
                    (I)tems
                    (S)lain Enemies
                    (E)xit To Game
                    (?)Info
                    """, ["E", "C", "S", "I"]], 
                    
            "cake": ["""\n
                    Enter:
                (U)se The Cake!
                (C)haracter Bio
                (I)tems
                (S)lain Enemies
                (E)xit To Game
                (?)Info
                """, ["E", "C", "S", "I", "U"]], 
                
            "gameMode": ["""
        Hey there go ahead and pick your game mode then you can get to killing or hunting or whatever you want.
        Each game mode has a different goal to achieve except for "whatever" which has no goal.
                        
            (P)oints!
            (T)reasure Hunt Specific
            (A)ll The Treasure Hunt
            (H)omicides
            (W)hatever
            (?)Info
        """, ["P", "T", "A", "H", "W"]]}

saveFile = {"1": "Saves/Save1.dat", "2": "Saves/Save2.dat", "3": "Saves/Save3.dat"}

character = "Please choose a character!"

displayCharacter = ["name", "history", "attack", "defense", "health", "level", "exp", "points", "game", "purse", "kills", "buddy"]

medallions = ["Shiny Crimson Medallion of Stabbing Shit!", "Shiny Medallion of Get a Life!",
               "Shiny Medallion of Hay Stack Needling!", "Shiny Medallion of Point Gathering!"]

namesList = ["Gerald", "Timithy", "Dwaynee", "Edgar", "Josh", "Errrric", "Mary", "Tabithuh"]
namesList2 = [" Carolton", " Ibthal", " Shirintas", " Randonious", " Smith", " Tableton", " Shelly", " Riskton"]
extraSillyness = [" The Chased", " The Dismembered", " The Forgotten", " The  ", " The Shivering", " The LongWinded",
                  " The One With The Comically Long Name That is Definitely Unnecessary"]

enemyNamelist = ["Blarth", "John", "Margloth", "Wipstem", "Marro", "Tallor", "Klox", "Rathu"]
enemySillyness = [" The Putrid", " The Scared", " The Garden Flower", " The Obese", " The Valiant", " Killer of Human Confections", " The Naked", " The Suicidal"]

where = ["The Shadows", "Above", "Underground", "The Doorway", "The Future??", "The Heart, Awww!"]

#I tried to give a brief history type line and a statement about the character.
historyList = ["The man who once rode another man to a neighboring town (do with that what you will).",
               "You once fell on hard times and starved to death, you're fine now.",
               "You do not understand why any of us are here but keep coming back anyway.",
               "You once drank milk from a glass.",
               "Your father was a hamster and your mother smelt of elder berries!",
               "You once found a book that taught you how to travel the multiverse, but being sick of such things you used this new found skill to travel to a universe without multiverses. This seems impossible but you some how managed it.",
               "You once... hey where'd you go?",
               "Long ago in the land of Narinn you were pooped out. What you wanted more? You exist enjoy!",
               "Remember that guy you cussed out that one time well he pulled a \"Taken\" with your family and now you have to use your particularly lacking set of skills to save them. Good Luck!",
               "You have a 16% chance of shitting a rainbow. This will look amazing but also hurt like hell as one would rightly assume."]
historyList2 = ["The world was never the same.",
                "To the Shagrin of all who saw you.",
                "This doesn't seem possible but it is.",
                "I have run out of things to say.",
                "あなたはこの言語を話せません!",
                "If life gives you lemons you still need life to give you sugar and water and I guess a glass to make lemonade. Don't be greedy eat your sour fruit.",
                "The world trembled in fear or maybe it's cold? Is it winter? That would be the determinator.",
                "Many hate you and I do as well."]

characterTitle = ["The Valiant", "The Tolerated (Sometimes)", "^^^That Guy^^^", "He Who Smells", "Sniffer of Wigs", "The Untitled Character's Title", "Truck Adjectives"]

madLib = "Welcome to nouns the adjectives place in the universe. Please feel free to verbs."
nouns = ["Mars", "Alderan", "London", "The Cave", "Room"]
adjectives = ["bravest", "Oddest", "Scariest", "blue", ]
verbs = ["Leave", "Die", "Run", "Poop", "Cry", "Jump", "fall"]

enemyDeath = ["Whhhyyyyyy?!", "Blaaaarg!", "Ouchies!", "You Suck!!", "My luck has run it's course and though I die I do not end, I merely begin a new adventure.",
              "OW, this damn game better not summon me again!"]
enemySelf = ["Chose to stab himself...It was very effective.", "Got sick of seeing your face which is saying something, did you see his?!",
             "Never existed in the first place.", "Suffered a flesh woun...nope he's dead.", "Went wee wee wee all the way to hell."]

treasures = ["The Fabled 10mm Socket", "The Holy Grail", "Golden Turd", "Pirate Gold (hope it's not cursed)", "What the? Oh well it's shiny!", "Some dudes arm and leg", 
             "3ft Silver Statue", "A Charizard Card", "A Mysterious Gold Ring, Hmm", "OMG It's a Cake", "A Treasure Map that leads to itself"]

attackTreasure = ["You chose to stop everything and do some push-ups, I guess. Gain some attack.", 
                  "You pushed open this really heavy door...Good for you.",
                  "SQUATS! ATTACK!",
                  "Sneak Attack, you're welcome!"]
defenseTreasure = ["A piece of timber fell on you and you took it like a champ.", "You're no wimp, but you don't want to die either. Have some defense.",
                   "OMG What is that over there? *points* Oh just some DEFENSE!", 
                   "It's Captain America's Shield...err I mean a shield of a non-trademarked character that isn't closely guarded by a super litigious corporation. You know what just... defense, take it, you'll need it if they find out we used their IP.",
                   "The best defense is a good ARMOR! Suit Up!"]
healthTreasure = ["A brisk walk turned into a full run... down a hillside you didn't see. Gain some health, cardio is a good thing!",
                  "See a shiling pick it up oooh hey some health!",
                  "Speed running a game is exactly what the creater intended, here's some health because why not.",
                  "You stopped drink as much carbonated mead and you're looking healthier by the day."]
randomPoints = ["Ryan Styles would be proud!", "Your not even a Gryffindor.", "Hold on to those.", "They add up.", "Nickle and diming your way along!",
                "POINTS!!"]

gameMode = """The game mode is what goal you wish to achieve during your game. 

                    -If you already have a goal you haven't completed and choose a new goal, even the one you already have, you goal will be reset 
                    and all progress will be lost.
                    
                    -Points is for gathering points...don't roll your eyes keep reading. Points are accrued through battle and gathering treasures, 
                    they may also pop up randomly so keep an eye out ;).  

                    -Specific Treasure hunt will randomly choose a treasure for you to find and you must crawl through the dungeon until you find it.

                    -Treasure hunt all is a quest to gather as much treasure as possible.

                    -Homicides well this should be apparent, but basically kill everything in sight and get points for it!

                   - Whatever is whatever you want to do. Basically there is no real goal just go galavanting through the dungeon.
                   
"""
characterSelect = """"""
generalGame = """
                The game of random dungeon adventure! Be weary my adventuring friend if you die your dead for good. That means no more save file ;).
                The menu setup is pretty straight forward type the letter option and it opens the corresponding information screen.
                Other than that you just walk around looking for treasure and enemies to slay. Have fun!
"""
justTalk = ["Oh, me well I've been here for about 6 months now which doesn't make much since since I didn't exist 'til two days ago.",
            "You gonna buy somethin' or just stand 'round gawkin' all day?",
            "I remember when adventurin' meant somethin' it was about protectin' or feedin' your family. Now it's all challenge this and shiny turd that, hmm!",
            "I don't say this to many adventurers, but you my friend are one of the more attractive ones."]
setMode = {"points": "Your playin' for points. It's simple really just get points. How many? What do I look like a statistician here? Go pick up somethin' shiny!",
           "treasureS": "You only need one treasure for this one. The guy at the keyboard tells you what to find and then you go find it... or die those are the only two option.",
           "treasureA": "You may need a bigger bag for this. You must collect one of each available treasure. That's like 11 treasures, so what the hell are you standing here for?",
           "homicide": "It's kinda like the purge. KILL EVERYTHING... Except for me! If I die well I don't know I'm sure you wont get any points for it since I'm just a menu.",
           "whatever": "Do you really need a description of this? Go play in traffic or somethin'!",}


informationDialog = {"gameMode": gameMode, "character": characterSelect, "game": generalGame, "barKeep": justTalk, "setMode": setMode}

def Information(info, key = None):
    if info == "barKeep":
        input(random.choice(informationDialog[info]))
    elif key:
        input(informationDialog[info][key])
    else:
        input(informationDialog[info])



dungeon = [
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",  "", "", "", "", "", "", "", "", ""],
    ["", " ", " ", " ", "", "", " ", "", "", " ", "", " ", "", "", "", " ", "", " ", " ", " ", " ", "", " ", " ", " ", " ", "", "", " ", " ",  "", "", "", " ", "", "", "", " ", ""],
    ["", " ", "", "", " ", "", " ", "", "", " ", "", " ", " ", "", "", " ", "", " ", "", "", "", "", " ", "", "", "", "", " ", "", "",  " ", "", "", " ", " ", "", "", " ", ""],
    ["", " ", "", "", " ", "", " ", "", "", " ", "", " ", " ", "", "", " ", "", " ", "", "", "", "", " ", "", "", "", " ", "", "", "",  "", " ", "", " ", " ", "", "", " ", ""],
    ["", " ", "", "", " ", "", " ", "", "", " ", "", " ", "", " ", "", " ", "", " ", "", " ", " ", "", " ", " ", "", "", " ", "", "", "",  "", " ", "", " ", "", " ", "", " ", ""],
    ["", " ", "", "", " ", "", " ", "", "", " ", "", " ", "", "", " ", " ", "", " ", "", "", " ", "", " ", "", "", "", " ", "", "", "",  "", " ", "", " ", "", "", " ", " ", ""],
    ["", " ", "", "", " ", "", " ", "", "", " ", "", " ", "", "", " ", " ", "", " ", "", "", " ", "", " ", "", "", "", "", " ", "", "",  " ", "", "", " ", "", "", " ", " ", ""],
    ["", " ", " ", " ", "", "", "", " ", " ", "", "", " ", "", "", "", " ", "", " ", " ", " ", " ", "", " ", " ", " ", " ", "", "", " ", " ",  "", "", "", " ", "", "", "", " ", ""],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",  "", "", "", "", "", "", "", "", ""]
]

splash = [
                        
                       " ████████▄  ███    █▄  ███▄▄▄▄      ▄██████▄     ▄████████  ▄██████▄  ███▄▄▄▄   ", 
                       " ███   ▀███ ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ ███    ███ ███▀▀▀██▄ ", 
                       " ███    ███ ███    ███ ███   ███   ███    █▀    ███    █▀  ███    ███ ███   ███ ", 
                       " ███    ███ ███    ███ ███   ███  ▄███         ▄███▄▄▄     ███    ███ ███   ███ ", 
                       " ███    ███ ███    ███ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀     ███    ███ ███   ███ ", 
                       " ███    ███ ███    ███ ███   ███   ███    ███   ███    █▄  ███    ███ ███   ███ ", 
                       " ███   ▄███ ███    ███ ███   ███   ███    ███   ███    ███ ███    ███ ███   ███ ", 
                       " ████████▀  ████████▀   ▀█   █▀    ████████▀    ██████████  ▀██████▀   ▀█   █▀  ",

       " ▄████████    ▄████████    ▄████████  ▄█     █▄   ▄█          ▄████████    ▄████████  ",
       " ███    ███   ███    ███   ███    ███ ███     ███ ███         ███    ███   ███    ███ ", 
       " ███    █▀    ███    ███   ███    ███ ███     ███ ███         ███    █▀    ███    ███ ", 
       " ███         ▄███▄▄▄▄██▀   ███    ███ ███     ███ ███        ▄███▄▄▄      ▄███▄▄▄▄██▀ ", 
       " ███        ▀▀███▀▀▀▀▀   ▀███████████ ███     ███ ███       ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ", 
       " ███    █▄  ▀███████████   ███    ███ ███     ███ ███         ███    █▄  ▀███████████ ", 
       " ███    ███   ███    ███   ███    ███ ███ ▄█▄ ███ ███▌    ▄   ███    ███   ███    ███ ", 
       " ████████▀    ███    ███   ███    █▀   ▀███▀███▀  █████▄▄██   ██████████   ███    ███ ", 
       "              ███    ███                          ▀                        ███    ███ "
]

sys_messages = ["You broke it!", "OOOO you um... You died sorry...", "Hey that's not what that ports for!", 
                "Your a few ones short of a system runtime huh?", "I'm a modern marvel, random snark not generated by AI!",
                "You got a little blood on your... Oh nevermind", "Look a DRAGON!! Nah I'm just playing.", "Do you even read these??"]


items = {"Ancient Crystal" : "Such a strange old crystal..."}
