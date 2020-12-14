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
import math
lines = aoc_utils.readlines()
addresses = {}
for x in lines:
    if x[0:3] == "mem":
        address = int(re.search(r"\[(.*)\]",x).group(1))
        wvalue = int(x.split()[2])
        value = int(address)
        value = "{0:b}".format(value)
        value = value.zfill(36)
        newvar = ''
        for x in range(len(value)):
            if mask[x]=="0":
                newvar += value[x]
            elif mask[x] == "1":
                newvar += "1"
            else:
                newvar += "X"
        combinations = []
        xv = 0
        maxv = pow(2,newvar.count('X'))
        for y in range(xv,maxv):
            workingvar = newvar
            binxv = "{0:b}".format(y).zfill(newvar.count('X'))
            for z in binxv:
                workingvar = workingvar.replace('X',z,1)
            addresses[int(workingvar)] = int(wvalue)
    else:
        mask = x.split()[2] 
print(sum(addresses.values()))
