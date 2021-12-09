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

lines = aoc_utils.readlines()
count = 0

@functools.lru_cache()
def isinbasin(x, y):
    number = int(lines[x][y])
    if lines[x][y] == "9":
        return None
    else:
        if x != 0:
            if number > int(lines[x - 1][y]):
                return isinbasin(x - 1, y)
        if x != len(lines) - 1:
            if number > int(lines[x + 1][y]):
                return isinbasin(x + 1, y)
        if y != 0:
            if number > int(lines[x][y - 1]):
                return isinbasin(x, y - 1)
        if y != len(lines[0]) - 1:
            if number > int(lines[x][y + 1]):
                return isinbasin(x, y + 1)
    return (x, y)


basins = defaultdict(int)
for x in range(len(lines)):
    for y in range(len(lines[0])):
        print(x, y)
        if isinbasin(x, y) is not None:
            basins[isinbasin(x, y)] += 1
print(functools.reduce(operator.mul,sorted(basins.values())[-3:]))
