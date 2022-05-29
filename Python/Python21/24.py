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
import sys
import sympy
lines = aoc_utils.readlines()
values = {}
counter = 1
simplifications = {}
linecounter = 0
sublines = []
for line in lines:
    if line.startswith("inp"):
        sublines.append([])
    sublines[-1].append(line)
print(sublines)
lastz = "0"
statements = {}
values = {}
for x in "abcdefghijklmnopqrstuvwxyz":
    values[x] = "0"
for x in range(-1000,1000):
    values[str(x)] = str(x)
for line in lines:
    linecounter += 1
    splitted = line.split()
    if line.startswith("inp"):
        values[splitted[-1]] =  "INP" + str(counter)
        counter += 1
    if line.startswith("add"):
        if values[splitted[-1]] == "0":
            pass
        elif values[splitted[-2]] == "0":
            values[splitted[-2]] = values[splitted[-1]]
        else:
            values[splitted[-2]] = "(" + values[splitted[-1]] +"+"+ values[splitted[-2]] +")"
    if line.startswith("mul"):
        if values[splitted[-1]] == "0" or values[splitted[-2]] == "0":
            values[splitted[-2]] = "0"
        elif values[splitted[-1]] == "1":
            pass
        else:values[splitted[-2]] = "(" + values[splitted[-1]] +"*"+ values[splitted[-2]] +")"
    if line.startswith("div"):
        if values[splitted[-1]] == "1":
            pass
        elif values[splitted[-1]] != "0":
            values[splitted[-2]] = "(" + values[splitted[-2]] +"//"+ values[splitted[-1]] +")"
    if line.startswith("mod"):
        if values[splitted[-2]] == "0":
            pass
        elif values[splitted[-1]] == "1":
            pass
        else:
            values[splitted[-2]] = "(" + values[splitted[-2]] +"%"+ values[splitted[-1]] +")"
    if line.startswith("eql"):
        if values[splitted[-2]] == values[splitted[-1]]:
            values[splitted[-2]] = "1"
        else:
            values[splitted[-2]] = "int(" + values[splitted[-1]] +"=="+ values[splitted[-2]] +")"
    if "INP" not in values[splitted[1]] and "S" not in values[splitted[1]]:
        values[splitted[1]] = str(eval(values[splitted[1]]))
    else:
        for value in re.findall(r"S\d*",values[splitted[1]]):
            for i in statements:
                if statements[i] == value:
                    break
            values[splitted[1]] = values[splitted[1]].replace(value,i)
        for value in statements:
            if value in values[splitted[1]]:
                values[splitted[1]] = values[splitted[1]].replace(value,statements[value])
        if values[splitted[1]] in statements:
            values[splitted[1]] = statements[values[splitted[1]]]
        else:
            if re.fullmatch(r"S(\d)*",values[splitted[1]]):
                continue
            number = "S" + str(len(statements))
            statements[values[splitted[1]]] = number
statements = {value : key for (key, value) in statements.items()}
for x in statements:
    print(x, "->",statements[x])
def evaluate(number):
    for x in range(len(str(number))):
        exec("INP" + str(x) + "=" + str(number)[x])
    newstatements = {}
    for statement in statements:
        value = statements[statement]
        while "S" in value:
            for match in re.findall(r"S\d+",value):
                value = value.replace(match,newstatements[match])
        newstatements[statement] = str(eval(value))
    print(newstatements["S150"])
    return newstatements["S150"]=="0"
print(evaluate(31521119151421))
