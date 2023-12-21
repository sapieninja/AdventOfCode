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
grid = aoc_utils.readLines()
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
    return dp
def internalconnects(pos):
    #return the other positions you can get to on a given tile
    x,y,direction = pos
    match grid[x][y], direction:
        case ".",_: return {north,south,east,west}
        case "|": return set()
        case "-": return set()
        case "L":
            if direction in {south,west}: return {south,west}
            else:
                return set()
        case "J":
            if direction in {south, east}: return {south,east}
            else:
                return set()
        case "7":
            if direction in {north,east}: return {north,east}
            else:
                return set()
        case "F":
            if direction in {north, west}: return {north,west}
            else:
                return set()
        case "S":
            return set()
    return set()
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
total = 0
searched = set()
for x in range(X):
    for y in range(Y):
        if grid[x][y] == "." and (x,y,north) not in searched:
            total += searchfrompos(x,y)
print(total)
