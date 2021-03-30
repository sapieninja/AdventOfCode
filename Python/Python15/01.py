import fileinput
import itertools
inputstring= next(fileinput.input())
print(inputstring)
floor = 0
iterator = 1
for x in inputstring:
    if(x=='('):floor+=1
    else:floor-=1
    if floor ==-1:
        print(iterator)
    iterator+=1
