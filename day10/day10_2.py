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
pipe_path = []
for line in sys.stdin:
    pipe_map.append([x for x in line.strip()])
    pipe_path.append([' ' for x in line.strip()])

def colour_map():
    #
    # we need to colour the map to see if each point is inside or outside the
    # pipe.
    # to do this we have to count the number of times we cross the pipe line.
    # so '|' is a cross
    # 'F-*J' is a cross
    # 'F-*7' is NOT a cross
    # 'L-*7' is a cross
    # 'L-*J' is NOT a cross
    # We start outside the pipe

    inside = 0
    hl = ' '
    for r in pipe_path:
        io = 0  # currently outside
        for c in range(len(r)):
            if r[c] == '|':
                io = 1 - io
                continue
            if r[c] == 'F':
                hl = 'F'
                continue
            if r[c] == 'L':
                hl = 'L'
                continue
            if r[c] == '-':
                continue
            if r[c] == 'J':
                if hl == 'F':
                    io = 1 - io
                    hl = ' '
                    continue
                if hl == 'L':
                    hl = ' '
                    continue
                print(f"Found '{r[c]}' but previous was '{hl}'")
                continue
            if r[c] == '7':
                if hl == 'L':
                    io = 1 - io
                    hl = ' '
                    continue
                if hl == 'F':
                    hl = ' '
                    continue
                print(f"Found '{r[c]}' but previous was '{hl}'")
                continue
            #r[c] = 'O' if io == 0 else 'I'
            if io == 1:
                inside += 1
                r[c] = 'I'
            else:
                r[c] = 'O'
    return inside

def sym_set(c, r, s):
    pipe_path[r][c] = s

def sym(c, r):
    return pipe_map[r][c]

def move(c, r, d):
    p = sym(c, r)
    #print(f"move({c},{r},{d_str[d]},{p})")
    match p:
        case 'S':
            return (c,r,d)
        case '|':
            sym_set(c, r, p)
        case '-':
            sym_set(c, r, p)
        case 'L':
            sym_set(c, r, p)
            d = UP if d == LEFT else RIGHT
        case 'J':
            sym_set(c, r, p)
            d = UP if d == RIGHT else LEFT
        case '7':
            sym_set(c, r, p)
            d = DOWN if d == RIGHT else LEFT
        case 'F':
            sym_set(c, r, p)
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

end_row = -1
end_col = -1
cur_symbol = '.'
for i in range(len(pipe_map)):
    if 'S' in pipe_map[i]:
        end_row = i
        end_col = pipe_map[i].index('S')
        break

if (end_row == -1) and (end_col == -1):
    quit("Could not find start")

cur_row = end_row
cur_col = end_col
print(f"{end_col},{end_row} -> {sym(end_col, end_row)}")

#
# When have the start point. Discover how the pipe should have looked and add it back in.
#
hor=0
ver=0
if (cur_col < len(pipe_map[0])) and (sym(cur_col + 1, cur_row) in "J7-"):
    print(f"(+1,0)=({cur_col + 1, cur_row}) => {sym(cur_col + 1, cur_row)}")
    cur_dir = RIGHT
    hor += 1
if (cur_col > 0) and (sym(cur_col - 1, cur_row) in "LF-"):
    print(f"(-1,0)=({cur_col - 1, cur_row}) => {sym(cur_col - 1, cur_row)}")
    cur_dir = LEFT
    hor += 2
if (cur_row < len(pipe_map)) and (sym(cur_col, cur_row + 1) in "LJ|"):
    print(f"(0,+1)=({cur_col, cur_row+1}) => {sym(cur_col, cur_row + 1)}")
    cur_dir = DOWN
    ver += 1
if (cur_row > 0) and (sym(cur_col, cur_row - 1) in "F7|"):
    print(f"(0,-1)=({cur_col, cur_row-1}) => {sym(cur_col, cur_row - 1)}")
    cur_dir = UP
    ver += 2
# ver shows the vertical exits, and hor shows the horizontal exits
#total: 0123456789ABCDEF
#hor:   0000111122223333
#ver:   0123012301230123
#char:  ...|.FL..7J.-...
pipe_char = "+++|+FL++7J+-+++"
print(f"{hor},{ver}")
if cur_dir == RIGHT:
    cur_col += 1
if cur_dir == LEFT:
    cur_col -= 1
if cur_dir == DOWN:
    cur_row += 1
if cur_dir == UP:
    cur_row -= 1


sym_set(end_col, end_row, pipe_char[hor * 4 + ver])
sym_set(cur_col, cur_row, sym(cur_col, cur_row))

steps = 1
while (cur_row != end_row) or (cur_col != end_col):
    (cur_col, cur_row, cur_dir) = move(cur_col, cur_row, cur_dir)
    cur_symbol = sym(cur_col, cur_row)
    #print(cur_col, cur_row, d_str[cur_dir], cur_symbol)
    steps += 1

inside = colour_map()

for r in pipe_path:
    for p in r:
        print(p, end = '')
    print()

print(inside)

