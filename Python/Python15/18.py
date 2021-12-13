import aoc_utils
from copy import deepcopy
import itertools
lines = aoc_utils.readlines()
g = [list(line) for line in lines]
R = 0
C = len(g[0])
g[0][0] = "#"
g[0][C-1] = "#"
g[C-1][0] = "#"
g[C-1][C-1] = "#"
for line in g:
    print(line)
print("______")
def nextxy(x,y):
    neighbours = 0
    if x==0 and y == 0:
        return "#"
    if x==0 and y == C-1:
        return "#"
    if x==C-1 and y ==0:
        return "#"
    if x==C-1 and y==C-1:
        return "#"
    for dx,dy in itertools.product([-1,0,1],[-1,0,1]):
        if dx==dy==0 or not(R <= x + dx < C and R <= y + dy < C):
            continue
        if g[x+dx][y+dy] == "#":
            neighbours += 1
    print(g[x][y])
    if g[x][y] == "#":
        if neighbours == 2 or neighbours == 3:
            return "#"
    elif neighbours == 3:
        return "#"
    return "."
for x in range(100):
    new = deepcopy(g)
    for x in range(len(g)):
        for y in range(len(g)):
            new[x][y] = nextxy(x,y)
    for line in g:
        print(line)
    print("_____")
    g = new
total = 0
for line in g:
    for row in line:
        if row == "#":
            total += 1
print(total)


