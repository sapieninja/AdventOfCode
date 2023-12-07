import aoc_utils 
from collections import *
lines = aoc_utils.readLines()
total = 0
gears = defaultdict(set)
for y in range(len(lines)):
    current = "" 
    seen = False
    loc = []
    for x in range(len(lines[y])):
        if lines[y][x].isdigit():
            current += lines[y][x]
            for dx in [-1, 0 , 1]:
                for dy in [-1, 0, 1]:
                    if (x+dx) >= 0 and (x+dx) < len(lines[y]) and (y+dy) >= 0 and (y+dy) < len(lines):
                        if lines[y+dy][x+dx] == "*":
                            seen = True
                            loc.append((y+dy, x+dx))
        else:
            if seen:
                for loca in loc:
                    gears[loca].add(int(current))
                seen = False
            loc = []
            current = ""
    if seen:
        for loca in loc:
            gears[loca].add(int(current))
        current = ""
        seen = False
        loc = []
for gear in gears:
    if len(gears[gear]) == 2:
        first,last = list(gears[gear])
        total += first*last
print(total)
