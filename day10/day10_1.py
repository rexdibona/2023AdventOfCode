#!/usr/bin/python3
import sys

#
# Direction: 0 = right, 1 = up, 2 = left, 3 = down
#
RIGHT=0
UP=1
LEFT=2
DOWN=3

d_str = ["Right", "Up   ", "Left ", "Down " ]

pipe_map = []
for line in sys.stdin:
    pipe_map.append(line.strip())

def sym(c, r):
    return pipe_map[r][c]

def move(c, r, d):
    p = sym(c, r)
    #print(f"move({c},{r},{d_str[d]},{p})")
    match p:
        case 'S':
            return (c,r,d)
        case '|':
            pass
        case '-':
            pass
        case 'L':
            d = UP if d == LEFT else RIGHT
        case 'J':
            d = UP if d == RIGHT else LEFT
        case '7':
            d = DOWN if d == RIGHT else LEFT
        case 'F':
            d = DOWN if d == LEFT else RIGHT
        case '.':
            print(f"Moved onto a '.' character at location {c},{r}")
        case _:
            print(f"Unknown pipe character {p} at location {c},{r}")
            return (c,r,d)
    match d:
        case 0:     # RIGHT:
            c += 1
        case 1:     # UP:
            r -= 1
        case 2:     # LEFT:
            c -= 1
        case 3:     # DOWN:
            r += 1
    return (c,r,d)

cur_row = -1
cur_col = -1
cur_symbol = '.'
for i in range(len(pipe_map)):
    if 'S' in pipe_map[i]:
        cur_row = i
        cur_col = pipe_map[i].index('S')
        break

if (cur_col < len(pipe_map[0])) and (sym(cur_col + 1, cur_row) in "J7-"):
    cur_col += 1
    cur_dir = RIGHT
elif (cur_col > 0) and (sym(cur_col - 1, cur_row) in "LF-"):
    cur_col -= 1
    cur_dir = LEFT
elif (cur_row < len(pipe_map)) and (sym(cur_col, cur_row + 1) in "J7|"):
    cur_row += 1
    cur_dir = DOWN
else:
    cur_row -= 1
    cur_dir = UP        # this should never happen, as one of the others should have been found first

steps = 1
while cur_symbol != 'S':
    (cur_col, cur_row, cur_dir) = move(cur_col, cur_row, cur_dir)
    cur_symbol = sym(cur_col, cur_row)
#    print(cur_col, cur_row, d_str[cur_dir], cur_symbol)
    steps += 1

#print(f"Step {steps}: ({cur_col},{cur_row})")
print(int(steps/2))
