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
print("You are in a maze. Where do you want to go?")
path1 = input("Type 'left' or 'right'\n")
if path1 == "left":
          print("The left path leads to the exit, and the journey continues in a bustling city. There you find two buildings to enter in the city. Which one you want to enter?")
          path2 = input("Type 'older' or 'green'\n")
          if path2 == "older":
                    print("This building is a secret hideout of a rebel group that provides the next objective. Now you have to decide to follow him or fight against and take the treasure to you.")
                    path3 = input("Type 'follow' or 'fight'\n")
                    if path3 == "fight":
                              print("You have taken the treasure and won the game!")
                    else:
                              print("As the rebel got older, he turned crazy and did not trust you enough to accept you in the group, so he backstabbed you on the first mission.")
          else:
                    print("The green building is a trap set by enemies. Game over")
else:
          print("The right path leads to a dead-end with a sleeping Minotaur. Game over!")
