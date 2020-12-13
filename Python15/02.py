import fileinput
import aoc_utils
inputs = aoc_utils.readlines()
areas = []
for x in inputs:
    xs = x.split('x')
    areas.append((int(xs[0]),int(xs[1]),int(xs[2])))
print(areas)
area = 0
for x in areas:
    area += 2*x[0]*x[1] + 2*x[1]*x[2] + 2*x[0]*x[2] + min(x[0]*x[1],x[1]*x[2],x[0]*x[2])
print(area)
length = 0
for x in areas:
    x = list(x)
    x.sort()
    length += 2*(x[0]+x[1]) + x[0]*x[1]*x[2]
    print(x,length)
print(length)
