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
import time
lines = aoc_utils.readlines()
density = defaultdict(int)
for line in lines:
    print(lines.index(line)/500)
    a, b = line.split(" -> ")
    a = list(map(int, (a.split(","))))
    b = list(map(int, (b.split(","))))
    if a[0] == b[0]:
        for y in range(min(a[1], b[1]), max(b[1], a[1]) + 1):
            density[(int(a[0]), y)] += 1
    elif a[1] == b[1]:
        for x in range(min(a[0], b[0]), max(b[0], a[0]) + 1):
            density[(x, int(a[1]))] += 1
    else:
        xlist = []
        ylist = []
        for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            xlist.append(x)
        for x in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
            ylist.append(x)
        if (b[1] - a[1]) / (b[0] - a[0]) > 0:
            for (x, y) in zip(xlist, ylist):
                density[(x, y)] += 1
        else:
            for (x, y) in zip(xlist, reversed(ylist)):
                density[(x, y)] += 1

count = 0
for entry in density:
    if density[entry] > 1:
        count += 1
print(count)
