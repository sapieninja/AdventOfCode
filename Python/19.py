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
dic = {}
nums = re.compile(r"\d+")
ms = []
for line in lines:
    if line.count(":") == 1:
        line = line.split(":")
        dic[line[0]] = line[1]
        if line[1].count('a') == 1: dic[line[0]] = 'a'
        elif line[1].count('b') == 1:dic[line[0]] = 'b'
    else:
        ms.append(line)
def main(part2=False):
    if part2:
        dic["8"] = dic["8"] + " | 42 8"
        dic["11"]= dic["11"] + " | 42 11 31"
        output = ""
        for x in range(1,20):
            v1 = " 42 "*x
            v2 = " 31 "*x
            output += f"{v1}{v2}|"
        output = output[:-1]
    def reval(matchobj):
        value = matchobj.group(0)
        if value != "8" and value != "11" or not part2:
            return "(" + dic[value]+ ")"
        else:
            if value == "8":
                return "(42)+"
            else:
                return "("+output+")"
    rout = dic["0"]
    while re.search(nums,rout):
        rout = re.sub(nums,reval,rout)
    rout = re.compile(rout.replace(" ","") + "$")
    count = 0
    for line in ms:
        if re.match(rout,line):
            print("     MATCHED         :",line)
            count += 1
        else:
            print("     NOT MATCHED     :",line)
    print(count)
main()
main(True)
