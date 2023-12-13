#!/usr/bin/python3
import sys

sums = 0

def find_next(nums):
#    print(nums)
    allzero = True
    for i in nums:
        if i != 0:
            allzero = False
            break
    if allzero:
        return 0
    last = nums[0]
    new = []
    for i in nums[1:]:
        new.append(i - last)
        last = i
    return nums[0] - find_next(new)

for line in sys.stdin:
    sums += find_next([int(x) for x in line.split()])

print(sums)
