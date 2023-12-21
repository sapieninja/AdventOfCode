import aoc_utils
import itertools
import more_itertools as itertools
import functools
import operator
import networkx as nx
import math
from collections import *
from pprint import pprint
from copy import deepcopy
import random
import re
from string import ascii_lowercase as alph
lines = aoc_utils.readLines()
workflows = {} 
for i in range(len(lines)): 
    line = lines[i]
    if line == "":
        break
    name = line[:line.index("{")]
    rest = line[line.index("{"):]
    workflows[name] = rest
class Range:
    def __init__(self,minx,maxx,minm,maxm,mina,maxa,mins,maxs):
        self.minx = minx
        self.maxx = maxx
        self.minm = minm
        self.maxm = maxm
        self.mina = mina
        self.maxa = maxa
        self.mins = mins
        self.maxs = maxs
    def getsize(self):
        return (1+self.maxx-self.minx)*(1+self.maxm-self.minm)*(1+self.maxa-self.mina)*(1+self.maxs-self.mins)
    def applycondition(self,condition):
        minx = self.minx
        maxx = self.maxx
        minm = self.minm
        maxm = self.maxm
        mina = self.mina
        maxa = self.maxa
        mins = self.mins
        maxs = self.maxs
        if "<" in condition:
            var, no = condition.split("<")
            no = int(no)
            if var == "x":
                maxx = min(self.maxx, int(no) - 1)
            if var == "m":
                maxm = min(self.maxm, int(no) - 1)
            if var == "a":
                maxa = min(self.maxa, int(no) - 1)
            if var == "s":
                maxs = min(self.maxs, int(no) - 1)
        if ">" in condition:
            var, no = condition.split(">")
            no = int(no)
            if var == "x":
                minx = max(self.minx, int(no) + 1)
            if var == "m":
                minm = max(self.minm, int(no) + 1)
            if var == "a":
                mina = max(self.mina, int(no) + 1)
            if var == "s":
                mins = max(self.mins, int(no) + 1)
        if minx>maxx:
            minx = 1
            maxx = 1
        if minm>maxm:
            minm = 1
            maxm = 1
        if mina>maxa:
            mina = 1
            maxa = 1
        if mins>maxs:
            mins = 1
            mins = 1
        return Range(minx,maxx,minm,maxm,mina,maxa,mins,maxs)
def process(workflow, R):
    t= 0
    if workflow == "A":
       return R.getsize()
    if workflow == "R":
        return 0
    rules = workflows[workflow][1:-1].split(",")
    for rule in rules:
        if ":" in rule:
            condition, rule = rule.split(":")
            newRange = R.applycondition(condition)
            t+=process(rule,newRange)
            if "<" in condition:
                var, no = condition.split("<")
                no = int(no)
                condition = var + ">" + str(no - 1)
            else:
                var, no = condition.split(">")
                no = int(no)
                condition = var + "<" + str(no + 1)
            R = R.applycondition(condition)
        else:
           t+=process(rule, R)
    return t
print(process("in", Range(1,4000,1,4000,1,4000,1,4000)))
