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
p1,p2 = aoc_utils.readlines()
p1,p2 = int(p1),int(p2)
tocheck,counter = 1,0
while tocheck!=p1:
    tocheck = (tocheck*7)%20201227
    counter += 1
print(pow(p2,counter)%20201227)
