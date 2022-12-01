import aoc_utils
values = sorted(list(map(sum,aoc_utils.readIntParagraphs())))
print(values[-1])
print(values[-1]+values[-2]+values[-3])
