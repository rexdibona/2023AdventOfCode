#!/usr/bin/python3
import functools
import sys

order = "xxJ23456789TQKA"

strength = [[] for x in range(8)]

def rank(card):
    #
    # card is the five card values, as a string
    #
    jokers = 0
    ranks = [0 for x in range(15)]
    for i in card:
        if i == 'J':
            jokers += 1
        else:
            ranks[order.index(i)] += 1
    ranks.sort()
    ranks.reverse()
    if ranks[0] == 5 or (ranks[0] + jokers) == 5:
        return 7
    if ranks[0] == 4 or (ranks[0] + jokers) == 4:
        return 6
    if ranks[0] == 3 or (ranks[0] + jokers) == 3:
        if ranks[1] == 2:
            return 5
        return 4
    if ranks[0] == 2 or (ranks[0] + jokers) == 2:
        if ranks[1] == 2:
            return 3
        return 2
    return 1

def compare(c1, c2):
    # compare function.
    for i in range(5):
        k1 = c1[0][i]
        k2 = c2[0][i]
        if k1 == k2:
            continue
        return order.index(k2) - order.index(k1)

for line in sys.stdin:
    parts = line.strip().split()
    strength[rank(parts[0])].append(parts)

for i in range(len(strength)):
    strength[i] = sorted(strength[i], key=functools.cmp_to_key(compare), reverse=True)

#print(strength)

winnings = 0
multiplier = 1
for i in strength:
    for j in i:
#        print(j)
        winnings += multiplier * int(j[1])
        multiplier += 1

print(winnings)
