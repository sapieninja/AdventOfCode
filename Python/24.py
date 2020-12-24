from collections import *
import itertools 
import random
import re
import sys
import aoc_utils
import queue
from operator import *
import math
import functools
from copy import deepcopy
lines = aoc_utils.readlines() 
black = set()
repeated = 0
for line in lines:
    line = re.sub("se","x",line)
    line = re.sub("sw","p",line)
    line = re.sub("nw","v",line)
    line = re.sub("ne","f",line)
    linev = [line.count("w"),line.count("e"),line.count("x"),line.count("p"),line.count("v"),line.count("f")]
    #replace se ne with e and sw nw by w
    for x in ((3,4,0),(2,5,1)):
        while linev[x[0]] >= 1 and linev[x[1]] >=1:
            linev[x[0]] -= 1
            linev[x[1]] -= 1
            linev[x[2]] += 1
    #reduce to only two coordinates instead of 6
    while linev[2] > 0:
        linev[2] -= 1
        linev[3] += 1
        linev[1] += 1
    while linev[4] > 0:
        linev[4] -=1
        linev[5] += 1
        linev[0] +=1
    linev = [linev[0],linev[1],linev[3],linev[5]]
    #subtract e from w and west from east
    linev = tuple((linev[0]-linev[1],linev[2]-linev[3]))
    if linev in black:
        black.remove(linev)
        repeated += 1
    else:
        black.add(linev)
print(len(black))
for x in range(100):
    toprocess = set() 
    newblack = set()
    for square in black:
        for dx in [1,0,-1]:
            for dy in [1,0,-1]:
                if not(dx==dy==1) and not(dx==dy==-1):
                    toprocess.add((square[0]+dx,square[1]+dy))
    for square in toprocess:
        no = 0
        for dx in [1,0,-1]:
            for dy in [1,0,-1]:
                if not(dx==dy==0) and not(dx==dy==1) and not(dx==dy==-1):
                    # print(square[0] + dx,square[1] + dy)
                    if (square[0] + dx,square[1] + dy) in black:
                        no += 1
        if no == 2:
            newblack.add(square)
        elif square in black and no == 1:
            newblack.add(square)
    black = newblack
print(x,len(black))
