#!/usr/bin/python3
import sys

#
# Direction: 0 = right, 1 = up, 2 = left, 3 = down
#

galaxy_map = []

def expand_col(col):
    gm1 = []
    for i in range(len(galaxy_map)):
        m = galaxy_map[i]
        gm1.append(m[:col] + '.'*1 + m[col:])
    return gm1

#
# Read in all the lines, duplicating any "empty" lines
for line in sys.stdin:
    l = line.strip()
    galaxy_map.append(l)
    try:
        l.index('#')
    except:
        for i in range(1):
            galaxy_map.append(l)

c = len(galaxy_map[0])
exp_list = []
while c > 0:
    c -= 1
    exp = True
    for r in galaxy_map:
        if r[c] == '#':
            exp = False
            break
    if exp:
        exp_list.append(c)

#print(exp_list)

for i in exp_list:
    galaxy_map = expand_col(i)

#for i in galaxy_map:
#    print(i)

stars = []
for r in range(len(galaxy_map)):
    l = galaxy_map[r]
    for c in range(len(l)):
        if l[c] == '#':
            stars.append((c, r))

print(stars)
path = 0
sl = len(stars)
for f in range(sl):
    s1 = stars[f]
    for t in range(f + 1, sl):
        s2 = stars[t]
        path += abs(s1[0] - s2[0]) + abs(s1[1] - s2[1])

print(path)

