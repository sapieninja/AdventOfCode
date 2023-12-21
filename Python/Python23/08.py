import aoc_utils 
import itertools
import functools
import operator
import networkx as nx
import math
from collections import *
from copy import deepcopy
import random
import re
from string import ascii_lowercase as alph
lines = aoc_utils.readLines()
instr = lines[0]
moves = {}
for line in aoc_utils.removeEmpties(lines[1:]):
    start, possible = line.split(" = ")
    left, right = possible.split(", ")
    left = left[1:]
    right = right[:-1]
    moves[start] = (left,right)
starts = [x for x in moves.keys() if x.endswith("A")]
cycles = []
for start in starts:
    pos = start
    prev = defaultdict(list)
    num = 0
    while True:
        move = instr[num%len(instr)]
        if move == "L":
            pos = moves[pos][0]
        else:
            pos = moves[pos][1]
        if pos.endswith("Z"):
            cycles.append(num+1)
            break
        num += 1
print(math.lcm(*cycles))
