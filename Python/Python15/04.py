import hashlib
import aoc_utils
inputstring = aoc_utils.read()
x = 0
while True:
#    print(x)
    ts = inputstring + str(x)
    hexhash = hashlib.md5(ts.encode()).hexdigest()
    if hexhash[0:5] == "0"*5:
        print(ts,hexhash)
    x += 1
    if x == 91546459*100:
        break

