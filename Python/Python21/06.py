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
nums = aoc_utils.readSplittedIntLine()
density = defaultdict(int)
for x in nums:
    density[x] += 1
print(density)
for x in range(256):
    for key in range(-1,max(density)):
        density[key] = density[key+1]
    density[max(density)] = 0
    density[6] = density[6] +  density[-1]
    density[8] = density[8] +  density[-1]
    density[-1] = 0
print(sum(density.values()))
