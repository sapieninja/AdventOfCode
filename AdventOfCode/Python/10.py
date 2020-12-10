from collections import *
import itertools
import random
import re
import sys
import aoc_utils
import queue
cache = {}
def main():
    inputsints = aoc_utils.readints()
    no_one = 0
    no_three = 1
    inputsints.sort()
    if inputsints[0] == 1:no_one+=1
    elif inputsints[1] ==3: no_three +=1 
    for x in range(len(inputsints)-1):
        if inputsints[x+1] - inputsints[x] == 1: no_one += 1
        elif inputsints[x+1] - inputsints[x] == 3: no_three += 1
    print("Part One: ",no_one*no_three)
    print("Part Two: ",noways(inputsints,-1,max(inputsints) + 3 ))
def noways(inputs,start_digit,maximum):
    #if start_digit in cache:
    #    return cache[start_digit]
    no = 0
    if start_digit == -1:start = 0
    else:start = inputs[start_digit]
    if start_digit == len(inputs) - 1: return 1
    if maximum - inputs[start_digit] <= 3 and start_digit != -1:no += 1
    for x in range(1,4):
        if inputs.count(start+x) == 1:
            no += noways(inputs,inputs.index(start+x),maximum)
    #cache[start_digit] = no
    return no
main()