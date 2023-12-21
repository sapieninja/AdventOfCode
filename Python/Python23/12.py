import aoc_utils
import itertools
import functools
from collections import *
lines = aoc_utils.readLines()
t = 0
@functools.cache
def getpossible(known,layout,consumed):
    #consider first item 
    if len(known) == 0:
        if len(layout) == 0:
            return 1
        elif len(layout) == 1 and layout[0] == 0:
            return 1
        else:
            return 0
    item = known[0]
    if item=="?":
        return getpossible("#" + known[1:], layout, consumed) + getpossible("." + known[1:], layout,consumed)
    elif item == "#":
        if len(layout) == 0:
            return 0
        if layout[0] >= 1:
            return getpossible(known[1:], (layout[0]-1,*layout[1:]), True)
        else:
            return 0
    elif item == ".":
        if len(layout) == 0:
            return getpossible(known[1:], layout, False)
        if layout[0] == 0:
            return getpossible(known[1:], (*layout[1:],), False)
        elif not consumed:
            return getpossible(known[1:], layout, False)
        else:
            return 0
for line in lines:
    known, layout = line.split(" ")
    known = "?".join(known for _ in range(5))
    layout = ",".join(layout for _ in range(5))
    layout = tuple(map(int, layout.split(",")))
    t += getpossible(known,layout,False)
print(t)
