import aoc_utils
import functools
import re
import random
lines = aoc_utils.readlines()
molecule = lines[-1]
lines = lines[:-1]
changeset = set()
def replacen(string,f,t,n):
    index = -1
    for x in range(n+1):
        index = string.index(f,index+1)
    string = string[:index] + t + string[index+len(f):]
    return string
def findlength(string):
    output = 0
    if string == "e":
        return 0
    changeset = set()
    for line in lines:
        t = line.split()[0]
        f = line.split()[2]
        for x in range(string.count(f)):
            changeset.add(replacen(string,f,t,x))
    changeset=sorted(list(changeset),key=len)
    checkable=[]
    for x in changeset:
        if len(x) == len(changeset[0]):
            checkable.append(x)
    return findlength(random.choice(checkable)) + 1

print(findlength(molecule))
