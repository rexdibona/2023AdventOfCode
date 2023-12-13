#!/usr/bin/python3
import sys

#
# Direction: 0 = right, 1 = up, 2 = left, 3 = down
#

galaxy_map = []
stars = []
exp_row = []
exp_col = []

mul=999999
def expand_stars():
    global stars

    # sort on columns
    stars.sort(key=lambda s: s[0])
    cur_col = 0
    cur_add = 0
    for i in range(len(stars)):
        while (cur_col < len(exp_col)) and (stars[i][0] > exp_col[cur_col]):
            cur_add += mul
            cur_col += 1
        stars[i] = (stars[i][0] + cur_add, stars[i][1])
    # sort on rows
    stars.sort(key=lambda s: s[1])
    cur_row = 0
    cur_add = 0
    for i in range(len(stars)):
        while (cur_row < len(exp_row)) and (stars[i][1] > exp_row[cur_row]):
            cur_add += mul
            cur_row += 1
        stars[i] = (stars[i][0], stars[i][1] + cur_add)
    pass

#
# Read in all the lines
#
for line in sys.stdin:
    l = line.strip()
    galaxy_map.append(l)


#
# find a list of rows that are to be expanded
#
for r in range(len(galaxy_map)):
    l = galaxy_map[r]
    try:
        l.index('#')
    except:
        exp_row.append(r)

for c in range(len(galaxy_map[0])):
    exp = True
    for r in galaxy_map:
        if r[c] == '#':
            exp = False
            break
    if exp:
        exp_col.append(c)

#print(exp_row)
#print(exp_col)

for r in range(len(galaxy_map)):
    l = galaxy_map[r]
    for c in range(len(l)):
        if l[c] == '#':
            stars.append((c, r))

#print(stars)
expand_stars()
#print(stars)

path = 0
sl = len(stars)
for f in range(sl):
    s1 = stars[f]
    for t in range(f + 1, sl):
        s2 = stars[t]
        path += abs(s1[0] - s2[0]) + abs(s1[1] - s2[1])

print(path)

