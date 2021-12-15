import aoc_utils
import itertools
import more_itertools
import functools
import operator
import math
from collections import *
from copy import deepcopy
import random
import time
import re
lines = aoc_utils.readlines()
start = lines[0]
connections = {}
laggedamount = {}
for line in lines:
    if line == "" or line==start:
        continue
    else:
        a,b = line.split(" -> ")
        connections[a] = b
density = defaultdict(int)
for x in range(len(start)-1):
    density[start[x]+start[x+1]] += 1
for x in range(40):
    wdensity = deepcopy(density)
    for poly in wdensity:
        sub = connections[poly]
        density[poly[0]+sub] += wdensity[poly] 
        density[sub+poly[1]] += wdensity[poly] 
        density[poly] -= wdensity[poly]
edensity = defaultdict(int)
for item in density:
    edensity[item[0]] += density[item]
    edensity[item[1]] += density[item]
edensity[start[0]] += 1
edensity[start[-1]] += 1
print(sum(edensity.values()))
