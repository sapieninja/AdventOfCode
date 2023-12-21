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
def nhash(item):
    current = 0
    for character in item:
        current += ord(character)
        current *= 17
        current %= 256
    return current
line = aoc_utils.readLines()[0]
t = 0
for item in line.split(","):
    t += nhash(item)
print(t)
hashmap = [defaultdict((int)) for _ in range(256)]
posmap  = [defaultdict((int)) for _ in range(256)]
for instruction in line.split(","):
    if "=" in instruction:
        label, focal = instruction.split("=")
        pos = nhash(label)
        hashmap[pos][label] = int(focal)
        if label not in posmap[pos]:
            if len(posmap[pos].values()) != 0:
                posmap[pos][label] = max(posmap[pos].values()) + 1
            else:
                posmap[pos][label] = 0
    else:
        label = instruction.split("-")[0]
        pos = nhash(label)
        if label in hashmap[pos]:
            hashmap[pos].pop(label)
            prevloc = posmap[pos].pop(label)
            for key in posmap[pos].keys():
                if posmap[pos][key] > prevloc:
                    posmap[pos][key] -= 1
t = 0
for bno,(focal, poses) in enumerate(zip(hashmap,posmap)):
    for key in focal.keys():
        t += (bno + 1) * (poses[key] + 1) * focal[key]
print(t)
