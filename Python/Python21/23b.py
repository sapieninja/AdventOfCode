import aoc_utils 
import itertools 
import functools
import heapq
import operator
import networkx as nx
import math
from collections import *
from copy import deepcopy
import random 
import re 
import time
import pprint
import sys
sys.setrecursionlimit(10000)
costs = [1,10,100,1000]
lines = aoc_utils.readlines()
positions = deepcopy(lines)
#we need to search through game states
for i in range(len(lines)):
    lines[i] = lines[i].replace("A",".")
    lines[i] = lines[i].replace("B",".") 
    lines[i] = lines[i].replace("C",".")
    lines[i] = lines[i].replace("D",".")
    poses = []
for x in range(len(lines)):
    for y in range(len(lines[0])):
        if lines[x][y] == ".":
            poses.append((x,y))
start = []
order = "AAAABBBBCCCCDDDD"
while len(order) != 0:
    for x in range(len(positions)):
        for y in range(len(positions[0])):
            if len(order) == 0:
                break
            if positions[x][y] == order[0]:
                order = order[1:]
                start.append((x,y)) 
def getpossible(state,i):
    tovisit = deque()
    tovisit.append(state[i])
    visited = {}
    visited[state[i]] = 0
    while len(tovisit) != 0:
        visiting = tovisit.pop()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            new = (visiting[0] + dx, visiting[1] + dy)
            if new in state or new in visited or new not in poses:
                continue
            tovisit.append(new)
            visited[new] = visited[visiting] + 1
    for i in visited:
        if visited[i] == 0:
            break
    visited.pop(i)
    return visited

def getneighbours(state):
    #if moving one to a hole is possible always do that, and don't move out of a completed hole
    toreturn = set()
    destinations = [3,5,7,9]
    for pos in range(len(state)):
        fee = costs[pos//4]
        usage = list(state)
        oldstate = state[pos]
        possibilities = getpossible(state,pos)
        destination = destinations[pos//4]
        if pos%2 == 0:
            other = pos + 1
        else:
            other = pos - 1
        for possibility in possibilities:
            #first check if destination is empty
            if possibility[0] != 1 and possibility[1] == destination:
                others = getothers(state,pos)
                if (3,destination) in state and (3,destination) not in others:
                    continue
                if (4,destination) in state and (4,destination) not in others:
                    continue
                if (5,destination) in state and (5,destination) not in others:
                    continue
                toreturn = set()
                usage[pos] = possibility
                toreturn.add((tuple(usage),possibilities[possibility]*fee))
                return toreturn
            if oldstate[0] == 1 and possibility[0] == 1: #hall mmonitor
                if oldstate[1] != possibility[1]:
                    continue
            if possibility[0] == 1 and possibility[1] in (3,5,7,9): #don't stop in the way of a door
                continue
            if possibility[0] != 1 and possibility[1] != destination:
                continue

            #we have already done the logical movement into holes
            #all other movement is illogical
            usage[pos] = possibility
            toreturn.add((tuple(usage),possibilities[possibility]*fee))
    return toreturn
def getvalidity(state):
    poses = (3,5,7,9)
    for i in range(len(state)):
        destination = poses[i//4]
        current = state[i]
        if current[1] != destination:
            return False
        others = getothers(state,i)
        for current in others:
            if current[1] != destination:
                return False
    return True
def getothers(state,i):
    start = (i//4)*4
    out = []
    for x in range(4):
        out.append(state[start+x])
    return out
node = (0,tuple(start))
frontier = [node]
explored = set()
infrontier = set()
infrontier.add(node)
last = 0
while True:
    if len(frontier) == 0:
        assert "FAILURE"
    node = heapq.heappop(frontier)
    if node[0] > last:
        last = node[0]
        print(node[0])
    if node[1] in explored:
        continue
    if getvalidity(node[1]):
        print(node[0])
        break
    explored.add(node[1])
    for neighbour in getneighbours(node[1]):
        n = ((neighbour[1]+node[0]),neighbour[0])
        if n[1] not in explored:
            if n not in frontier:
                heapq.heappush(frontier,n)
            else:
                for i in range(len(frontier)):
                    if frontier[i][1] == n[1]:
                        if frontier[i][0] > n[0]:
                            frontier.pop(i)
                            heapq.heappush(frontier,n)
                            break
