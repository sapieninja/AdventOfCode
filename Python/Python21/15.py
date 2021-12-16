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
G = networkx.DiGraph()
R = len(g)
C = len(g[0])


def newweight(r, c):
    addition = r // R + c // C
    answer = g[r % R][c % C] + addition
    return (answer-1)%9 +1
def getnumber(x,y):
    output = (y)*1000
    return output + x
def getvalue(number):
    y = output//1000
    x = output%1000
    return g[x][y]


for r in range(R*5):
    for c in range(C*5):
        for i in itertools.product([-1, 0, 1], [-1, 0, 1]):
            if i[0] == i[1] == 0:
                continue
            if (
                0 <= r + i[0] < R*5
                and 0 <= c + i[1] < C*5
                and abs(i[0] * i[1]) != 1
            ):
                G.add_edge(getnumber(r,c), getnumber(r+i[0],c+i[1]), weight=newweight(r, c))
print(G)
print("Part 1:", networkx.shortest_path(G,getnumber(0,0),getnumber(R-1,C-5),weight="weight"))
print("Part 2:", networkx.shortest_path_length(G,getnumber(0,0),getnumber(R*5-1,C*5-1),weight="weight"))
