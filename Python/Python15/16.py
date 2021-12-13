import aoc_utils
import itertools
lines = aoc_utils.readlines()
sues = []
for line in lines:
    line = line.replace(",","")
    line = iter(line.split()[2:])
    sues.append(dict(zip(line,line)))
for sue in sues:
    print(sue)
aim = sues[0]
def valid(sue,im):
    for key in sue:
        if key == "cats:" or key == "trees:":
            if int(sue[key]) <= int(aim[key]):
                return False
        elif key == "pomeranians:" or key == "goldfish:":
            if int(sue[key]) >= int(aim[key]):
                return False
        elif sue[key] != aim[key]:
            return False
    return True
for x in range(len(sues)):
    if valid(sues[x],aim):
        print(x)
