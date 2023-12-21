import aoc_utils
import itertools
import functools
import operator
import math
from collections import *
from copy import deepcopy
import random
import re
from string import ascii_lowercase as alph
lines =  aoc_utils.readLines()
dug = set()
current = (0,0)
dug = []
def interpret(hexcode):
    num = hexcode[2:-2] 
    num = int(num, base=16)
    instr = hexcode[-2]
    if instr == "0": 
        return ("R", num)
    if instr == "1": 
        return ("D", num)
    if instr == "2": 
        return ("L", num)
    if instr == "3": 
        return ("U", num)
length = 0
def generate():
    global length
    current = (0,0)
    for line in lines:
        dire, no, hexcode = line.split(" ")
        no = int(no)
        dire, no = interpret(hexcode)
        if dire == "R":
            current = (current[0], current[1] + no)
        if dire == "L":
            current = (current[0], current[1] - no)
        if dire == "U":
            current = (current[0]-no, current[1])
        if dire == "D":
            current = (current[0]+no, current[1])
        length += no
        yield current
def getarea(coords):
    A = 0
    for c,n in itertools.pairwise(coords):
        A += (n[1] + c[1])*(c[0]-n[0])/2
    return A
print(int(abs(getarea(generate()))+length/2+1))
