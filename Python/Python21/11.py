import aoc_utils
import itertools
import functools
import operator
import networkx
import math
from collections import *
from copy import deepcopy
import random
import re
g=aoc_utils.numericgrid()
flashes = 0
flashed = set()
def checkflash(x,y):
    global flashes
    if (x,y) in flashed:
        return
    if g[x][y] > 9:
        flashed.add((x,y))
        flashes += 1
        jx = [-1,0,1]
        for dx,dy in itertools.product(jx,jx):
            if x+dx < 0 or x+dx >= len(g) or y+dy < 0 or y+dy >= len(g[0]):
                continue
            else:
                if dx==dy==0:
                    continue
                g[x+dx][y+dy] += 1
                checkflash(x+dx,y+dy)
        g[x][y]=0
i = 0
while True:
    i += 1
    flashed = set()
    for x in range(len(g)):
        for y in range(len(g[0])):
            g[x][y] += 1
    for x in range(len(g)):
        for y in range(len(g[0])):
            checkflash(x,y)
            for p,q in flashed:
                g[p][q] = 0
    if len(flashed) == len(g)*len(g[0]):
        print(i)
        break
