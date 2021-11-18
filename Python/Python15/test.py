import aoc_utils
lines = aoc_utils.readlines()
for x in lines:
    print(x)
aim = 'a'
soldict = {}
for x in lines:
    solution = ''
    i = 0
    while True:
        if x[i] == '-':
            break
        solution += x[i]
        i+=1
    soldict[x.split()[-1]] = solution
solution = soldict[aim]
print(solution)
print(soldict["lx"])
while any(substring in solution for substring in soldict):
    x = solution.split()
    for i in range(len(x)):
        if x[i] in soldict:
            x[i] = "("+soldict[x[i]]+")"
    solution = ""
    for word in x:
        solution += " "
        solution += word
    print(solution)
    input()
