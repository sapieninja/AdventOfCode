import aoc_utils
import re
passlines = aoc_utils.readlines()
sumnumbers = 0
for passline in passlines:
    (lower,upper) = (int((a:=re.match("^(.*)-(.*\w+)",passline)).group(0)),int(a.group(1)))
    no = passline.count(passline[4]) - 1
    if lower <= no and no <= upper:
        sumnumbers += 1
print(sumnumbers)