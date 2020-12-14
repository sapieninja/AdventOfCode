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
        value = x.split()[2]
        value = int(value)
        value = "{0:b}".format(value)
        value = value.zfill(36)
        newvar = ''
        for x in range(len(value)):
            if mask[x]=="X":
                newvar += value[x]
            else:
                newvar += mask[x]
        addresses[address] = int(newvar,2)
    else:
        mask = x.split()[2] 
print(sum(addresses.values()))
