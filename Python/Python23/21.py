import aoc_utils
import itertools
import more_itertools as itertools
import functools
import operator
import networkx as nx
import math
from collections import *
from copy import deepcopy
import random
import re
from string import ascii_lowercase as alph

grid = [list(line) for line in aoc_utils.readLines()]
X = len(grid)
Y = len(grid[0])
def getno(x,y,n):
    pos = set()
    pos.add((x,y))
    newcoords = set()
    for i in range(n):
        newcoords = set()
        for coord in pos:
            for direction in ((-1,0),(1,0),(0,1),(0,-1)):
                dx,dy = direction
                x,y = coord
                if grid[(x+dx)%X][(y+dy)%Y] == "." or grid[(x+dx)%X][(y+dy)%Y] == "S":
                    newcoords.add((x+dx,y+dy))
        pos = newcoords
    t = 0
    for x,y in pos:
        if not (0<=x<X or 0<=y<Y):
            t += 1
    print(t)
    return len(pos)
sx,sy = 0,0
for x in range(X):
    for y in range(Y):
        if grid[x][y] == "S":
            sx,sy=x,y
evenstepgrid = 7367
oddstepgrid = 7329
n = 1
a = (n-1)*(n-1)
b = n*n
print(getno(sx,sy,197))
print(5618+5628+5607+5597+(6454+6443+6416+6412)*(n-1)+7367*a + 7329*b)
