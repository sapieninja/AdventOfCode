import aoc_utils
packet = aoc_utils.read()
for i in range(13,len(packet)):
    if len(set(packet[i-14:i])) == 14:
        print(i)
        break
