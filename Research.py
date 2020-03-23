from Switch import *

def Research():
    loop = True

    R_Military_All = R_Military_init()
    while loop:
        printResearch()
        choice = int(input(":> "))
        loop = Switch(0, 3, choice)
    if choice == 0:  # Return to the main menu
        loop = True
        while loop:
            print("return")
            choice = int(input(":> "))
            loop = Switch(0, 10, choice)
    elif choice == 1:  # View the military upgrades
        loop = True
        while loop:
            R_Selected = printMilitaryResearch(R_Military_All)
            loop = False
    elif choice == 2:  # View the logistical upgrades
        loop = True
        while loop:
            printLogisticsResearch()
            choice = int(input(":> "))
            loop = Switch(0, 10, choice)
    elif choice == 3:  # View the economy upgrades
        loop = True
        while loop:
            printEconomyResearch()
            choice = int(input(":> "))
            loop = Switch(0, 10, choice)
        if choice == 1:
            printResearchSelection(Matrix[2][0], Matrix[2][1], Matrix[2][2])




def printResearch():
    print("[0] Return")
    print("[1] Military")
    print("[2] Logistics")
    print("[3] Economy")

def printMilitaryResearch(R_Military_All):
    print("m")  # GENERAL FORMAT IS SHOWN BELOW FOR HOW EACH TECH IS PRINTED
    loop = True
    while loop:
        for i in range(0, len(R_Military_All)):
            print("[" + str(i+1) + "] " + R_Military_All[i].classification)
            print(R_Military_All[i].name)
            print(R_Military_All[i].cost)
            print(R_Military_All[i].desc + "\n")
        choice = int(input(">: "))
        loop = Switch(0, len(R_Military_All), choice)
        return R_Military_All[choice-1]

def printLogisticsResearch():
    print("l")

def printEconomyResearch():
    print("e")

def printResearchSelection(name, cost, description):
    print(name + ":")
    print(description)
    print("Research " + name + " for " + cost + "?")
    print("[1] Yes")
    print("[2] No")

# Formatted as the following. First column is military upgrades. Second for logistics. Third for Economy.
# Each row represents another tech within that same tree.

def R_Military_init():
    R_Military_Blasters1 = R_Military("Military", "Better Blasters", 300, "Provides better blasters", [1, 1, 1])
    R_Military_Shields1 = R_Military("Military", "Better Shields", 200, "Provides better shields", [2, 2, 2])
    return [R_Military_Blasters1, R_Military_Shields1]

class R_Upgrade:
    def __init__(self, classification, name, cost, desc, effect):
        self.classification = classification
        self.name = name
        self.cost = cost
        self.desc = desc
        self.effect = effect  # effect will be in the format of a list that will be broken down into a code
                              # each letter will indicate something about what the upgrade effects.

class R_Military(R_Upgrade):
    pass

class R_Logistics(R_Upgrade):
    pass

class R_Economy(R_Upgrade):
    pass

