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


def isvalid(string):
    stack = []
    for x in string:
        if x == "{" or x == "[" or x == "(" or x == "<":
            stack.append(x)
        else:
            if x == ")":
                x = "("
            if x == "]":
                x = "["
            if x == ">":
                x = "<"
            if x == "}":
                x = "{"
            if x == stack[-1]:
                stack.pop(len(stack) - 1)
            else:
                print(x)
                if x == "(":
                    return 3
                if x == "[":
                    return 57
                if x == "{":
                    return 1197
                if x == "<":
                    return 25137
    return 0


def getstack(string):
    stack = []
    for x in string:
        if x == "{" or x == "[" or x == "(" or x == "<":
            stack.append(x)
        else:
            if x == ")":
                x = "("
            if x == "]":
                x = "["
            if x == ">":
                x = "<"
            if x == "}":
                x = "{"
            if x == stack[-1]:
                stack.pop(len(stack) - 1)
            else:
                if x == "(":
                    return 3
                if x == "[":
                    return 57
                if x == "{":
                    return 1197
                if x == "<":
                    return 25137
    return stack


lines = list(filter(lambda line: isvalid(line) == 0, lines))
scores = []
for line in lines:
    score = 0
    for character in reversed(getstack(line)):
        print(character)
        score *= 5
        if character == "(":
            score += 1
        if character == "[":
            score += 2
        if character == "{":
            score += 3
        if character == "<":
            score += 4
    scores.append(score)
print(sorted(scores)[len(scores) // 2])
