import aoc_utils
import itertools
nums = aoc_utils.numericGrid(separator = " ")
def getnext(sequence):
    diffs = [b-a for a,b in itertools.pairwise(sequence)]
    return sequence[-1] + (getnext(diffs) if any(diffs) else 0)
print(sum(map(getnext, nums)))
print(sum(map(lambda x: getnext(x[::-1]), nums)))
