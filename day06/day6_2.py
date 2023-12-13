#!/usr/bin/python3
import sys

result = 1
def check(time, distance):
#    print(f"check({time}, {distance})")
    count = 0
    for held in range(time+1):
        s = held
        d = (time - held) * s
#        print(f"Time: {held} distance: {d}")
        if d > distance:
            count += 1
    return count

line1 = [int(x) for x in sys.stdin.readline().replace(' ','').split(':')[1:]]
line2 = [int(x) for x in sys.stdin.readline().replace(' ','').split(':')[1:]]
#print(line1)
#print(line2)
if len(line1) != len(line2):
    print(f"Length of lines is different: {len(line1)} != {len(line2)}")
    quit("Lines Different Lengths")
for i in range(len(line1)):
    result *= check(line1[i], line2[i])
print(result)
