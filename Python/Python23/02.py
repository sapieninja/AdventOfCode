import aoc_utils
lines = aoc_utils.readLines()
bag = {"red": 12, "green": 13, "blue": 14}
def calc(p2, lines):
    total = 0
    for gameid,game in enumerate(lines,start=1):
        possible = True
        game = game.split(":")[1]
        game = game.split(";")
        minbag = {"red": 0, "blue": 0, "green": 0}
        for subgame in game:
            amounts = subgame.split(",")
            for value in amounts:
                num = [x for x in value.split(" ") if x!= ""][0]
                name = [x for x in value.split(" ") if x!= ""][1]
                num = int(num)
                if num > minbag[name]:
                    minbag[name] = num
                if num > bag[name]:
                    possible = False
        if possible and not p2:
            total += gameid
        elif p2:
            total += minbag["blue"]*minbag["green"]*minbag["red"]
    return total
print(calc(False, lines))
print(calc(True,  lines))

