from random import *
from NewGame import *
from Overview import *
import time

clear = "\n"*7
print(clear)

loop = True
while loop == True:
    print("[1] New Game")
    print("[2] Load Game")
    print("[3] Options")
    choice = int(input("\n>: "))
    loop = Switch(1,3,choice)
    print(clear)

if choice == 1:
    ##begin a new game
    print("start game")
    unload_vars = NewGame()
    Player_Faction = unload_vars["Player_Faction"]
    Enemy_Faction = unload_vars["Enemy_Faction"]
    READY_TO_EXECUTE = unload_vars["READY_TO_EXECUTE"]
    planet1 = unload_vars["planet1"]
    planet2 = unload_vars["planet2"]
    planet3 = unload_vars["planet3"]
    planet4 = unload_vars["planet4"]
    planet5 = unload_vars["planet5"]
    planet6 = unload_vars["planet6"]
    planet7 = unload_vars["planet7"]



elif choice == 2:
    #open the load game screen
    print("load game")
elif choice == 3:
    #open the options menu
    print("options")

planets = [planet1, planet2, planet3, planet4, planet5, planet6, planet7]
Master = [Player_Faction, Enemy_Faction, planets]

if READY_TO_EXECUTE:
    Overview(Player_Faction, Enemy_Faction, planets)


