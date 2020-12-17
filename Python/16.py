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
tickets = aoc_utils.readlines()
rules = []
myticketnext = False
ot = []
for ticket in tickets:
    if ticket.count("or") != 0:
        name,rule = ticket.split(":")
        first,_,second = rule.split()
        rules.append((name,(int(first.split('-')[0]),int(first.split('-')[1])),(int(second.split('-')[0]),int(second.split('-')[1]))))
    elif myticketnext == False:
        if ticket!="nearby tickets:" and ticket!="your ticket:":
            ot.append(list(map(int,ticket.split(','))))
    else:
        myticket = list(map(int,ticket.split(',')))
    myticketnext = False
    if ticket == "your ticket:":
        myticketnext = True
gt = []
output = 0
for x in ot:
    tg = True
    for y in x:
        io = False
        for rule in rules:
            if y >= rule[1][0] and y <= rule[1][1] or y >= rule[2][0] and y <= rule[2][1]:
                io = True
        if io == False:
            output +=y 
            tg = False
    if tg == True:
        gt.append(x)
print(output)
co = zip(*reversed(gt))
wo = []
for x in co:
    wf = []
    for rule in rules:
        works = True
        for val in x:
            first = True
            second = True
            if val < rule[1][0] or val > rule[1][1]:
                first = False
            if val < rule[2][0] or val > rule[2][1]:
                second = False
            if first==False and second==False:
                works = False
        if works == True:
            wf.append(rule[0])
    wo.append(wf)
an = {}
while len(an) != len(gt[0]):
    for x in range(len(wo)):
        if len(wo[x]) == 1:
            an[x] = wo[x][0]
    values = list(an.values())
    for x in wo:
        for value in values:
            if value in x:
                x.remove(value)
output = 1
for x in range(len(myticket)):
    if an[x].startswith('departure'):
        output*=myticket[x]
print(output)
