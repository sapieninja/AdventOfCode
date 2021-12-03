import aoc_utils
import networkx
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
print("Part 1:", x*aim)
print("Part 2",  x*y  )

