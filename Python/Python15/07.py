import aoc_utils
import functools
lines = aoc_utils.readlines()
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
soldict["b"] = "16076"
solution = soldict[aim]
@functools.lru_cache()
def findlongsolution(solution):
    #input the wire name
    #split it into sub parts
    #go for the integer not the other solution
    solution = solution.replace("RSHIFT",">>").replace("LSHIFT","<<").replace("NOT","~").replace("AND","&").replace("OR","|")
    try:
        eval(solution)
        return str(eval(solution))
    except:
        solutionlist = solution.split()
        for x in range(len(solutionlist)):
            if solutionlist[x] in soldict:
                solutionlist[x] = "( " + findlongsolution(soldict[solutionlist[x]]) + " )"
        solution = ' '.join(solutionlist)
        return str(eval(solution))


solution = findlongsolution(solution)
print(solution)

