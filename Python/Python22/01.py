import aoc_utils
import itertools
import functools
import operator
import networkx as nx
import math
from collections import *
from copy import deepcopy
import random
import re
from string import ascii_lowercase as alph
nums = aoc_utils.readparagraphs()
values = []
for paragraph in nums:
    total = sum(map(int,paragraph))
    values.append(total)
values.sort()
print(values[-1]+values[-2]+values[-3])
