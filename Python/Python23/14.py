import aoc_utils
import itertools
import functools
import operator
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
west = (0, -1)
south = (1,0)
east = (0,1)

def roll(grid,direction):
    while True:
        moved = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "O":
                    nx = x + direction[0]
                    ny = y + direction[1]
                    if 0<= nx < X and 0<= ny <Y:
                        if grid[nx][ny] == ".":
                            grid[x][y] = "."
                            grid[nx][ny] = "O"
                            moved = True
        if not moved:
            break
    return grid
def score(grid):
    s = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "O":
                s+=(X-x)
    return s
cycle = []
def gridtostr(grid):
    return "".join("".join(x) for x in grid)
seen = {}
cycle = []
for i in range(1,1000000001):
    for direction in (north, west, south, east):
        grid = roll(grid, direction)
    cycle.append(score(grid))
    if gridtostr(grid) in seen:
        break
    seen[gridtostr(grid)] = i
last = seen[gridtostr(grid)]
cycle = cycle[last:]
print(cycle)
steps = 1000000000 - last - 1
print(cycle[steps%len(cycle)])
