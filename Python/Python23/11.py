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
grid = [list(x) for x in aoc_utils.readLines()]
X = len(grid)
Y = len(grid[0])
emptyrows = []
for x in range(X):
    if all(v=="." for v in grid[x]):
        emptyrows.append(x)
emptyColumns = []
for y in range(Y):
    if all(v=="." for v in (grid[x][y] for x in range(X))):
        emptyColumns.append(y)
galaxies = []
for x in range(X):
    for y in range(Y):
        if grid[x][y] == "#":
            galaxies.append((x,y))
def pair(diff,g1, g2):
    total = 0
    minx = min(g1[0], g2[0])
    maxx = max(g1[0], g2[0])
    for i in range(minx,maxx):
        if i in emptyrows:
            total += diff - 1
    miny = min(g1[1], g2[1])
    maxy = max(g1[1], g2[1])
    for i in range(miny,maxy):
        if i in emptyColumns:
            total += diff - 1
    return total + abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
p1 = 0
p2 = 0
for i in range(len(galaxies)):
    for other in range(i+1,len(galaxies)):
        p1 += pair(2,galaxies[i],galaxies[other])
        p2 += pair(1000000,galaxies[i], galaxies[other]) 
print(p1)
print(p2)
