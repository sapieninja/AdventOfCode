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
lines = aoc_utils.readLines()
t = 0
def getpossible(known,layout):
    reg = ".*"
    for item in layout:
        reg += item*"(#|\?)"
        reg += ".+"
    reg = reg[:-1] + "*"
    print(reg)
    return len(re.findall(reg, known))
for line in lines:
    known, layout = line.split(" ")
    #known = "?".join(known for _ in range(5))
    #layout = ",".join(layout for _ in range(5))
    layout = tuple(map(int, layout.split(",")))
    t += getpossible(known,layout)
print(t)
