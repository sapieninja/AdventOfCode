import itertools
enemypoints = 104
enemydamage = 8
enemyarmour = 4
weapons = {8:(4,0),10:(5,0),25:(6,0),40:(7,0),74:(8,0)}
armour =  {0:(0,0),13:(0,1),31:(0,2),53:(0,3),75:(0,4),102:(0,5)}
rings ={25:(1,0),50:(2,0),100:(3,0),20:(0,1),40:(0,2),80:(0,3)}

def win(points,damage,armour,enemypoints,enemydamage,enemyarmour):
    while True:
        attack = damage - enemyarmour
        if attack <= 0:
            attack = 1
        enemypoints-=attack
        if enemypoints <= 0:
            return True
        attack = enemydamage - armour
        if attack <= 0:
            attack = 1
        points-=attack
        if points <= 0:
            return False
points = 100
costs = set()
for weapon in weapons:
    for armourc in armour:
        for r in range(3):
            if r == 0:
                damage = 0
                defense = 0
                damage += weapons[weapon][0]
                defense+= armour[armourc][1]
                if win(points,damage,defense,enemypoints,enemydamage,enemyarmour):
                    costs.add(weapon+armourc+sum(ringsc))
            for ringsc in itertools.combinations(rings,r):
                print(ringsc)
                damage = 0
                defense = 0
                damage += weapons[weapon][0]
                defense+= armour[armourc][1]
                for ringx in ringsc:
                    defense += rings[ringx][1]
                    damage += rings[ringx][0]
                if win(points,damage,defense,enemypoints,enemydamage,enemyarmour):
                    costs.add(weapon+armourc+sum(ringsc))
print(min(costs))
