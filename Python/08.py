from collections import *
import itertools
import random
import re
import sys
import aoc_utils
import queue
def main():
    lines = aoc_utils.readlines()
    yield "Part 1: " + str(process(lines))
    for x in range(len(lines)):
        if lines[x][0:3] == "nop":
            lines[x] = "jmp" + lines[x][3:]
            yield process(lines)
            lines = aoc_utils.readlines()
        elif lines[x][0:3] == "jmp":
            lines[x] = "nop" + lines[x][3:]
            yield process(lines)
            lines = aoc_utils.readlines()
def process(lines):
    index = 0
    done = {}
    for index in range(len(lines)):
        done[index] = False
    accumulator = 0
    index = 0
    while True:
        if index < 0 or index >= len(lines):
            return "Part 2: " + str(accumulator)
        instruction = lines[index]
        if done[index]:
            return accumulator
        done[index] = True
        if instruction[0:3] == "nop": 
            index += 1
            continue
        elif instruction[0:3] == "acc":
            accumulator += int(re.search("[+-]\d+",instruction).group())
            index += 1
            continue
        elif instruction[0:3] == "jmp":
            index += int(re.search("[+-]\d+",instruction).group())
            continue

for value in main():
    if type(value) == type("string"):
        print(value)