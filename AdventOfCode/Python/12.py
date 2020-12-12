from collections import *
import itertools
import random
import re
import sys
import aoc_utils
import queue
from operator import *
import functools
from copy import deepcopy
def solve(part2 = False):
    inputs = aoc_utils.readlines()
    de = 0
    dn = 0
    if part2:
        dn = 1
        de = 10
    sn = 0
    se = 0
    directions = ["E", "S", "W", "N"]
    direction = 0
    for x in inputs:
        if x[0] == "F" and not part2:
            x = directions[(direction//90)%4] + x[1:]
        choice = x[0]
        number = int(re.search('\d+',x).group())
        if choice == "N": dn += number
        if choice == "S": dn -= number
        if choice == "E": de += number
        if choice == "W": de -= number
        if choice == "L" and not part2: direction -= number
        if choice == "R"and not part2: direction += number
        if choice == "L" and part2: (de,dn) = rotate(de,dn,number,True)
        if choice == "R" and part2: (de,dn) = rotate(de,dn,number)
        if choice == "F" and part2:
            se += number * de
            sn += number * dn
    if part2: return abs(sn) + abs(se)
    return abs(de) + abs(dn)
def rotate(de,dn,degrees,l = False):
    degrees //= 90
    for x in range(degrees):
        if not l:
            temp = dn
            dn = -de
            de = temp
        else:
            temp = dn
            dn = de
            de = -temp
    return (de,dn)
print("Part 1:",solve())
print("Part 2:",solve(True))

