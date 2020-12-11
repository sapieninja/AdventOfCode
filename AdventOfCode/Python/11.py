from collections import *
import itertools
import random
import re
import sys
import aoc_utils
import queue
from operator import *
import functools
def main():
    inputs = aoc_utils.readlines()
    old_inputs = [x for x in inputs]
    while True:
        inputs = step(inputs)
        for y in (x for x in inputs):
            print(y)
        if inputs == old_inputs:
            break
        old_inputs = [x for x in inputs]
        print("NEXT ITERATION")
    count = 0
    for x in inputs:
        for y in x:
            if y == "#":
                count+=1
    print(count)
def step(inputs):
    length = len(inputs[0])
    newlist = [x for x in inputs]
    for x in range(len(inputs)):
        for y in range(length):
            if inputs[x][y] == "L":
                nearby = []
                if x != len(inputs) - 1:
                    xplus = True
                else: xplus = False
                if x != 0:
                    xminus = True
                else: xminus = False
                if y != length - 1:
                    yplus = True
                else:
                    yplus = False
                if y != 0:
                    yminus = True
                else:yminus = False
                if xplus and yplus:nearby.append(inputs[x+1][y+1])
                if xplus:nearby.append(inputs[x+1][y])
                if xplus and yminus:nearby.append(inputs[x+1][y-1])
                if yplus:nearby.append(inputs[x][y+1])
                if yminus:nearby.append(inputs[x][y-1])
                if xminus and yplus:nearby.append(inputs[x-1][y+1])
                if xminus:nearby.append(inputs[x-1][y])
                if xminus and yminus:nearby.append(inputs[x-1][y-1])
                if "#" in nearby:
                    continue;
                else: newlist[x] = newlist[x][:y] + "#" + newlist[x][y+1:]
            elif inputs[x][y] == "#":
                nearby = []
                if x != len(inputs) - 1:
                    xplus = True
                else: xplus = False
                if x != 0:
                    xminus = True
                else: xminus = False
                if y != length - 1:
                    yplus = True
                else:
                    yplus = False
                if y != 0:
                    yminus = True
                else:yminus = False
                if xplus and yplus:nearby.append(inputs[x+1][y+1])
                if xplus:nearby.append(inputs[x+1][y])
                if xplus and yminus:nearby.append(inputs[x+1][y-1])
                if yplus:nearby.append(inputs[x][y+1])
                if yminus:nearby.append(inputs[x][y-1])
                if xminus and yplus:nearby.append(inputs[x-1][y+1])
                if xminus:nearby.append(inputs[x-1][y])
                if xminus and yminus:nearby.append(inputs[x-1][y-1])
                amount = len([x for x in nearby if x=="#"])
                if amount >= 4:
                    newlist[x] = newlist[x][:y] + "L" + newlist[x][y+1:]
    return newlist
        
main()