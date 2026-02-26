#Name: Connor Altland
#Class: 6th Hour
#Assignment: Scenario 6

import random

#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Semester Project 1 using classes instead of dictionaries, include and refactor
#the combat test code below as well.)

class char:
    def __init__(self, name, hp, init, ac, atkmod, damage):
        self.name = name
        self.hp = hp
        self.init = init
        self.ac = ac
        self.atkmod = atkmod
        self.damage = damage


gale = char("gale",32,1,14,6,  random.randint(1,10) + random.randint(1,10))
troll = char("troll",84,1,15,7, random.randint(1,6) + random.randint(1,6) + 4)
laezel = char("laezel",48,1,17,6,  random.randint(1,6) + random.randint(1,6) + 3)
goblin = char("goblin",7,0,12,4, random.randint(1,6) + 2)
shadowheart = char("shadowheart",40,1,18,4,  random.randint(1,6) + 3)
orc = char("orc",15,1,13,5, random.randint(1,12) + 3)
astarion = char("astarion",40,3,14,5,  random.randint(1,6) + random.randint(1,6) + 4)
mindflayer = char("mindflayer",71,1,15,7, random.randint(1,10) + random.randint(1,10) + 4)
dragon = char("dragon",127,2,18,7, random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4)

while True:
    print("Starting Turn.")
    Gale_roll = random.randint(1, 20) + gale.init
    Troll_roll = random.randint(1, 20) + troll.init
    print(f"{gale.name} rolled {Gale_roll}")
    hero_attack = random.randint(1, 20) + 6
    print(f"{troll.name} rolled {Troll_roll}")
    if Troll_roll >= Gale_roll:
        print(f"{troll.name} goes first")
        villain_attack = random.randint(1,20) + troll.atkmod
        if villain_attack == 20:
            print("Natural 20")
            gale.hp -= troll.damage * 2
        else:
            if villain_attack >= gale.ac:
                print("attack hit")
                gale.hp -= troll.damage
                print(gale.ac)
                print(troll.damage)
            elif villain_attack < gale.ac:
                print("attack missed")
        if gale.hp >= 1:
                continue
        elif gale.hp <= 0:
                print("Gale died , Troll wins")
                break
        if hero_attack > troll.atkmod:
            print("attack hit")
            troll.hp -= gale.damage
            print(troll.hp)
            print(gale.damage)
        elif hero_attack <= troll.ac:
            print("attack missed")
        if troll.hp >= 1:
            continue
        elif troll.hp <= 0:
            print("Troll died , Gale wins")
            break

    elif Gale_roll >= Troll_roll:
        print(f"gale goes first")
        hero_attack = random.randint(1, 20) + troll.atkmod
        if hero_attack > troll.ac:
            print("attack hit")
            troll.hp -= gale.damage
            print(troll.hp)
            print(gale.damage)
        elif hero_attack <= troll.ac:
            print("attack missed")
        if  troll.hp >= 1:
            continue
        elif troll.hp <= 0:
            print("Troll died , Gale wins")
            break
    if Troll_roll > Gale_roll:
        print(f"troll goes first")
        villain_attack = random.randint(1, 20) + troll.ac
        if villain_attack == 20:
            print("Natural 20")
            gale.hp -= troll.damage * 2
        else:
            if villain_attack > gale.ac:
                print("attack hit")
                gale.hp -= troll.damage
                print(gale.hp)
                print(troll.damage)
            elif villain_attack < gale.ac:
                print("attack missed")
                if gale.hp >= 1:
                    continue
                elif gale.hp <= 0:
                    print("Gale died , Troll wins")
                    break
