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
import datetime
from copy import deepcopy
order = aoc_utils.read()
cups = list(map(int,order))
maximum =max(cups)
cups = cups + [x for x in range(maximum+1,1000001)]
maximum =max(cups)
class Node:
    def __init__(self,pv,no,payload):
        self.pv = pv
        self.no = no
        self.payload = payload
    def __repr__(self):
        return f"{self.payload}"
class Dll:
    def __init__(self,iterator):
        startnode = None
        maximum = max(iterator)
        dinos = {}
        for item in iterator:
            if startnode == None:
                startnode = Node(None,None,item)
                dinos[item] = startnode
                prevnode = startnode
            else:
                if item-1 in dinos:
                    pv = dinos[item-1] 
                else:
                    pv = None
                newnode = Node(pv,None,item) 
                dinos[item] = newnode
                if item+1 in dinos:
                    dinos[item+1].pv = newnode
                prevnode.no = newnode
                prevnode = newnode
        #we need to fix the edges
        #first the end of the array needs to be mapped to the beginning
        prevnode.no = startnode
        #second the first element in the array by order needs to be mapped to the end
        dinos[1].pv = dinos[maximum]
        self.cu = startnode
        self.dinos = dinos
        self.maximum = maximum
    def nextcur(self):
        self.cu = self.cu.no
        return self.cu
    def previous(self):
        return self.cu.pv
    def popnextcurrent(self):
        toreturn = self.cu.no
        self.cu.no = self.cu.no.no
        return toreturn
    def getgroup(self):
        return (self.popnextcurrent(),self.popnextcurrent(),self.popnextcurrent())
    def insert(self,node,newnode):
        node.no,newnode.no=newnode,node.no
        return newnode
    @property
    def getlist(self):
        toreturn = []
        while self.cu.no.payload not in toreturn:
            toreturn.append(self.nextcur().payload)
        return toreturn
    def getpart(self,num):
        start = self.dinos[num].no
        out = 1
        for x in range(2):
            out *= start.payload
            start = start.no
        print(out)
cups = Dll(cups)
for x in range(10000000):
    group = cups.getgroup()
    previous = cups.previous()
    while previous in group:
        previous = previous.pv
    for x in group:
        previous = cups.insert(previous,x)
    cups.nextcur()
cups.getpart(1)
