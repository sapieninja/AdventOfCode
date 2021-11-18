import json
with open("10.in","r") as inputfile:
    data = json.load(inputfile)
def evaluate(x):
    if type(x) == type(1):
        return x
    elif type(x) == type("hello"):
        return 0
    elif type(x) == type([1,2]):
        total = 0
        for subpart in x:
            total += evaluate(subpart)
        return total
    elif type(x) == type({}):
        total = 0
        if "red" in x.keys() or "red" in x.values():
            return 0
        for key in x.keys():
            total += evaluate(x[key])
        return total
    print(type(x))
print(evaluate(data))
