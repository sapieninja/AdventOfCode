import aoc_utils
import itertools
lines = aoc_utils.readlines()
people = set()
for x in lines:
    people.add(x.split()[0])
people = list(people)
connections = {}
length = len(people)
matrix = [[0 for x in range(length)] for x in range(length)]
for line in lines:
    a = line.split()[0]
    b = line.split()[-1][:-1]
    if line.split()[2] == "gain":
        matrix[people.index(a)][people.index(b)] += int(line.split()[3])
        matrix[people.index(b)][people.index(a)] += int(line.split()[3])
    else:
        matrix[people.index(a)][people.index(b)] -= int(line.split()[3])
        matrix[people.index(b)][people.index(a)] -= int(line.split()[3])
for x in matrix:
    print(x)
maximum = 0
for permutation in itertools.permutations(people):
    score = 0
    for x in range(len(permutation)):
        score += matrix[people.index(permutation[x-1])][people.index(permutation[x])]
    if score >= maximum:
        maximum = score
print(maximum)






