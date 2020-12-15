import aoc_utils

si = aoc_utils.read()
starting_nos = list(map(int,si.split(',')))
x = 1
p = {}
previous = 0
while True:
    if x<=len(starting_nos):
        nextout = starting_nos[x-1]
        first = True
    else:
        if first:
            nextout = 0
        else:
            nextout = x-p[previous]-1
        if not nextout in p:
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
