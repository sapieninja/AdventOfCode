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
density = Counter(nums)
count = 0
target = sorted(nums)[len(nums)//2]
for num in nums:
    count += abs(num-target)
print("Part 1", count)
target = sum(nums)/len(nums)
target += sum([(x-target)/abs(x-target) for x in nums])/(2*len(nums))#implement error term
target += 0.0001
count = 0
for num in nums:
    difference = abs(num-target)
    count += (difference**2 + difference)/2
print("Part 2:",count)
