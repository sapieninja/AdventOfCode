import aoc_utils
from collections import *
lines = aoc_utils.readLines()
total = 0
num = defaultdict(int)
total = 0
for gameid,game in enumerate(lines,start=1):
    game = game.split(":")[1]
    winning, have = game.split("|")
    winning = [int(x) for x in winning.split(" ") if x!=""]
    have    = [int(x) for x in have.split(" ") if x!=""]
    amount = 0
    for item in have:
        if item in winning:
            amount += 1
    total += 2**(amount - 1) if amount > 0 else 0
    num[gameid] = amount
copies = defaultdict(int)
for gameid in sorted(list(num.keys()),reverse=True):
    copies[gameid] += 1
    for item in range(gameid+1, gameid + num[gameid]+1):
        copies[gameid] += copies[item]
print(total)
print(sum(list(copies.values())))
