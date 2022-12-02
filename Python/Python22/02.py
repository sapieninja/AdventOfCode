import aoc_utils
lines = aoc_utils.readSplittedLines(" ")
print(sum(map(lambda i:('XYZ'.index(i[1])+1) + (('ZXY'.index(i[1])-'ABC'.index(i[0]))%3)*3,lines)))
print(sum(map(lambda i:(('XYZ'.index(i[1])+'BCA'.index(i[0]))%3 + 1) + 'XYZ'.index(i[1])*3,lines)))
