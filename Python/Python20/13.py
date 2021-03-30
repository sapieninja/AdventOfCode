from collections import *
import itertools 
import random
import re
import sys
import aoc_utils
import queue
import modint
from operator import *
import functools
import math
from copy import deepcopy
inputs = aoc_utils.readlines()
time = int(inputs[0])
buses = [int(x) for x in inputs[1].split(',') if x != 'x']
minimum = 10000000000000000000000000000000000000000000
bus  = 0
for x in buses:
    print(x - time%x)
    print(minimum)
    if x - time%x <= minimum:
        minimum = x - time%x
        bus = x
bus_list = inputs[1].split(',')
#chinese remainder theorem
busx = [int(x) for x in bus_list if x!="x"]
busn = [int(x)-bus_list.index(x) for x in bus_list if x!="x"]
print(busx)
print(busn)
print(modint.chinese_remainder(busx,busn))
