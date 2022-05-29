from collections import * 
stack = deque()
nums =((1,13,10),
(1,11,16),
(1,11,0),
(1,10,13),
(26,-14,7),
(26,-4,11),
(1,11,11),
(26,-3,10),
(1,12,16),
(26,-12,8),
(1,13,15),
(26,-12,2),
(26,-15,5),
(26,-12,10)
)
p1 = [0]*14
p2 = [0]*14
for a,b,c in nums:
    if a == 1:
        stack.append((a,b,c))
    else:
        popped = stack.pop()
        difference = b + popped[2]
        if difference >= 0:
            p1[nums.index(popped)] = 9 - difference
            p1[nums.index((a,b,c))] = 9
            p2[nums.index(popped)] = 1
            p2[nums.index((a,b,c))] = 1 + difference
        else:
            p1[nums.index(popped)] = 9
            p1[nums.index((a,b,c))] = 9 + difference
            p2[nums.index(popped)] = 1 - difference
            p2[nums.index((a,b,c))] = 1
p1 = list(map(str,p1))
p2 = list(map(str,p2))
print("".join(p1))
print("".join(p2))
