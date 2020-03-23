from random import *
from Switch import *
from Faction import *
from Planet import *

clear = "\n"*7
print(clear)

def NewGame():
    READY_TO_EXECUTE = False
    Player_Faction = Faction()
    Enemy_Faction = Faction()
    loop = True
    while loop == True:
        print(clear)
        print("load successful")
        print("Pick your side:")
        print("[1] Empyrion")
        print("[2] United Alliance")
        choice = int(input(">: "))
        loop = Switch(1,2,choice)


    print(clear)
    print(choice)
    if choice == 1:
        print("Emyprion chosen")
        Player_Faction.team = 1
        Enemy_Faction.team = 2
    elif choice == 2:
        print("United Alliance chosen")
        Player_Faction.team = 2
        Enemy_Faction.team = 1

    if Player_Faction.team == 1:
        loop = True
        while loop:
            Player_Faction.commanders[0] = "CPT Carson"
            Player_Faction.troops[0] = 16
            Player_Faction.commanders[1] = "CPT Slammer"
            Player_Faction.troops[1] = 13
            Player_Faction.commanders[2] = "CPT Bland"
            Player_Faction.troops[2] = 16
            print("Pick your Supreme Leader:")
            print("[1] Character A")
            print("[2] Character B")
            print("[3] Character C")
            choice = int(input(">: "))
            loop = Switch(1,3,choice)
            print(clear)

    elif Player_Faction.team == 2:
        loop = True
        while loop:
            Player_Faction.commanders[0] = "CPT Black"
            Player_Faction.troops[0] = 16
            Player_Faction.commanders[1] = "CPT Ramm"
            Player_Faction.troops[1] = 13
            Player_Faction.commanders[2] = "CPT Pelusa"
            Player_Faction.troops[2] = 16
            print("Pick your Supreme Leader:")
            print("[1] Character D")
            print("[2] Character E")
            print("[3] Character F")
            choice = int(input(">: "))
            loop = Switch(1, 3, choice)
            print(clear)

    if Player_Faction.team == 1:
        if choice == 1:
            Player_Faction.leader = "Character A"
        elif choice == 2:
            Player_Faction.leader = "Character B"
        elif choice == 3:
            Player_Faction.leader = "Character C"
    if Player_Faction.team == 2:
        if choice == 1:
            Player_Faction.leader = "Character D"
        elif choice == 2:
            Player_Faction.leader = "Character E"
        elif choice == 3:
            Player_Faction.leader = "Character F"

    #GIVE THE PLANETS INITIAL VALUES HERE
    planet1 = Planet()
    planet1.name = "Rhen Var"

    planet2 = Planet()
    planet2.name = "Mustafar"

    planet3 = Planet()
    planet3.name = "Rengalia"

    planet4 = Planet()
    planet4.name = "Empiria"

    planet5 = Planet()
    planet5.name = "Stelata"

    planet6 = Planet()
    planet6.name = "Cristosis"

    planet7 = Planet()
    planet7.name = "Muzark"
    #END PLANET GENERATION

    READY_TO_EXECUTE = True


    return{"Player_Faction" : Player_Faction,
           "Enemy_Faction"  : Enemy_Faction,
           "READY_TO_EXECUTE": READY_TO_EXECUTE,
           "planet1" : planet1,
           "planet2" : planet2,
           "planet3" : planet3,
           "planet4" : planet4,
           "planet5" : planet5,
           "planet6" : planet6,
           "planet7" : planet7}