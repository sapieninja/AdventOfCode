import aoc_utils
import itertools
import re
lines = aoc_utils.readlines()
ingredients = []
for line in lines:
    ingredients.append(list(map(int,re.findall(r'-?\d',line))))
maxscore = 0 
for a,b,c,d in itertools.product(range(0,101),range(0,101),range(0,101),range(0,101)):
    if a+b+c+d==100:
        score = 1
        for i in range(len(ingredients[0])):
            part = 0
            part += a*ingredients[0][i]
            part += b*ingredients[1][i]
            part += c*ingredients[2][i]
            part += d*ingredients[3][i]
            if part > 0:
                score *= part
        if score//500 > maxscore and part==500:
            maxscore = score//500
print(maxscore)
