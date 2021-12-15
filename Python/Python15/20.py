import math
import primefac
import itertools
import functools
import operator
base = 36000000
def sumfactors(base):
    factors = list(primefac.primefac(base))
    total = 1
    for i in set(factors):
        count = factors.count(i)
        total *= (i**(count+1)-1)/(i-1)
    return total
def getnumbers(base):
    factors = list(primefac.primefac(base))
    output = set()
    if base<=50:
        output.add(1)
    for r in range(1,len(factors)+1):
        for numbers in itertools.combinations(factors,r):
            result = functools.reduce(operator.mul,numbers)
            if base/result <= 50:
                output.add(result)
    return list(output)


for i in range(10):
    print(getnumbers(i))
for i in range(0,base,math.factorial(4)):
    current = sum(getnumbers(i))
    print(current/base)
    if current*11 >= base:
        print(i)
        break

