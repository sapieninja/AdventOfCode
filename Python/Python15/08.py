import aoc_utils
str_used = 0
code_used = 0
for x in aoc_utils.readlines():
    code_used += len(x)
    str_used += len(x) + 2
    str_used += x.count('"')
    str_used += x.count("\\")
print(str_used - code_used)
