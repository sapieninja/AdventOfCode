import aoc_utils
import itertools
import functools
import operator
import networkx as nx
import math
from collections import *
from copy import copy
import random
import re
lines = aoc_utils.readlines()
lines = list(map(list,lines))
counter = 0
R = len(lines)
L = len(lines[0])
print(R,L)
while True:
    newlines = copy(lines)
    counter += 1
    moved = False
    for x in range(R):
        for y in range(L):
            if lines[x][y] == ">":
                if lines[x][(y+1)%L] == ".":
                    newlines[x][y] = "."
                    newlines[x][(y+1)%L] = ">"
                    moved = True
    lines = copy(newlines)
    for x in range(R):
        for y in range(L):
            if lines[x][y] == "v":
                if lines[(x+1)%R][(y)] == ".":
                    newlines[x][y] = "."
                    newlines[(x+1)%R][y] = "v"
                    moved = True
    lines = copy(newlines)
    if not moved:
        print(counter)
        break
