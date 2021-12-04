import aoc_utils
import itertools
import functools
from functools import cache
import operator
import networkx
import math
from collections import *
from copy import deepcopy
import random
import re
nums = aoc_utils.readlines()
def getmostcommon(numsin):
    numones = [0]*len(numsin[0])
    for x in range(len(numsin[0])):
        for num in numsin:
            if num[x] == "1":
                numones[x]+=1
    epsilon = ""
    for x in numones:
        if x>=len(numsin)/2:
            epsilon+="1"
        else:
            epsilon+="0"
    return epsilon
def elimination(nums,operator):
    for x in range(len(nums[0])):
        digit = getmostcommon(nums)[x]
        nums = list(filter(lambda num:operator(num[x],digit),nums))
        if len(nums) == 1:
            return int(nums[0],2)
print("Part 1:", int(getmostcommon(nums),2) * (2**len(nums[0])-int(getmostcommon(nums),2)-1))
print("Part 2:", elimination(deepcopy(nums),operator.eq)*elimination(deepcopy(nums),operator.ne))
