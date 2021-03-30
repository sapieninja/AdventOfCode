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
def findsnake(grid):
    snake = ((1,-1),(3,0),(1,1),(1,0),(1,-1),(3,0),(1,1),(1,0),(1,-1),(3,0),(1,1),(1,1),(0,-1),(1,0))
    counter = 0
    for x in range(len(grid[0])):
        for y in range(len(grid[0])):
            if grid[x][y] == "#":
                present = True
                dx = 0
                dy = 0
                for shift in snake:
                    dy += shift[0]
                    dx += shift[1]
                    if (x+dx)>=len(grid[0])-1 or (y+dy)>=len(grid[0])-1:
                        present = False
                        break
                    else:
                        if grid[x+dx][y+dy] != "#":
                            present = False
                if present:
                    counter += 1
    return counter
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
    og = deepcopy(out)
    for f in range(0,3):
        for p in range(0,4):
            count = 0
            for row in out:
                for column in row:
                    if column == "#":count+=1
            value = findsnake(out)
            if value!=0:
                print(count-value*15)
            out = rotate(out,1)
        out = og
        out = flip(out,1)
def bgrid(board,ops,nt):
    ob = [[0 for p in board[0]] for x in board[0]]
    length = len(board[0])
    placed = set()
    op = -1
    i = 0
    while len(list([x for x in itertools.chain.from_iterable(x for x in ob) if x==0]))>0:
        # print(placed)
        if len(placed) == op:
            placed = set()
            ob = [[0 for y in board[0]] for x in board[0]]
            i += 1
            continue
        op = len(placed)
        if len([x for x in list(itertools.chain.from_iterable(x for x in ob)) if x ==0]) == len(list(itertools.chain.from_iterable(ob))):
            #we will now place the central piece in the board
            ob[length//2][length//2] = rotate(P[board[length//2][length//2]],i//3)
            ob[length//2][length//2] = flip(ob[length//2][length//2],i%3)
            placed.add(board[length//2][length//2])
        else:
            for x in range(length):
                for y in range(length):
                    if ob[x][y] == 0:
                        dx = 0
                        dy = 0
                        if x != 0:
                            if ob[x-1][y] != 0:
                                dx,dy = -1,0 
                                mb = ob[x-1][y][-1]
                        if x!= length-1:
                            if ob[x+1][y] != 0:
                                dx,dy = 1,0
                                mb = ob[x+1][y][0]
                        if y != 0:
                            if ob[x][y-1] != 0:
                                dx,dy = 0,-1
                                mb = [item[-1] for item in ob[x][y-1]]
                        if y != length -1:
                            if ob[x][y+1] != 0:
                                dx,dy = 0,1
                                mb = [item[0] for item in ob[x][y+1]]
                        if dx!=0 or dy!=0:
                            #idk the key for the new position so we are just going to have to work out the grid for here :) 
                            #i will simply do this by trying all the options
                            #it will probably take a few hours to run
                            #but at least it will run :)
                            #so to business
                            # print(dx,dy)
                            for key in P.keys():#iterate through every key however we do need a way of excluding the same grid from happening twice
                                if key in placed:
                                    continue
                                grid = P[key]
                                og = deepcopy(grid)
                                for p in range(0,3):
                                    for q in range(0,4):
                                        test = []
                                        if  dx==-1 :test = grid[0]
                                        elif dx== 1:test = grid[-1]
                                        elif dy==-1:test = [item[0]  for item in grid]
                                        elif dy==1: test = [item[-1] for item in grid]
                                        if str(mb)==str(test):
                                            ob[x][y] = grid
                                            placed.add(key)
                                        grid = rotate(grid,1)
                                    grid = og
                                    grid = flip(grid,p)
    length = len(ob[0][0][0])
    for p in range(len(ob[0])):
        for q in range(len(ob[0])):
            grid = ob[p][q]
            ob[p][q] = [[ob[p][q][y][x] for x in range(length) if x!=0 and x!=length-1] for y in range(length) if y!=0 and y!=length-1]
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
