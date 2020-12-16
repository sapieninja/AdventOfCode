import aoc_utils
import datetime

si = aoc_utils.read()
starting_nos = list(map(int,si.split(',')))
x = 1
p = [-1 for x in range(30000000)] 
previous = 0
for sno in starting_nos:
    p[sno] = x
    previous = sno
    x+=1
first = True
while True:
    if first:
        nextout = 0
    else:
        nextout = x-p[previous]-1
    if p[nextout] == -1:
        first = True
    else:
            first = False
    p[previous] = x-1
    previous = nextout
    if x == 2020:
        print(nextout)
    if x == 30000000:
        print(nextout)
        break
    x+= 1
