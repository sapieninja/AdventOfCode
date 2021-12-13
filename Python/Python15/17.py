import aoc_utils
import itertools
containers = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
count = 0
minimum = 99999999999999999999999999999999999999999999999999999999999999999
for r in range(1,len(containers)):
    for p in itertools.combinations(containers,r):
        if sum(p) == 150:
            count += 1
            if minimum > len(p):
                minimum = len(p)
print(count)
count = 0
for p in itertools.combinations(containers,minimum):
    if sum(p) == 150:
        count += 1
print(count)

