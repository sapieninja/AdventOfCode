import aoc_utils
from collections import *
import itertools
lines = aoc_utils.readlines()
count = 0
cor = [["a","b","c","f","e","g"],["c","f"],["a","c","d","e","g"],["a","c","d","f","g"],["b","c","d","f"],["a","b","d","f","g"],["a","b","d","e","f","g"],["a","c","f"],["a","b","c","d","e","f","g"],["a","b","c","d","f","g"]]
for line in lines:
    possibilities = defaultdict(set)
    truth = {}
    start,end = line.split("|")
    start = start.split()
    end = end.split()
    for part in itertools.chain(start):
        definite = set()
        for possibility in cor:
            if len(possibility) == len(part):
                if len(definite) == 0:
                    definite = set(possibility)
                else:
                    definite = definite.intersection(set(possibility))
        for segment in definite:
            if len(possibilities[segment]) == 0:
                possibilities[segment] = set(part)
            else:
                possibilities[segment] = possibilities[segment].intersection(set(part))
    while len(truth) != 7:
        for i in possibilities.keys():
            if len(possibilities[i]) == 1:
                truth[i] = list(possibilities[i])[0]
        for i in possibilities.keys():
            for p in truth.values():
                if p in possibilities[i]:
                    possibilities[i].remove(p)
    out = ""
    for part in end:
        actual = []
        for x in part:
            for i in truth.keys():
                if truth[i] == x:
                    actual.append(i)
        for i in range(len(cor)):
            if set(actual) == set(cor[i]):
                out += str(i)
    count += int(out)
print(count)

