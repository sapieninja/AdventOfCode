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
import heapq
from string import ascii_lowercase as alph
grid = [list(x) for x in aoc_utils.readLines()]
#dijkstra over (x,y,dx,dy,straight)
Q = []
X = len(grid)
Y = len(grid[0])
heapq.heappush(Q, (0,(0,0,1,0,0)))
heapq.heappush(Q, (0,(0,0,0,1,0)))
prev = {}
mdistance = {}
ddistance = {}
while Q:
    distance,current = heapq.heappop(Q)
    x,y,dx,dy,straight = current
    if (x,y) not in mdistance:
        mdistance[(x,y)] = distance
    elif distance < mdistance[(x,y)]:
        mdistance[(x,y)] = distance
    for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
        ndx,ndy = direction
        nstraight = straight
        valid = True
        if (dx,dy) == (-ndx,-ndy):
            valid = False
        if (dx,dy) != (ndx,ndy) and straight < 4:
            valid = False
        if (dx,dy) == (ndx,ndy) and straight >= 10:
            valid = False
        elif (dx,dy) != (ndx,ndy):
            nstraight = 0
        if 0<=x+ndx<X and 0<=y+ndy<Y and valid:
            nstraight += 1
            nd = distance + int(grid[x+ndx][y+ndy])
            new = (x+ndx, y+ndy, ndx,ndy,nstraight)
            if new not in ddistance:
                ddistance[new] = 100000000000000000000
            if nd < ddistance[new]:
                ddistance[new] = nd
                heapq.heappush(Q,(nd,new))
                prev[new] = current
print(mdistance[(X-1,Y-1)])
