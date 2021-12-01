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
nums = aoc_utils.readints()
p1 = 0
prev = 2**32
for x in nums:
    if x > prev:
        p1+=1
    prev = x
print(p1)
p2 = 0
prev = 2**32
for x in range(len(nums)-2):
    if nums[x] + nums[x+1] + nums[x+2] > prev:
        p2 += 1
    prev = nums[x] + nums[x+1] + nums[x+2]
print(p1,p2)
