print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


print("You have arrived at the Island at evening. Would you like to stay the night at the beach, or head inland?")
path1 = input("beach or inland? \n").lower()

if path1 == "beach":
    path2 = input("You decide to wait until you can see where you are going before heading inland. In the morning, you collect yourself. Will you walk along the beach or head into the jungle? Type 'Beach' or 'Jungle'\n ").lower()
    if path2 == "beach":
        path3 = input("You decide it's best to scout the beach before haphazardly walking into the jungle. After walking for a while, you spot a little shack along the beach. Would you like to go on and explore it? Type Y or N \n").lower()
        if path3 == "y":
            print("You head into the shack. It's unlocked. Suddenly, you hear natives outside. It was a good idea to hide, they would have surely killed you on sight. You found the treasure chest! You Win")
        else:
            print("You decide not to head in, and continue on your way. However, you run into a group of natives who do not take kindly to you. A few arrows later, you are dead. Game Over.")

    else:
        print("You head into the jungle, however you can't see well at all. you slip and fall into a ravine. Game over.")

else:
    print("You head inland, fall into a ravine and die. Game over.")
