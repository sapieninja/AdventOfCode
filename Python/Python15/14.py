import aoc_utils
from collections import *
lines = aoc_utils.readlines()
deer = {}
for line in lines:
    line = line.split()
    deer[line[0]] = [int(line[3]),int(line[6]),int(line[-2])]
    print(deer)
status = {}
for dee in deer.keys():
    status[dee] = [0,deer[dee][1],deer[dee][2]]#0 is for how far they have gone, 1 is for how long till rest, and 2 is for how long resting for
print(status)
points = defaultdict(int)
for x in range(2503):
    for dee in deer.keys():
        if status[dee][1] != 0:
            status[dee][0] += deer[dee][0]
            status[dee][1] -= 1
            if status[dee][1] == 0:
                status[dee][2] -= 1
        else:
            if status[dee][2] == 0:
                status[dee][1] = deer[dee][1]
                status[dee][2] = deer[dee][2]
            else:
                status[dee][2] -= 1
    maximum = 0
    for dee in deer:
        if status[dee][0] > maximum:
            maximum = status[dee][0]
    for dee in deer:
        if status[dee][0] == maximum:
            points[dee] += 1
print(max(points.values()))


