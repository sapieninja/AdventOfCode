import aoc_utils
import re
nums = aoc_utils.readLines()
def calc(p2,nums):
    total = 0
    valid = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in nums:
        linenos = []
        if p2:
            for option in valid:
                indexes = [m.start() for m in re.finditer(option, line)]
                for index in indexes:
                    linenos.append((index, valid.index(option) + 1))
        for index,digit in enumerate(line):
            if digit.isnumeric():
                linenos.append((index,digit))
        linenos.sort()
        num = int(linenos[0][1])*10 + int(linenos[-1][1])
        total += num
    return total
print(calc(False, nums))
print(calc(True,  nums))
