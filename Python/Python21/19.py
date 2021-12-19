import aoc_utils
import itertools
import functools
import operator
import math
from collections import *
from copy import deepcopy
import random
import re
lines = aoc_utils.readlines()
scanners = []
for line in lines:
    if line.startswith("---"):
        scanners.append([])
    elif line != "":
        line = line.split(",")
        line = tuple(map(int,line))
        scanners[-1].append(line)
beacons = set(scanners[0])
def generate(beacons):
    beacons = deepcopy(beacons)
    first = set()
    for axisorder in itertools.permutations((0,1,2)):
        for axispolarity in itertools.permutations((1,1,1,-1,-1,-1),3):
            newbeacons = []
            for beacon in beacons:
                x = beacon[axisorder[0]]*axispolarity[0]
                y = beacon[axisorder[1]]*axispolarity[1]
                z = beacon[axisorder[2]]*axispolarity[2]
                newbeacons.append((x,y,z))
            if newbeacons[0] not in first:
                first.add(newbeacons[0])
                yield (newbeacons,axisorder,axispolarity)
def getdistance(one,two):
    return (one[0]-two[0] , one[1] - two[1] , one[2] - two[2])
def checkoverlap(one,two):
    #to find the overlap we only need to check all rotations of one beacon then find all the distances.
    for rotation in generate(two):
        perm = rotation[0]
        distances = defaultdict(int)
        for a,b in itertools.product(one,perm):
            distances[getdistance(a,b)] += 1
            if distances[getdistance(a,b)] == 12:
                return getdistance(a,b),rotation[1],rotation[2]
    return False
def manhattan(one,two):
    return abs(one[0] - two[0]) + abs(one[1] - two[1]) + abs(one[2] - two[2])
def rotateandtransform(beacons,axisorder,axispolarity,vector):
        newbeacons = []
        for beacon in beacons:
            x = beacon[axisorder[0]]*axispolarity[0] + vector[0]
            y = beacon[axisorder[1]]*axispolarity[1] + vector[1]
            z = beacon[axisorder[2]]*axispolarity[2] + vector[2]
            newbeacons.append((x,y,z))
        return newbeacons
beacons = set(scanners[0])
found = {}
found[0] = True
poses = set()
tested = set()
while len(found) != len(scanners):
    for p in range(len(scanners)):
        for i in range(len(scanners)):
            if i not in found and p in found and (p,i) not in tested:
                output = checkoverlap(scanners[p],scanners[i])
                if output == False:
                    tested.add((p,i))
                    continue
                else:
                    toadd = rotateandtransform(scanners[i],output[1],output[2],output[0])
                    poses.add(output[0])
                    scanners[i] = toadd
                    found[i] = True
                    for p in toadd:
                        beacons.add(p)
maximum = 0
for x,y in itertools.product(poses,poses):
    if manhattan(x,y) > maximum:
        maximum = manhattan(x,y)
print(len(beacons))
print(maximum)
