import aoc_utils
import itertools
import functools
import operator
import turtle
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
            if 0<=x+dx<X and 0<=y+dy<Y and (x+dx,y+dy) not in distance:
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
    print(x,y)
    dp = []
    match grid[x][y]:
        case  "|": dp = [north,south]
        case "-": dp = [east,west]
        case  "L": dp = [north, east] 
        case "J": dp = [north, west]
        case "7": dp = [south, west]
        case "F": dp = [south, east]
        case "S": dp = [(p-x,q-y) for p,q in starts]
    print(dp)
    return dp
for x in range(X):
    for y in range(Y):
        if grid[x][y] == "S":
            start = (x,y)
            starts = []
            for delta in [north,south,east,west]:
                dx, dy = delta
                if 0<=x+dx<X and 0<=y+dy<Y:
                    if (-dx,-dy) in getconnections((x+dx,y+dy)):
                        starts.append((x+dx,y+dy))
loop = findloop([starts[0]], grid)
def getarea(coords):
    A = 0
    for i in range(len(coords)):
        c = coords[i]
        n = coords[(i+1)%len(coords)]
        A += (n[1] + c[1])*(c[0]-n[0])/2
    return A
print(len(loop))
for x in range(X):
    for y in range(Y):
        if grid[x][y] == "S":
            grid[x][y] = "F"
input()
lloop = [start]
while len(loop) != len(lloop):
    x,y = lloop[-1]
    for dx,dy in getconnections(lloop[-1]):
        if (x+dx,y+dy) not in lloop:
            lloop.append((x+dx, y+dy))
            break
print(getarea(lloop))
print(abs(getarea(lloop)) - len(lloop)/2 +1)
input()
offset = {"|": (0,0.5), "-":(0.5,0), "L":(0.5, -0.5), "7":(-0.5, 0.5), "J": (0.5,0.5), "F": (-0.5,-0.5)}
pos = [x for x in lloop]
for wrapping in (-1,1):
    first = True
    pos = [x for x in lloop]
    for i in range(len(lloop)):
        x,y = lloop[i]
        prevf = pos[(i-1)%len(lloop)]
        if first:
            pos[i] = (pos[i][0] + offset[grid[x][y]][0]*wrapping, pos[i][1] + offset[grid[x][y]][1]*wrapping)
            first = False
        else:
            val = offset[grid[x][y]]
            opt1 = (x + val[0], y + val[1])
            opt2 = (x - val[0], y - val[1])
            c1 = int(prevf[0] == opt1[0]) + int(prevf[1] == opt1[1])
            c2 = int(prevf[0] == opt2[0]) + int(prevf[1] == opt2[1])
            if c1 >= c2:
                pos[i] = opt1
            else:
                pos[i] = opt2
    print(pos)
    print(getarea(pos))
Bob = turtle.Turtle()
Bob.hideturtle()
Bob.speed(10)
Bob.penup()
for (x,y),(x1,y1) in zip(pos,lloop):
    Bob.goto(x*3,y*3)
    Bob.pendown()
input()
