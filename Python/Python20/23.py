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
order = aoc_utils.read()
cups = list(map(int,order))
maximum = max(cups)
print(maximum)
current = cups[0]
for x in range(100):
    collection = [cups.pop((cups.index(current)+1)%len(cups)),cups.pop((cups.index(current)+1)%len(cups)),cups.pop((cups.index(current)+1)%len(cups))]
    print(collection)
    lc =current - 1
    while cups.count(lc) != 1:
        lc -= 1
        if lc<=0:
            lc = maximum
        print(lc)
    index = cups.index(lc)+ 1
    for x in collection:
        cups.insert(index,x)
        index += 1
    current = cups[(cups.index(current)+1)%len(cups)]
    print(cups,current)
output = ""
index = cups.index(1) + 1
for x in range(len(cups)-1):
    output += str(cups[(index+x)%len(cups)])
print(output)
