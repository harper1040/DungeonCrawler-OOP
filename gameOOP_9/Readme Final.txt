Joey Harper
2025-4-18
OOP Final Readme file


	Welcome to Dungeon Crawler the game of... dungeon crawling... In this game the goal is to beat a dungeon boss. Instead of a leveled dungeon where you traverse a dungeon down into it's depths, I chose to make this a find the key to open the portal type gameplay. The key, aka Ancient Crystal, can be found laying on the ground or being held by an enemy. Defeat the enemy and they drop the crystal, some enemies will drop other items. Once you have the key take it to the portal to open it and travel to the boss room where you will have to fight to the death... or rage quit that's always an option. You choose your player and then the town, dungeon, and monsters are generated. When you enter the dungeon monsters are spawned in. Be careful once you thin out the monster ranks more will spawn in after a while. Once you best the boss and clear the dungeon a new dungeon and boss room will be generated. You can crawl dungeons until you die.


	Monster AI- The mimic will attack and then run away up to 4 tiles. It randomly chooses a direction and uses move_actor 4 times. It moves until it hits something or reaches 4 tiles. 

	The boss will persue the player and attack when close enough.

	I have chosen equippable items, non hostile monsters, a shop, and potions. Equipment will include armor and weapon(s). The potions will be health, attack and speed. All potions can be purchased from the shop and dropped by enemies. Health give the player + 5 health, speed and attack increase those respective stats by 3 for 60 seconds. Speed will move the player 3 times every movement this may make traversal of the dungeon more difficult. There is a sword and an armor that is equippable that provides either more damage or more resistance to damage. The Slime is the non hostile monster. When interacting it will go blooub or the character will comment on it's stickiness.

	I used pygame for the music/sound effects and the boss battle. The sounds are made by me as are the backgrounds and sprites. 

	Enjoy the dungeon... Don't die the insurance situation is still a bit, how would you say, non existant...

	