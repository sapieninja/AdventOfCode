import functools
from time import time
st = time()
pos = [10, 1]
rolls = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


@functools.cache
def number(posa, posb, scorea, scoreb):
    if scorea >= 21:
        return (1, 0)
    if scoreb >= 21:
        return (0, 1)
    totala, totalb = 0, 0
    for i in rolls:
        b, a = number(
            posb, (posa + i - 1) % 10 + 1, scoreb, scorea + (posa + i - 1) % 10 + 1
        )
        totala += a * rolls[i]
        totalb += b * rolls[i]
    return totala, totalb

print(max(number(pos[0], pos[1], 0, 0)))
end = time()
print(end - st)
