#!/usr/bin/python3
import sys

sum = 0
lines=[]

# return True if this number has a symbol "next" to it.
def check_number(row, col, length):
    global lines
    for r in range(3):
        cur_row = row + r - 1
        if (cur_row < 0) or (cur_row >= len(lines)):
            continue
        for c in range(length+2):
            cur_col = col + c - 1
            if (cur_col < 0) or (cur_col >= len(lines[cur_row])):
                    continue
            if lines[cur_row][cur_col] in "!@#$%^&*()+-/=":
                return True
    return False

for line in sys.stdin:
    lines.append(line.strip())

for r in range(len(lines)):
    for c in range(len(lines[r])):
        ch = lines[r][c]
        if ch in "0123456789":
            # we have fouond the start of a number.
            # Grab the entire number and then check if it has a symbol around it.
            cp = c
            num = 0
            while cp < len(lines[r]) and lines[r][cp] in "0123456789":
                cp += 1
            cn = check_number(r, c, cp - c)
            num = int(lines[r][c:cp])
            for i in range(cp - c):
                #lines[r][c+i] = '.'
                lines[r] = lines[r][:c] + "."*(cp-c) + lines[r][cp:]
            if cn:
                sum += num
            print(f"Num: {num} {cn}")

print(lines)



print(f"{sum}")

