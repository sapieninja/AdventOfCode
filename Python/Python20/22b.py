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
for line in lines:
    if line.count(":") == 0 and count != 2:
        p1.append(int(line))
    elif line.count(":") == 1:
        count+=1
    if count == 2 and line.count(":") == 0:
        p2.append(int(line))
def game(p1,p2):
    setmoves = set()
    while len(p1) != 0 and len(p2) != 0:
        if (tuple(p1),tuple(p2)) in setmoves:
            return (p1,p2,1)
        setmoves.add((tuple(p1),tuple(p2)))
        d1 = p1.pop(0)
        d2 = p2.pop(0)
        if len(p1) >= d1 and len(p2) >= d2:
            winner = game(p1[:d1],p2[:d2])[2]
        else:
            if d1 >= d2:
                winner = 1
            else:
                winner = 2
        if winner == 1:
            p1.append(d1)
            p1.append(d2)
        else:
            p2.append(d2)
            p2.append(d1)
    return (p1,p2,winner)
p1,p2,_ = game(p1,p2)
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
