from collections import *
import itertools
import random
import re
import sys
import aoc_utils
import queue
def main():
    ints = aoc_utils.readints()
    start = 25
    for x in range(start,len(ints)-1):
        value = ints[x]
        previous = ints[x-25:x]
        if not sumto(value,previous):
            print("Part One:",value)
            print("Part Two:",findsumofrange(value,ints))
def findsumofrange(value,ints):
    for x in range(len(ints)-1):
        sum = ints[x]
        counter = 1
        while(sum < value):
            sum += ints[x+counter]
            counter += 1
        if sum == value:
            contiguous = ints[x:x+counter]
            return max(contiguous) + min(contiguous)
def sumto(value,list):
    for x in list:
        for y in list:
            if x + y == value and x != y:
                return True
    return False
main()