from collections import *
import itertools
import random
import re
import sys
import aoc_utils
import queue
from operator import *
import functools
def main():
    inputs = aoc_utils.readlines()
    old_inputs = [x for x in inputs]
    while True:
        inputs = step(inputs)
        if inputs == old_inputs:
            break
        old_inputs = [x for x in inputs]
    count = 0
    for x in inputs:
        for y in x:
            if y == "#":
                count+=1
    print(count)
def generatenextcoords(x,y,xplus,yplus,inputs):
    yield (x + xplus,y+yplus)
    while True:
        x += xplus;y += yplus
        try:
            if(x<0 or y < 0):
                break
            inputs[x][y]
            yield (x,y)
        except:
            break
def step(inputs):
    length = len(inputs[0])
    newlist = [x for x in inputs]
    for x in range(len(inputs)):
        for y in range(length):
            if inputs[x][y] == "L":
                nearby = []
                if x != len(inputs) - 1:
                    xplus = True
                else: xplus = False
                if x != 0:
                    xminus = True
                else: xminus = False
                if y != length - 1:
                    yplus = True
                else:
                    yplus = False
                if y != 0:
                    yminus = True
                else:yminus = False
                if xplus and yplus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,1,1,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if xplus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,1,0,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if xplus and yminus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,1,-1,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if yplus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,0,1,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if yminus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,0,-1,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if xminus and yplus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,-1,1,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if xminus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,-1,0,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if xminus and yminus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,-1,-1,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if "#" in nearby:
                    continue;
                else: newlist[x] = newlist[x][:y] + "#" + newlist[x][y+1:]
            elif inputs[x][y] == "#":
                nearby = []
                if x != len(inputs) - 1:
                    xplus = True
                else: xplus = False
                if x != 0:
                    xminus = True
                else: xminus = False
                if y != length - 1:
                    yplus = True
                else:
                    yplus = False
                if y != 0:
                    yminus = True
                else:yminus = False
                if xplus and yplus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,1,1,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if xplus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,1,0,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if xplus and yminus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,1,-1,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if yplus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,0,1,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if yminus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,0,-1,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if xminus and yplus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,-1,1,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if xminus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,-1,0,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                if xminus and yminus:
                    try:
                        nearby.append(inputs[(a:=next(x for x in generatenextcoords(x,y,-1,-1,inputs) if inputs[x[0]][x[1]]!="."))[0]][a[1]])
                    except:
                        pass
                amount = len([x for x in nearby if x=="#"])
                if amount >= 5:
                    newlist[x] = newlist[x][:y] + "L" + newlist[x][y+1:]
    return newlist
        
main()