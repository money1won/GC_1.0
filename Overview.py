from Planet import *
from Switch import *
from Map import *
from Commanders import *
from Research import *
clear = "\n"*7

def Overview(Player_Faction, Enemy_Faction, planets):
    #7 planets will be made to simulate the game in its early stage. This will be expanded and automated in the future
    loop = True
    while loop:
        print("[1] Map")
        print("[2] Commanders")
        print("[3] Research")
        print("[4] Engineering")
        print("[5] End Turn")
        choice = int(input(">: "))
        loop = Switch(1, 5, choice)
        print(clear)

    if choice == 1:
        loop = True
        while loop:
            Map(planets)
            choice = int(input(">:"))
            loop = Switch(0, 7, choice)
            if choice == 0:
                pass
            elif choice == 1:
                print("Send which unit to " + str(planets[0].name) + "?")
            # if 0 (back), return to main menu
    elif choice == 2:
        print("present commanders")
        Commanders(Player_Faction, Enemy_Faction)
    elif choice == 3:
        Research()
        print("show research")
    elif choice == 4:
        print("show engineering")
    elif choice == 5:
        print("your turn is over!")
        # AI turn
