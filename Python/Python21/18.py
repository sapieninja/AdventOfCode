import aoc_utils
import itertools
import functools
import operator
import networkx
import math
from collections import *
from copy import deepcopy
import random import re
lines = aoc_utils.readlines()
lines = list(map(eval,lines))
def addrightmost(part,add):
    if type(part[-1]) == type(1):
        part[-1] += add
        return
    addrightmost(part[-1],add)
def addleftmost(part,add):
    if type(part[0]) == type(1):
        part[0] += add
        return
    addleftmost(part[0],add)
def explode(line,d):
    #bug
    #when there are two sublists the explosion does not work
    for x in range(len(line)):
        if d == 3 and type(line[x]) == type([]):
            if len(line[x]) == 2:
                a,b = line[x]
                line[x] = 0
                return a,b,x,True
        if type(line[x]) == type([]):
            a,b,i,validity = explode(line[x],d+1)
            if validity:
                if i-1!=-1:
                    if type(line[x][i-1]) == type(1):
                        line[x][i-1] += a
                    else:
                        addrightmost(line[x][i-1],a)
                    a = 0
                if i+1!=len(line[x]):
                    if type(line[x][i+1]) == type(1):
                        line[x][i+1] += b
                    else:
                        addleftmost(line[x][i+1],b)
                    b = 0
                return a,b,x,True
    return 0,0,0,False
def split(line):
    for x in range(len(line)):
        if type(line[x]) == type(1):
            if line[x] >= 10:
                a = line[x]//2
                b = math.ceil(line[x]/2)
                line[x] = [a,b]
                return True
        else:
            if split(line[x]):
                return True
    return False
def magnitude(line):
    if type(line) == type(0):
        return line
    else:
        return 3*magnitude(line[0]) + 2 * magnitude(line[-1])
def addition(a,b):
    line = [a,b]
    action = True
    while action:
        action = False
        a,b,i,action = explode(line,0)
        if i-1!=-1:
            if type(line[i-1]) == type(1):
                line[i-1] += a
            else:
                addrightmost(line[i-1],a)
            a = 0
        if i+1!=len(line):
            if type(line[i+1]) == type(1):
                line[i+1] += b
            else:
                addleftmost(line[i+1],b)
            b = 0
        if action == False:
            action = split(line)
    return line
current = lines[0]
maximum = 0
for a,b in itertools.permutations(lines,2):
    result = magnitude(addition(deepcopy(a),deepcopy(b)))
    if result > maximum:
        maximum = result
print(maximum)
