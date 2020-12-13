import aoc_utils
import re
amount = 0
vowels = list('aioue')
for x in aoc_utils.readlines():
    if re.search(r"(..).*\1",x) is not None: 
        print("Half matched",x)
        if re.search(r"(.).\1",x) is not None:
            print("Matched:",x)
            amount += 1
    else:
        print(x)
print(amount)
