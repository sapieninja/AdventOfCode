import aoc_utils
import itertools
import more_itertools
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
seeds = [int(x) for x in seeds.split(" ") if x!= ""]
def possible(x):
    for a,b in more_itertools.chunked(seeds, 2):
        if a<=x<a+b:
            return True
    else:
        return False
def convert(ranges,old):
    for dest, source, l in ranges:
        if source<=old<source+l:
            return dest+(old-source)
    else:
        return old
ranges = []
def tryvals():
    i = 1
    while True:
        yield i
        i+=1
seq = tryvals()
for line in tqdm.tqdm(reversed(lines[0:])):
    if ":" in line:
        conv = functools.partial(convert,ranges)
        seq = map(conv,seq)
        ranges = []
    elif line != "":
        a,b,c = map(int,line.split(" "))
        ranges.append((b,a,c))
print(next(filter(possible,seq)))
