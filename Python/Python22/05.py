import aoc_utils
lines = aoc_utils.readLines(False)
crates = []
instructions = []
toCrates = True
for line in lines:
    if toCrates:
        if line.strip().startswith("1"):toCrates = False
        crates.append(line)
    else:
        instructions.append(line)
crates = list(reversed(crates))
noStacks = len(crates[0].split())
stacks = [[] for i in range(noStacks)]
for layer in crates[1:]:
    for p in range(noStacks):
        if layer[p*4+1].strip() != "":
            stacks[p].append(layer[p*4+1])

instructions = aoc_utils.removeEmpties([instruction.strip() for instruction in instructions])

for instruction in instructions:
    commands = instruction.split()
    no = int(commands[1])
    fr = int(commands[3])-1
    to = int(commands[5])-1
    toMove = stacks[fr][-no:]
    stacks[fr] = stacks[fr][:-no]
    for i in toMove:
        stacks[to].append(i)

for stack in stacks:
    print(stack[-1],end="")
