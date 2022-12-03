import aoc_utils
import functools
import itertools
import more_itertools as itertools
import string
lines = aoc_utils.readLines()
def getscore(words): return string.ascii_letters.index(functools.reduce(set.intersection,(set(x) for x in words)).pop()) + 1
print(sum(map(lambda x: getscore([x[len(x)//2:],x[:len(x)//2]]),lines)))
print(sum(map(getscore,itertools.chunked(lines,3))))
