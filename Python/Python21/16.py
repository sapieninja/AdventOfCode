import aoc_utils
import itertools
import functools
from operator import *
import networkx
import math
from collections import *
from copy import deepcopy
import random
import re
msg = aoc_utils.read()
#greedy parser
def vn(packet):
    output = int(packet[0:3],2)
    print(output,packet)
    t = int(packet[3:6],2)
    packet = packet[6:]
    if t == 4:
        out = ""
        print(4,packet)
        while True:
            prev = packet[0]
            if prev =="1":
                out += packet[1:5]
                packet = packet[5:]
            else:
                out += packet[1:5]
                packet = packet[5:]
                break
        print(out)
        return (int(out,2),len(packet))


    else:
        subpackets = []
        i = int(packet[0])
        print("parsing mode",i,int(packet[1:16],2),int(packet[1:12],2))
        if i == 0:
            l = int(packet[0:16],2)
            packet = packet[16:]
            totake = packet[0:l]
            offset = len(packet) - l
            packet = packet[l:]
            while l>0:
                value,remaining = vn(totake)
                l-=(len(totake)-remaining)
                subpackets.append(value)
                totake = totake[-remaining:]
        else:
            l = int(packet[1:12],2)
            packet = packet[12:]
            for i in range(l):
                value,remaining = vn(packet)
                packet = packet[-remaining:]
                if remaining == 0:
                    packet = ""
                subpackets.append(value)
    output = 0 
    if t == 0:
        output = sum(subpackets)
    if t == 1:
        output = math.prod(subpackets)
    if t == 2:
        output = min(subpackets)
    if t == 3:
        output = max(subpackets)
    if t == 5:
        output = subpackets[0] > subpackets[1]
    if t==6:
        output = subpackets[0] < subpackets[1] 
    if t==7:
        output = subpackets[0] == subpackets[1]


    return (output,len(packet)) #give the output and the number of bits left for other parsers
into = bin(int(msg,16))[2:]
into = into.zfill(len(msg)*4)
print(into)
print(vn(into)[0])

