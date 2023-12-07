import aoc_utils
import itertools
import more_itertools as itertools
import functools
import operator
import networkx as nx
import math
from collections import *
from copy import deepcopy
import random
import re
from string import ascii_lowercase as alph
lines = aoc_utils.readLines()
poss = "AKQT98765432J"
#@functools.total_ordering
class Hand:
    def __init__(self, hand, bid):
        self.bid= bid
        self.hand = hand
    @property
    def type(self):
        #substituting same for all jokers always optimal
        most_common = Counter(self.hand).most_common(2)
        if most_common[0][0] != "J" or len(most_common) == 1:
            replacement = most_common[0][0]
        else:
            replacement = most_common[1][0]
        return Hand._typehand(self.hand.replace("J", replacement))
    @staticmethod
    def _typehand(hand):
        ordering = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
        nums = Counter(hand)
        return ordering.index(tuple(sorted(nums.values(),reverse=True)))
    def __lt__(self, other):
        if self.type < other.type:
            return True
        elif self.type > other.type:
            return False
        else:
            for card,ocard in zip(self.hand, other.hand):
                if poss.index(card) > poss.index(ocard):
                    return True
                elif poss.index(card) < poss.index(ocard):
                    return False
        return False
    def __eq__(self,other):
        return False
cards = []
bids = []
for num,line in enumerate(lines,start=1):
    card, bid = line.split(" ")
    cards.append(Hand(card, int(bid)))
cards.sort()
total = 0
for rank, card in enumerate(cards, start=1):
    total += rank*card.bid
print(total)
