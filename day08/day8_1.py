#!/usr/bin/python3
import sys

order =''
mapping = {}

for line in sys.stdin:
    l = line.strip()
    if order == '':
        order = l
        continue
    if l == '':
        continue
    #
    # A mapping. Record it in the dictionary
    #
    la = l.split('=')
    mapping[la[0].strip()] = la[1].strip().replace(' ', '').replace('(', ''). replace(')', '').split(',')

steps = 0
current='AAA'
while current != 'ZZZ':
    for i in order:
        if i == 'L':
            current = mapping[current][0]
        else:
            current = mapping[current][1]
        steps += 1
        if current == 'ZZZ':
            break

print(steps)
