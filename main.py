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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

choice_1 = input("You are at the entrance to the island. Would you like to go left or right?\n")

# Building game with choices.
if choice_1 == "left":
    choice_2 = input("You have reached a lake. Do you wait or swim?\n")
    if choice_2 == "wait":
        choice_3 = input("You have taken the boat and reached a place with three doors. The doors are red, blue and yellow respectively. Which door do you choose?\n")
        if choice_3 == "yellow":
            print("You win")
        elif choice_3 == "red":
            print("As soon as you open the red door, you are consumed by a great fire and you die. Game over.")
        elif choice_3 == "blue":
            print("On opening the blue door, many beasts attack you and eat you. Game over.")
        else:
            print("The vapours you inhaled while passing through the lake have turned you into a madman. You get into a blinding rage and end up killing yourself. Game over.")
    else:
        print("You are attacked by a trout while swimming and you die. Game over")
else:
    print("You turn right, fall into a hole and die. Game over.")