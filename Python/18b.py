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
lines = aoc_utils.readlines()
su = 0
def evaluate(x):
    x = x.replace(" ","")
    while x.count("(") != 0: 
        for characterx in range(len(x)): 
            if x[characterx] == "(": 
                counter = 0
                for charx in range(characterx,len(x)):
                    if x[charx] == "(":
                        counter += 1
                    if x[charx] == ")":
                        counter -= 1
                    if counter == 0:
                        index = charx
                        break
                # print("oldx",x,x[0:characterx],x[index+1:len(x)])
                x = x[0:characterx] + evaluate(x[characterx+1:index]) + x[index+1:len(x)]
                # print("newx",x)
                break
    numbers = re.findall(r"\d+",x)
    operators = re.findall(r"\*|\+|\/|\-",x)
    nd = list(enumerate(operators))
    while not len(numbers) == 1:
        y = -1
        for p in nd:
            if p[1] == "+" or p[1] == "-":
                y = p[0]
                break
        if y == -1:
            y = 0
        # print("Expression:",f"{numbers[y]}{operators[y]}{numbers[y+1]}")
        value = eval(f"{numbers[y]}{operators[y]}{numbers[y+1]}")
        del numbers[y]
        del nd[y]
        del operators[y]
        for p in range(y,len(nd)):
            nd[p] = (nd[p][0] -1,nd[p][1])
        numbers[y] = value
    return str(numbers[0])
for x in lines:
    a=int(evaluate(x))
    print("value",a,x)
    su+=a
    print("total",su)
print(su)
