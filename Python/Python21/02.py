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
lines = aoc_utils.readlines()
x = 0
y = 0
aim = 0
for line in lines:
    if line.startswith("forward"):
        x+=int(line.split()[1])
        y+=int(line.split()[1])*aim
    if line.startswith("down"):
        aim+=int(line.split()[1])
    if line.startswith("up"):
        aim-=int(line.split()[1])
    if line.startswith("backward"):
        x-=int(line.split()[1])
print(x,y)
print(x*y)
