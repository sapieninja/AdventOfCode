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

lines = aoc_utils.readSplittedLines(",")


def getxy(into):
    return map(int, into.split("-"))


def isValid(line):
    (a, b), (c, d) = getxy(line[0]), getxy(line[1])
    return a <= d and c <= b


print(len(list(filter(isValid, lines))))
