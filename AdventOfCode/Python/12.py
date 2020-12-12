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
    de,dn,sn,se,direction,directions = 10 if part2 else 0,1 if part2 else 0,0,0,0,list("ESWN")
    for x in inputs:
        if x[0] == "F" and not part2: x = directions[(direction//90)%4] + x[1:]
        dn,de,direction,se,sn= dn + int(x[1:]) if x[0] == "N" else (dn -int(x[1:]) if x[0] == "S" else dn),de + int(x[1:]) if x[0] == "E" else (de-int(x[1:]) if x[0] == "W" else de),direction + int(x[1:]) if (x[0] == "R" and not part2) else (direction - int(x[1:]) if x[0] == "L" else direction),se+de*int(x[1:]) if (x[0] == "F" and part2) else se,sn+dn*int(x[1:]) if (x[0] == "F" and part2) else sn
        if x[0] == "L" and part2: 
            for y in range(int(x[1:])//90):de,dn = -dn,de
        elif x[0] == "R" and part2:
            for y in range(int(x[1:])//90): de,dn = dn,-de
    return abs(sn) + abs(se) if part2 else abs(de) + abs(dn)
print("Part 1:",solve(),"\nPart 2:",solve(True))

