import aoc_utils
directions = aoc_utils.read()
coordinate = (0,0)
robocoord = coordinate
turn = 0
places = set()
for x in directions:
    if turn == 0:
        places.add(coordinate)
        if x==">":coordinate= (coordinate[0] + 1,coordinate[1])
        elif x=="<":coordinate= (coordinate[0] -1,coordinate[1]) 
        elif x=="^":coordinate= (coordinate[0], coordinate[1] + 1 ) 
        elif x=="v":coordinate= (coordinate[0], coordinate[1] -1) 
    if turn == 1:
        places.add(robocoord)
        if x==">":robocoord= (robocoord[0] + 1,robocoord[1])
        elif x=="<":robocoord= (robocoord[0] -1,robocoord[1]) 
        elif x=="^":robocoord= (robocoord[0], robocoord[1] + 1 ) 
        elif x=="v":robocoord= (robocoord[0], robocoord[1] -1) 
    print(places)
    print(coordinate)
    turn = (turn+1)%2
print(len(places))
