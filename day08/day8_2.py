#!/usr/bin/python3
import sys

order = []
mapping = {}
ghosts = []
paths = {}
num_ghosts = 0

for line in sys.stdin:
    l = line.strip()
    if order == []:
        order = [0 if a == 'L' else 1 for a in l]
        continue
    if l == '':
        continue
    #
    # A mapping. Record it in the dictionary
    #
    la = l.split('=')
    name = la[0].strip()
    node = la[1].strip().replace(' ', '').replace('(', ''). replace(')', '').split(',')
    node.append(name[2] == 'Z')
    mapping[name] = node

for i in mapping:
    paths[i] = [0, 0, mapping[i][2], i]

for i in mapping:
    paths[i][0] = paths[mapping[i][0]]
    paths[i][1] = paths[mapping[i][1]]

for i in mapping:
    if i[2] == 'A':
        print(i)
        ghosts.append(paths[i])
        num_ghosts += 1

#print(ghosts)

#print(paths)
#print(paths['22A'][0][1][1][2])

steps = 0
end = False

while not end:
    for i in order:
        end = True
        for g in range(num_ghosts):
            ghosts[g] = ghosts[g][i]
            end = end and ghosts[g][2]
#        for g in range(num_ghosts):
#            print(f"Ghost[{g}] is now at {ghosts[g][3]},T/F {ghosts[g][2]} {end}")
        steps += 1
        if end:
            break

print(steps)
