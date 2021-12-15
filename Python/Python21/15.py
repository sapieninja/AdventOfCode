import aoc_utils
import itertools
import functools
import operator
import networkx
import math
from collections import *
from datetime import datetime
from copy import deepcopy
import random
import re

g = aoc_utils.numericgrid()
G = networkx.MultiDiGraph()
R = len(g)
C = len(g[0])


def newweight(r, c):
    addition = r // R + c // C
    answer = g[r % R][c % C] + addition
    while answer > 9:
        answer -= 9
    return answer


for r in range(R * 5):
    for c in range(C * 5):
        for i in itertools.product([-1, 0, 1], [-1, 0, 1]):
            if i[0] == i[1] == 0:
                continue
            if (
                0 <= r + i[0] < R * 5
                and 0 <= c + i[1] < C * 5
                and abs(i[0] * i[1]) != 1
            ):
                G.add_edge((r, c), (r + i[0], c + i[1]), weight=newweight(r, c))
print(G)


def dist(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


total = -g[0][0]
for point in networkx.astar_path(
    G, (0, 0), (R * 5 - 1, C * 5 - 1),heuristic=dist
):
    total += newweight(point[0], point[1])
print(total)
