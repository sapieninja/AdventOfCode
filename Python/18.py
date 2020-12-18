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
    print(len(x))
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
                print("oldx",x,x[0:characterx],x[index:len(x)])
                x = x[0:characterx] + evaluate(x[characterx+1:index]) + x[index+1:len(x)]
                print("newx",x)
                break
    nop = len(x)//2
    index = 0
    numbers = re.findall(r"\d+",x)
    value = int(numbers[0])
    operators = re.findall(r"\*|\+|\/|\-",x)
    print(operators)
    print(numbers)
    for y in range(len(operators)):
        print(y)
        print(numbers[y+1])
        print("Expression:",f"{value}{operators[y]}{numbers[y+1]}")
        value = eval(f"{value}{operators[y]}{numbers[y+1]}")
    return str(value)
for x in lines:
    su+=int(evaluate(x))
print(su)
