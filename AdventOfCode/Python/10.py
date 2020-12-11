from collections import *
import itertools
import random
import re
import sys
import aoc_utils
import queue
import functools
inputsints = aoc_utils.readints()
inputsints.sort()
def main():
    no_one = 0
    no_three = 1
    if inputsints[0] == 1:no_one+=1
    elif inputsints[1] ==3: no_three +=1 
    for x in range(len(inputsints)-1):
        if inputsints[x+1] - inputsints[x] == 1: no_one += 1
        elif inputsints[x+1] - inputsints[x] == 3: no_three += 1
    print("Part One: ",no_one*no_three)
    print("Part Two: ",noways(-1,max(inputsints) + 3 ))
@functools.lru_cache(maxsize=None)
def noways(start_digit,maximum):
    no = 0
    if start_digit == -1:start = 0
    else:start = inputsints[start_digit]
    if start_digit == len(inputsints) - 1: return 1
    if maximum - inputsints[start_digit] <= 3 and start_digit != -1:no += 1
    for x in range(1,4):
        if inputsints.count(start+x) == 1:
            no += noways(inputsints.index(start+x),maximum)
    return no
main()