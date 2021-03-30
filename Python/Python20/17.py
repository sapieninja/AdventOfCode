from collections import *
import itertools
import random
import re
import sys
import aoc_utils
import queue
from operator import *
import math
import functools
from copy import deepcopy
lines = aoc_utils.readlines()
p = []
for x in range(len(lines)):
    for y in range(len(lines[0])):
        if lines[x][y] == "#":
            p.append((x,y,0))
def iteration(p):
    #i can only process the places that either are a cube, or are directly a neighbour to a cube
    pp = set()
    np = set([x for x in p])
    for place in p:
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                for dz in [-1,0,1]:
                    pp.add((place[0]+dx,place[1]+dy,place[2]+dz))
    for place in pp:
        no = 0
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                for dz in [-1,0,1]:
                    if not(dx==dy==dz==0):
                        if (place[0] +dx,place[1]+dy,place[2]+dz) in p:
                            no += 1
        if place in p:
            if not(no == 2 or no == 3):
                np.remove(place)
        if place not in p:
            if no == 3:
                np.add(place)
    return np
for x in range(6):
    p = iteration(p)
    for y in p:
        print(y)
    input()
print(len(p))
