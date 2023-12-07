import aoc_utils
import time
import math
lines = aoc_utils.readLines()
times = lines[0].split(":")[1]
distances = lines[1].split(":")[1]
times = [x for x in times.split() if x != " "]
distances = [x for x in distances.split() if x != " "]
def possible(t, d):
    disc = math.sqrt(math.pow(int(t),2)-4*int(d))/2
    return math.floor((int(t)/2) + disc) - math.ceil((int(t)/2)-disc) + 1
print(math.prod(map(lambda x: possible(x[0],x[1]),zip(times, distances))))
print(possible("".join(times), "".join(distances)))
