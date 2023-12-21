import aoc_utils
import itertools
import functools
import operator
import math
import graphviz
import matplotlib.pyplot as plt
from collections import *
from copy import deepcopy
import random
import networkx as nx
import re
from string import ascii_lowercase as alph
instrs = aoc_utils.readLines()
instructions = {}
symbols = {}
for instr in instrs:
    name, result = instr.split(" -> ")
    if name == "broadcaster":
        instructions[name] = result
    else:
        symbol = name[0]
        name = name[1:]
        instructions[name] = result
        symbols[name] = symbol
conjunctions = defaultdict(dict)
for instruction in instructions.keys():
    for dest in instructions[instruction].split(", "):
        if dest in symbols:
            if symbols[dest] == "&":
                conjunctions[dest][instruction] = False
flipflops = defaultdict(bool)
clow = 0
chigh = 0
def processpulses():
    global chigh
    global clow
    Q = deque()
    Q.append(("broadcaster", False,"button"))
    while Q:
        name, high, sent = Q.popleft()
        if name == "rx" and not high:
            return True
        if high: chigh += 1
        else: clow += 1
        if name not in instructions:
            continue
        if name == "broadcaster":
            for dest in instructions[name].split(", "):
                Q.append((dest, False,name))
            continue
        symbol = symbols[name]
        if symbol == "%":
            if not high:
                if not flipflops[name]:
                    for dest in instructions[name].split(", "):
                        Q.append((dest, True,name))
                    flipflops[name] = True
                else:
                    for dest in instructions[name].split(", "):
                        Q.append((dest, False,name))
                    flipflops[name] = False
        if symbol == "&":
            conjunctions[name][sent] = high
            if all(conjunctions[name].values()):
                for dest in instructions[name].split(", "):
                    Q.append((dest, False ,name))
            else:
                for dest in instructions[name].split(", "):
                    Q.append((dest, True ,name))
for _ in range(1000):
    processpulses()
print(clow*chigh)
G = graphviz.Digraph("visualisation")
for instruction in instructions: 
    for dest in instructions[instruction].split(", "):
        isymbol = ""
        dsymbol = ""
        if instruction in symbols:
            isymbol += symbols[instruction]
        if dest in symbols:
            dsymbol += symbols[dest]
        G.edge(isymbol + instruction,dsymbol + dest)
G.render("visualisation.gv",view=True)
