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
aim = aoc_utils.read()
minx = 192
maxx = 251
miny = -89
maxy = -59
x,y = 0,0
contenders = set()
count = 0
for dx in range(0,252):
    for dy in range(-100,1000):
        vx = dx
        vy = dy
        x = 0
        y = 0
        maximumy = 0
        valid = False
        for i in range(10000):
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            elif vx < 0:
                vx += 1
            vy -=1
            if y > maximumy:
                maximumy = y
            if minx<=x<=maxx and miny<=y<=maxy:
                valid = True
        if valid:
            count += 1
            contenders.add((dx,dy))
print(len(contenders))





