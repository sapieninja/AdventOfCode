
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
north = (-1,0)
south = (1,0)
east = (0,1)
west = (0,-1)
def findloop(starts,grid):
    toExplore = deque()
    distance = defaultdict(int)
    for start in starts:
        toExplore.append(start)
        distance[start] = 1
    while toExplore:
        print(toExplore)
        x,y = toExplore.popleft()
        dp = getconnections((x,y))
        for dx,dy in dp:
            if 0<=x+dx<X and 0<=y+dx<Y and (x+dx,y+dy) not in distance:
                toExplore.append((x+dx,y+dy))
                distance[(x+dx,y+dy)] = distance[(x,y)] + 1
    for x in range(X):
        for y in range(Y):
            if (x,y) in distance:
                print(grid[x][y],end="")
            else:
                print(".",end="")
        print("")
    return set(distance.keys())
def getconnections(pos):
    x,y = pos
    dp = []
    match grid[x][y]:
        case  "|": dp = [north,south]
        case "-": dp = [east,west]
        case  "L": dp = [north, east] 
        case "J": dp = [north, west]
        case "7": dp = [south, west]
        case "F": dp = [south, east]
        case "S": dp = [(p-x,q-y) for p,q in starts]
    return dp
for x in range(X):
    for y in range(Y):
        if grid[x][y] == "S":
            starts = []
            for delta in [north,south,east,west]:
                dx, dy = delta
                if 0<=x+dx<X and 0<=y+dy<Y:
                    if (-dx,-dy) in getconnections((x+dx,y+dy)):
                        starts.append((x+dx,y+dy))
def searchfrompos(x,y):
    dp = [north, south, east, west]
    toExplore = deque()
    for direction in [north,south,east,west]:
        toExplore.append((x,y,direction))
    count = 0
    while toExplore:
        x,y,direction = toExplore.popleft()
        searched.add((x,y,direction))
        for new in internalconnects((x,y,direction)):
            if (x,y,new) not in searched:
                toExplore.append((x,y,new))
        dx, dy = direction
        if 0<=x+dx<X and 0<=y+dy<Y:
            if (x+dx, y+dy, (-dx,-dy)) not in searched:
                toExplore.append((x+dx, y+dy, (-dx,-dy)))
                if grid[x+dx][y+dy] == ".":
                    count += 1
        else:
            return 0
    print(searched,count)
    return count
loop = findloop(starts, grid)
def contained(x,y):
    if (x,y) in loop:
        return 0
    substr = grid[x][0:y]
    return (substr.count("F")+substr.count("L")+substr.count("J")+substr.count("|")+substr.count("7"))%2
t = 0
for x in range(X):
    for y in range(Y):
        if (x,y) not in loop:
            grid[x][y] = "."
for x in range(X):
    for y in range(Y):
        t+=contained(x,y)
print(t)
