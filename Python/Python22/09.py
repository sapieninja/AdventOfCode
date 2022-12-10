import aoc_utils
lines = aoc_utils.readLines()
def solve(n):
    positions = set()
    knots = [(0,0)]*n
    for line in lines:
        d,l = line.split()
        if d == "U": delta = (0,1)
        if d == "D": delta = (0,-1)
        if d == "R": delta = (1,0)
        if d == "L": delta = (-1,0)
        for i in range(int(l)):
            knots[0] = (knots[0][0] + delta[0], knots[0][1] + delta[1])
            for i in range(len(knots)-1):
                h = knots[i]
                t = knots[i+1]
                if abs(t[0]-h[0]) == 0 and abs(t[1] - h[1]) == 2:   t = (t[0], t[1] + (1 if h[1] - t[1] > 0 else -1))
                elif abs(t[1]-h[1]) == 0 and abs(t[0] - h[0]) == 2: t = (t[0] + (1 if h[0] - t[0] > 0 else -1), t[1])
                elif abs(t[1]-h[1])>1 or abs(t[0] - h[0])>1: t = (t[0] + (1 if h[0] - t[0] > 0 else -1), t[1] + (1 if h[1] - t[1] > 0 else -1))
                knots[i+1] = t
            positions.add(knots[-1])
    return len(positions)
print(solve(2))
print(solve(10))
