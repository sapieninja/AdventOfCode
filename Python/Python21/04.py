import aoc_utils
import itertools
import functools
import operator
import networkx
import math
from collections import *
from copy import deepcopy
import random
import re

lines = aoc_utils.readlines()
numbers = list(map(int, lines[0].split(",")))
groups = []
scores = []


def calcscore(group, current):
    total = 0
    for line in group:
        for number in line:
            if number != -1:
                total += int(number)
    scores.append(total * current)


def checkwin(group):
    for line in group:
        if sum(line) == -5:
            return True
    for x in range(5):
        if sum([line[x] for line in group]) == -5:
            return True
    return False


for line in lines[1:]:
    if line == "":
        groups.append([])
    else:
        groups[-1].append(list(map(int, line.split())))
for number in numbers:
    for group in groups:
        for line in group:
            if number in line:
                line[line.index(number)] = -1
    for group in groups:
        if checkwin(group):
            calcscore(group, number)
    groups = list(filter(lambda group: checkwin(group) == False, groups))
print("Part 1:", scores[0])
print("Part 2:", scores[-1])
