import aoc_utils
import itertools
import functools
import operator
import networkx
import math
from collections import *
from copy import deepcopy
import random
import re
import time
import matplotlib as plt
import numpy as np

lines = aoc_utils.readlines()
pos = set()


def showpos(pos):
    minx = 10000000000000000000
    maxx = 0
    miny = 10000000000000000000
    maxy = 0
    for (x, y) in pos:
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if (x, y) in pos:
                print("■", end="")
            else:
                print(" ", end="")
        print()

for line in lines:
    if line.count(",") == 1:
        x, y = line.split(",")
        pos.add((int(x), int(y)))
    else:
        newpos = set()
        if line == "":
            continue
        about = int(line.split()[-1].split("=")[1])
        if line.split()[-1].startswith("y"):
            for x, y in pos:
                y = about - abs(y - about)
                newpos.add((x, y))
        if line.split()[-1].startswith("x"):
            for x, y in pos:
                x = about - abs(x - about)
                newpos.add((x, y))
        pos = newpos
        showpos(pos)
        print()
