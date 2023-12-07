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
import tqdm
from string import ascii_lowercase as alph
lines = aoc_utils.readLines()
seeds = lines[0]
seeds = seeds.split(":")[1]
seeds = [x for x in seeds.split(" ") if x!= ""]
seeds = set(map(int, seeds))
currentmap = seeds
prevmap = set()
for line in tqdm.tqdm(lines[0:]):
    if ":" in line:
        prevmap = currentmap.union(prevmap)
        currentmap = set()
    elif line != "":
        a,b,c = map(int,line.split(" "))
        for i in range(c):
            if (b+i) in prevmap:
                currentmap.add(a+i)
                prevmap.remove(b+i)
print(min(currentmap.union(prevmap)))
