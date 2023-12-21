import aoc_utils
import itertools
import functools
import operator
import math
from collections import *
from copy import deepcopy
import random
import re
from string import ascii_lowercase as alph
import sys
grid = [list(x) for x in aoc_utils.readLines()]
X = len(grid)
Y = len(grid[0])
def getbeamlocs(x,y,dx,dy):
    locs = set()
    explored = set()
    start = (x,y,dx,dy)
    Q = deque()
    Q.append(start)
    while Q:
        C = Q.popleft()
        if C in explored:
            continue
        explored.add(C)
        x,y,dx,dy = C
        if not (0<=x<X and 0<=y<Y):
            continue
        locs.add((x,y))
        piece = grid[x][y]
        if piece == ".":
            Q.append((x+dx,y+dy,dx,dy))
        elif piece == "\\":
            dx, dy = dy, dx
            Q.append((x+dx,y+dy,dx,dy))
        elif piece == "/":
            dx, dy = -dy, -dx
            Q.append((x+dx,y+dy,dx,dy))
        elif piece == "|":
            if (dx,dy) == (1,0) or (dx,dy) == (-1,0):
                Q.append((x+dx,y+dy,dx,dy))
            else:
                Q.append((x+1, y, 1, 0))
                Q.append((x-1, y, -1, 0))
        elif piece == "-":
            if (dx,dy) == (0,1) or (dx,dy) == (0,-1):
                Q.append((x+dx,y+dy,dx,dy))
            else:
                Q.append((x, y+1, 0, 1))
                Q.append((x, y-1, 0, -1))
    return locs
maximum = 0
for x in range(0,X):
    maximum = max(maximum, len(getbeamlocs(x, 0, 0, 1)))
    maximum = max(maximum, len(getbeamlocs(x, Y-1, 0, -1)))
for y in range(0,Y):
    maximum = max(maximum, len(getbeamlocs(0, y, 1, 0)))
    maximum = max(maximum, len(getbeamlocs(X-1, y, -1, 0)))
print(maximum)
