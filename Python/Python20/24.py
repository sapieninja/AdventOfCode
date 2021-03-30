from collections import defaultdict
from aoc_utils import readlines
lines = readlines() 
black = set()
for line in lines:
    line = line.replace("se","x").replace("sw","p").replace("nw","v").replace("ne","f")
    linev = [line.count("w"),line.count("e"),line.count("x"),line.count("p"),line.count("v"),line.count("f")]
    #replace se ne with e and sw nw by w
    for x in ((3,4,0),(2,5,1)):
        while linev[x[0]] >= 1 and linev[x[1]] >=1:
            linev[x[0]] -= 1
            linev[x[1]] -= 1
            linev[x[2]] += 1
    #reduce to only two coordinates instead of 6
    while linev[2] > 0:
        linev[2] -= 1
        linev[3] += 1
        linev[1] += 1
    while linev[4] > 0:
        linev[4] -=1
        linev[5] += 1
        linev[0] +=1
    linev = [linev[0],linev[1],linev[3],linev[5]]
    #subtract e from w and west from east
    linev = tuple((linev[0]-linev[1],linev[2]-linev[3]))
    if linev in black:
        black.remove(linev)
    else:
        black.add(linev)
print(len(black))
for x in range(100):
    toprocess = defaultdict(int) 
    newblack = set()
    for square in black:
        for dx in [1,0,-1]:
            for dy in [1,0,-1]:
                if not(dx==dy==1) and not(dx==dy==-1) and not(dy==dx==0):
                    toprocess[(square[0]+dx,square[1]+dy)] += 1
    for square in toprocess:
        no = toprocess[square]
        if no == 2:
            newblack.add(square)
        elif square in black and no == 1:
            newblack.add(square)
    black = newblack
print(len(black))
