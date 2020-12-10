import aoc_utils
import itertools
import datetime
start = datetime.datetime.now()
inputs = aoc_utils.readlines()
connections = []
places = []
for x in inputs:
    split = x.split()
    places.append(split[0])
    places.append(split[2])
    connections.append((split[0],split[2],int(split[4])))
places = set(places)
def distance(route):
    sumlength = 0
    for y in range(len(route)-1):sumlength += next(x[2] for x in connections if (x[1] == route[y] and x[0] == route[y+1]) or (x[1] == route[y+1] and x[0] == route[y]))
    return sumlength
distances = list(map(distance,itertools.permutations(places,len(places))))
print(min(distances))
print(max(distances))
end = datetime.datetime.now()
print(end-start)