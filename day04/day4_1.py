#!/usr/bin/python3
import sys

sum = 0

for line in sys.stdin:
    g = line.split(':')
    game = int(g[0].split(' ')[-1])
    nums = g[1].strip().replace('  ', ' ').split('|')
    wins = nums[0].strip().split(' ')
    count = 0
    guesses = nums[1].strip().split(' ')
#    print(f"{game}: {wins} | {guesses}")
    for i in guesses:
        if i in wins:
#            print(f"{i}")
            count += 1
    if count != 0:
        sum += (1 << (count - 1))

print(f"{sum}")

