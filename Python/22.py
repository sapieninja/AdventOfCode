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
p1 = []
p2 = []
count = 0
print(lines)
for line in lines:
    if line.count(":") == 0 and count != 2:
        p1.append(int(line))
    elif line.count(":") == 1:
        count+=1
    print(count)
    if count == 2 and line.count(":") == 0:
        p2.append(int(line))
print(p1)
print(p2)
while len(p1) != 0 and len(p2) != 0:
    if p1[0] > p2[0]:
        p1.append(p1.pop(0))
        p1.append(p2.pop(0))
    else:
        p2.append(p2.pop(0))
        p2.append(p1.pop(0))
    print(p1)
    print(p2)
if p1 == []:
    winner = p2
else:
    winner = p1
multi = len(winner)
score = 0
for x in winner:
    score += x*multi
    multi -= 1
print(score)
