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
grids = aoc_utils.readParagraphs()
def getreflections(grid):
    reflections = []
    for i in range(len(grid)-1):
        before = grid[i::-1]
        after = grid[i+1:]
        valid = True
        for x,y in zip(before,after):
            if x != y:
                valid = False
        if valid:
            reflections.append(i)
    return reflections
def getscore(grid):
    t = 0
    for item in getreflections(grid):
        t += (item+1)*100
    for item in getreflections(list(map(list,zip(*grid)))):
        t += (item + 1)
    return t
def allreflects(grid):
    return [getreflections(grid), getreflections(list(map(list,zip(*grid))))]
def findsmudges(grid):
    old = allreflects(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == ".":
                grid[y][x] = "#"
            else:
                grid[y][x] = "."
            new = allreflects(grid)
            for item in new[0]:
                if item not in old[0]:
                    return (item+1)*100
            for item in new[1]:
                if item not in old[1]:
                    return (item+1)
            if grid[y][x] == ".":
                grid[y][x] = "#"
            else:
                grid[y][x] = "."
p1 = 0
p2 = 0
for grid in grids:
    grid = list(map(list,grid))
    p1 += getscore(grid)
    p2 += findsmudges(grid)
print(p1)
print(p2)
