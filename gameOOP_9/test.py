import random
from time import time
import my_utilities as MU
import container_assignment as CC

room_width = ([random.randint(4, 9) for x in range(10)][random.randint(0, 9)])
room_width2 = ([random.randint(4, 9) for x in range(10)])


letters = []

while True:
    
    choice = MU.get_key()

    if choice == 113:
        print(choice)
        letters.append(choice)
        #break
    elif choice == 72:
        print("up")
        letters.append(choice)
    elif choice == 57:
        break
    else:
        print(choice)
        letters.append(choice)

print(letters)
        


