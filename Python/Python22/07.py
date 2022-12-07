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
directories = {}
cwd = ""
intrinsic = {}
extrinsic = defaultdict(list)
readingmode=False
for line in lines:
    if line.startswith("$ cd"):
        readingmode=False
        path = line.split()[-1]
        if path=="/":
            cwd=""
        elif path=="..":
            cwd="/".join(cwd.split("/")[:-1])
        else:
            cwd+="/"+path
    if readingmode:
        if line.startswith("$"):
            readingmode = False
        else:
            lineItems = line.split()
            if lineItems[0] == "dir":
                extrinsic[cwd].append(cwd+"/"+lineItems[1])
            else:
                intrinsic[cwd]+=int(lineItems[0])
    if line.startswith("$ ls"):
        intrinsic[cwd] = 0
        readingmode=True
total = {}
def calctotal(cwd):
    t = 0
    for i in extrinsic[cwd]:
        t += calctotal(i)
    total[cwd] = intrinsic[cwd] + t
    return intrinsic[cwd]+t
calctotal("")
print(sum(x for x in total.values() if x<=100000))
print(min(sorted(list(x for x in total.values() if x >=total[""] - 40000000))))
