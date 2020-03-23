from random import *
# Max Soldiers: Each platoon has 45 Soldiers maximum. This allows for absolutely no more than 1 LT, 2 SFC, no more than
# 5 SSGs, no more than 10 SGTs. The remainder (CPL to PVT) doesn't matter.

# Slots: 1 "PL", 1 "PSG", 4 "SL", 8 "TL". The highest qualified will always take the highest role

class Platoon(object):
    def __init__(self):
        self.squad = []
        for i in range(0,4):
            self.squad.append(self.Squad)

    class Squad:
        def __init__(self):
            self.test = 4






def FirstNameGenerator():
    first_names = {"1" : "James",
             "2" : "Morgan",
             "3" : "David",
             "4" : "Chase",
             "5" : "Cole"}
    return first_names[str(randint(1, 5))]

def LastNameGenerator():
    last_names = {"1" : "Carson",
             "2" : "Joseph",
             "3" : "Barnes",
             "4" : "Randall",
             "5" : "Madison"}
    return last_names[str(randint(1, 5))]

def RankGenerator(grade):
    ranks = {"1" : "Recruit",
             "2" : "PVT",
             "3" : "PFC",
             "4" : "CPL",
             "5" : "SGT",
             "6" : "SSG",
             "7" : "SFC",
             "8" : "MSG",
             "9" : "SGM",
             "11" : "LT",
             "13" : "CPT",
             "14" : "MAJ",
             "15" : "LTC",
             "16" : "COL"}
    return ranks[str(grade)]

def RankFinder(soldier):
    soldier.rank

plt = Platoon()
for i in range (0,4):
    print(plt.squad[i].test)


# class Foo(object):
#     class Bar(object):
#         class Blah(object):
#             x=1
#
# print(Foo.Bar.Blah.x)
