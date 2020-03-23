from Switch import *
import sys

def Commanders(Player_Faction, Enemy_Faction):
    loop = True
    while loop:
        for i in range(0, 19):
            print("[" + str(i + 1) + "] " + str(Player_Faction.commanders[i]) + ": " + str(Player_Faction.troops[i]))
        choice = int(input(">: "))
        loop = Switch(0, 19, choice)
    Display(choice, Player_Faction, Enemy_Faction)


def Display(choice, Player_Faction, Enemy_Faction):
    print(Player_Faction.commanders[choice-1] + ":")
    count = 0
    count2 = 1
    print("[0] Return")
    for i in range(0, Player_Faction.troops[choice-1]):
        count = count + 1
        if count == 1:
            string = ("[" + str(i+1) + "]" + " 1st PLT")
        elif count == 2:
            string = ("[" + str(i+1) + "]" + " 2nd PLT")
        elif count == 3:
            string = ("[" + str(i+1) + "]" + " 3rd PLT")
        elif count == 4:
            string = ("[" + str(i+1) + "]" + " 4th PLT")
        if count2 == 1:
            string = (string + " A CO")
        elif count2 == 2:
            string = (string + " B CO")
        elif count2 == 3:
            string = (string + " C CO")
        elif count2 == 4:
            string = (string + " D CO")
        if count % 4 == 0:
            count = 0
            count2 = count2 + 1
        print(string)