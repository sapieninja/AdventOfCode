import aoc_utils
ints = aoc_utils.readints()
for x in ints:
    for y in ints:
        if x+y == 2020:
            print(x*y)
for x in ints:
    for y in ints:
        for z in ints:
            if x + y + z == 2020:
                print(x*y*z)
                break