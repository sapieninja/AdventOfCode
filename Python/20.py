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
P = {}
i = -1
p = 0
for line in lines:
    if line.startswith('Tile'):
        line = re.search(r"\d+",line).group(0)
        P[line] = [] 
        token = line
    else:
        grid = P[token]
        grid.append([])
        for character in line:
            grid[-1].append(character)
        P[token] = grid
def rotate(grid,i):
    for x in range(i):
        grid = list(list(x) for x in zip(*reversed(grid)))
    return list(grid)
def flip(grid,i):
    if i == -1:return grid
    if i == 0: return [list(reversed(x)) for x in grid]
    elif i == 1: return list(reversed(grid))
    elif i == 2: return list(reversed([list(reversed(x)) for x in grid]))
def neighbours(grid,grid2):
    og = deepcopy(grid)
    og2= deepcopy(grid2)
    if grid != grid2:
        for q in range(0,3):
            for z in range(0,4):
                for p in range(0,3):
                    for y in range(0,4):
                        if list(grid2[0]) == list(grid[0]):
                            return (True,q,z,p,y)
                        grid2 = rotate(grid2,1)
                    grid2 = og2
                    grid2 = flip(grid2,p)
                grid = rotate(grid,1)
            grid = og
            grid = flip(grid,q)
    return (False,0,0)
def main():
    nt = {}
    ops = {}
    out = 1
    for key in P.keys():
        non = 0
        if key not in nt:
            nt[key] = set()
        for key2 in P.keys():
            value = neighbours(P[key],P[key2])
            if value[0]:
                non += 1
                nt[key].add(key2)
                ops[key] = (value[1],value[2],value[3],value[4],key2) 
        if non == 2:
            out*=int(key)
    print("Part 1:",out)
    length = int(math.sqrt(len(P.keys())))
    board = boardgen(nt)
    out = bgrid(board,ops,nt)
    count = 0
    for row in out:
        for column in row:
            if column == "#":
                count += 1
    print("Part 2 mod 15 is:",count%15)
def bgrid(board,ops,nt):
    ob = [[0 for p in board[0]] for x in board[0]]
    for x in range(len(board[0])):
        for y in range(len(board[0])):
            key = board[x][y]
            neighbour = ops[key][4]
            grid =  P[key]
            grid = list(list(x) for x in grid)
            grid = flip(grid,ops[key][0]-1)
            grid = flip(grid,ops[key][3]-1)
            grid = rotate(grid,ops[key][1]) 
            if x!=0:
                if board[x-1][y] == neighbour:
                    grid = rotate(grid,3)
                    grid = flip(grid,1)
            if x!=len(board[x])-1:
                if board[x+1][y] == neighbour:
                    grid = rotate(grid,1)
                    grid = flip(grid,2)
            if y!=0:
                if board[x][y-1] == neighbour:
                    grid = rotate(grid,2)
            if y!=len(board[x])-1:
                if board[x][y+1] == neighbour:
                    grid = flip(grid,2)
                    grid = rotate(grid,1)
            grid = [[grid[y][x] for x in range(len(grid[0])) if x!=0 and x!=len(grid[0])-1] for y in range(len(grid)) if y!=0 and y!=len(grid)-1] 
            ob[x][y] = grid
    length = len(ob[0][0][0])
    out = [[0 for p in range(len(board[0]*length))] for x in range(len(board[0])*length)]
    for x in range(len(board[0])*length):
        for y in range(len(board[0])*length):
            out[x][y] = ob[x//length][y//length][x%length][y%length]
    return out
def boardgen(nt):
    length = int(math.sqrt(len(nt)))
    board = [[0 for x in range(length)] for y in range(length)]
    board[0][0] = next(x for x in nt if len(nt[x])==2)
    possible = set(nt.keys())
    possible.discard(str(board[0][0]))
    while len([0 for y in board if [x for x in y if x==0]!=[]])!=0:
        for num in range(length*2):
            for x in range(length):
                for y in range(length):
                    if x+y==num and board[x][y] == 0:
                        choices = possible 
                        if x!=0:
                            if board[x-1][y] != 0:choices = choices.intersection(nt[str(board[x-1][y])])
                        if y!=0:
                            if board[x][y-1] != 0:choices = choices.intersection(nt[str(board[x][y-1])])
                        if len(choices) == 1:
                            board[x][y] = list(choices)[0]
                            possible.remove(str(board[x][y]))
                        if num==1 and len(choices) == 2:
                            board[x][y] = sorted(list(choices))[0] #prevents undefined behaviour
                            possible.remove(str(board[x][y]))
    return board
main()
