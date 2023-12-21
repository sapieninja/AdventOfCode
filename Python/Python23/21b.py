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

grid = [list(line) for line in aoc_utils.readLines()]
X = len(grid)
Y = len(grid[0])
def getno(x,y,n):
    pos = set()
    pos.add((x,y))
    newcoords = set()
    prev = []
    for i in range(n):
        newcoords = set()
        for coord in pos:
            for direction in ((-1,0),(1,0),(0,1),(0,-1)):
                dx,dy = direction
                x,y = coord
                newcoords.add((x+dx,y+dy))
        pos = newcoords
        prev.append(len(pos))
    print(prev)
    return len(pos)
getno(0,0,100)
