import aoc_utils
lines = aoc_utils.readlines()
instructions = []
for x in lines:
    x = x.split()
    if x[0] == "toggle":
        instructions.append(("toggle",x[1],x[3]))
    else:
        instructions.append((x[1],x[2],x[4]))
grid = [[0 for x in range(1000)] for y in range(1000)]
print(instructions)
for instruction in instructions:
    for x in range(int(instruction[1].split(',')[0]),int(instruction[2].split(',')[0])+1):
        for y in range(int(instruction[1].split(',')[1]),int(instruction[2].split(',')[1])+1):
            if  instruction[0] == "off":
                grid[x][y] -= 1
                if grid[x][y] < 0:grid[x][y] = 0
            elif  instruction[0] == "on":
                grid[x][y] += 1
            else:
                grid[x][y] += 2
count = sum(sum(x) for x in grid)
print(count)
