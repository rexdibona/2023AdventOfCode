#!/usr/bin/python3
import sys

sum = 0

def check(l, p1, p2):
    p2i = 0
    p2l = len(p2)
    cl = 0  # current number of '#' characters

    for i in p1:
        if i == '#':
            cl += 1
            continue
        if cl != 0:
            if p2i >= p2l:
                #print(f"p2i >= p2l: {p2i} {p2l}")
                return 0
            if p2[p2i] != cl:
                #print(f"p2[p2i] != cl: {p2[p2i]} {cl}")
                return 0
            #print(f"found {p2[p2i]} == {cl}")
            p2i += 1
            #print(f"p2i now {p2i}")
            cl = 0
    #print(f"cl = {cl}, p2i = {p2i}, p2l = {p2l}")
    if (cl == 0) and (p2i != p2l):
        # no trailing '#'
        return 0
    if cl != 0:
        if p2i >= p2l:
            return 0
        if (p2[p2i] == cl) and (p2i + 1 == p2l):
            return 1
        return 0
    return 1



def arrangements(pos, length, broken, fixed):
#    print(f"arrangements({pos}, {length}, {broken}, {fixed})")
    numq = 0
    if pos == length:
        #print(f"check({length}, {broken}, {fixed})")
        numq = check(length, broken, fixed)
        #print(f"check({length}, {broken}, {fixed}) => {numq}")
        return numq
    if broken[pos] == '?':
        # try both possibilities
        broken[pos] = '#'
        numq += arrangements(pos + 1, length, broken, fixed)
        broken[pos] = '.'
        numq += arrangements(pos + 1, length, broken, fixed)
        broken[pos] = '?'
    else:
        numq += arrangements(pos + 1, length, broken, fixed)
    return numq

# Read in each line, processing as we go
for line in sys.stdin:
    l = line.strip().split(' ')
    arr = arrangements(0, len(l[0]), [x for x in l[0]], [int(x) for x in l[1].split(',')])
    #print(arr)
    sum += arr
print(sum)
