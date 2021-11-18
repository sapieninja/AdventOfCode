import re
alphabet = list("abcdefghijklmnopqrstuvwxyz")
def addone(ticket):
    ticket = list(ticket)
    for x in range(len(ticket)):
        ticket[x] = alphabet.index(ticket[x])
    #we scan from the front for the number 25 and when it stops we increment
    for x in range(1,len(ticket)):
        if ticket[-x] == 25:
            ticket[-x] = 0
        else:
            ticket[-x] = ticket[-x] + 1
            break
    output = ""
    for x in ticket:
        output += alphabet[x]
    return output
def validate(ticket):
    if "i" in ticket or "o" in ticket or "l" in ticket:
        return False
    repetition = False
    for x in range(len(ticket)-3):
        if alphabet.index(ticket[x]) == alphabet.index(ticket[x+1]) -1 and alphabet.index(ticket[x+1]) == alphabet.index(ticket[x+2]) -1:
            repetition = True
    if repetition == False:
        return False
    matches = set(re.findall(r"(.)\1",ticket))
    if len(matches) < 2:
        return False
    return True
ticket = input()
while True:
    ticket = addone(ticket)
    if validate(ticket):
        print("VALID",ticket)
        break
