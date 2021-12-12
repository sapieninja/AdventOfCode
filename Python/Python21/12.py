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
c = defaultdict(list)
for line in lines:
    a,b = line.split("-")
    c[a].append(b)
    c[b].append(a)
def noways(current,route):
    if "start" in route and current == "start":
        return 0
    if current == current.lower() and current in route:
        for i in route:
            if i == i.lower():
                if route.count(i) == 2:
                    return 0
    gone = deepcopy(route)
    gone.append(current)
    if current == "end":
        return 1
    else:
        output = 0
        for i in c[current]:
            output += noways(i,gone)
        return output
print(noways("start",[]))
