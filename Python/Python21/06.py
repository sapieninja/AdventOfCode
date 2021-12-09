import aoc_utils
import sys
from collections import *
nums = aoc_utils.readSplittedIntLine()
density = defaultdict(int)
nums.sort()
for x in nums:
    density[x] += 1
for x in range(256):
    for key in range(-1,max(density)):
        density[key] = density[key+1]
    density[max(density)] = 0
    density[6] = density[6] +  density[-1]
    density[8] = density[8] +  density[-1]
    density[-1] = 0
print(sum(density.values()))
