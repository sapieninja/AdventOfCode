from collections import *
import itertools
import random
import re
import sys
import aoc_utils
import queue
from operator import *
import math
import functools
from copy import deepcopy
lines = aoc_utils.readlines()
P = []
for x in lines:
    ingredients = []
    for word in x.split():
        if word.startswith("("): break
        else:
            ingredients.append(word)
    allergens = re.search(r"\(.*\)",x).group(0)
    pa = []
    for x in allergens.split():
        if x.count("(") == 0 and x.count(")") == 0:
            x = x.replace(",","")
            pa.append(x)
        elif x.count(")") == 1:
            pa.append(x[:-1])
    P.append((ingredients,pa))
print(P)
ti = list(itertools.chain.from_iterable([[ingredient for ingredient in x[0]] for x in P]))
print(ti)
di = {}
for line in P:
    print(line[1])
    for allergen in line[1]:
        if allergen not in di:
            di[allergen] = set(line[0])
        else:
            di[allergen] = set(line[0]).intersection(di[allergen])
dang = {}
while len(di) != 0:
    print(dang,di)
    success = False
    for x in di:
        if len(di[x]) == 1:
            success = True
            dang[x] = list(di[x])[0]
            for y in di:
                di[y].discard(x)
    for x in dang.values():
        for y in di:
            di[y].discard(x)
    if not success:
        break
for x in sorted(dang.keys()):
    print(dang[x],end=",")
print()
