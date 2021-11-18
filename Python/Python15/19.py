import aoc_utils
import re
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
for line in lines:
    f = line.split()[0]
    t = line.split()[2]
    for x in range(molecule.count(f)):
        changeset.add(replacen(molecule,f,t,x))
print(len(changeset))
