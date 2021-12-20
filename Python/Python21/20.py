import aoc_utils
import itertools
import functools
import operator
import math
from collections import *
from copy import deepcopy
import random
import re
def lookup(x,y,p):
    if 0<=x<len(g) and 0<=y<len(g):
        return g[y][x]
    else:
        if p == 0:
            return "."
        else:
            return "#"
lines = aoc_utils.readlines()
enhancement = lines[0]
g = [list(x) for x in lines[2:]]
def enhance(g,q):
    newg = []
    for i in range(-1,len(g)+1):
        newg.append([])
        for p in range(-1,len(g)+1):
            output = ""
            for dy,dx in itertools.product([-1,0,1],[-1,0,1]):
                output += (lookup(p+dx,i+dy,q))
            output = output.replace("#","1")
            output = output.replace(".","0")
            index = int(output,2)
            newg[-1].append(enhancement[index])
    return newg
def pprint(g):
    for x in g:
        print()
        for y in x:
            print(y,end="")
for x in range(200):
    g = enhance(g,0)
    pprint(g)
    g = enhance(g,1 if enhancement[0] == "#" else 0)
    pprint(g)
    if x == 0:
        total = 0
        for i in range(len(g)):
            for p in range(len(g)):
                if g[i][p] =="#":
                    total += 1
        print(total)
total = 0
for i in range(len(g)):
    for p in range(len(g)):
        if g[i][p] =="#":
            total += 1
print(total)
pprint(g)
