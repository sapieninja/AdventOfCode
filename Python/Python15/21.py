import itertools
enemypoints = 104
enemydamage = 8
enemyarmour = 4
weapons = {8:(4,0),10:(5,0),25:(6,0),40:(7,0),74:(8,0)}
armour =  {0:(0,0),13:(0,1),31:(0,2),53:(0,3),75:(0,4),102:5}
rings ={0:(0,0),0:(0,0),25:(1,0),50:(2,0),100:(3,0),20:(0,1),40:(0,2)}

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
        for ringsc in itertools.combinations(rings,2):
            damagev = 0
            armourv = 0
            damagev += weapons[weapon][0]
            damagev += rings[ringsc[0]][0]
            damagev += rings[ringsc[1]][0]
            armourv += armour[armourc][1]
            armourv += rings[ringsc[0]][1]
            armourv += rings[ringsc[1]][1]
            if win(points,damagev,armourv,enemypoints,enemydamage,enemyarmour):
                costs.add(weapon+armourc+ringsc[0]+ringsc[1])
print(min(costs))






