import sys

rows = []
cols = []

def do_check(rows, rc):
    for i in enumerate(rows[:-1]):
        if i[1] == rows[i[0]+1]:
            check_num = min(len(rows) - (i[0]+1), (i[0]+1))
            #print(f"Checking {check_num} {rc}s")
            found = True
            for c in range(1, check_num):
                if rows[i[0] - c] != rows[i[0] + 1 + c]:
                    found = False
                    break
            if found:
                #print(f"{rc} = {i[0] + 1}")
                return i[0] + 1
    return -1

def process():
    """
    print("ROWS")
    for i in rows:
        print(i)
    print()
    print("COLS")
    for i in cols:
        print(i)
    print()
    """

    res = do_check(rows, "row")
    if res == -1:
        res = do_check(cols, "col")
        if res == -1:
            return -1
    else:
        res *= 100
    return res

total = 0
for line in sys.stdin:
     l = line.strip()
     if len(l) == 0:
         total += process()
         rows=[]
         continue
     rows.append(l)
     if len(rows) == 1:
         cols = [i for i in l]  # start the columns matrix
         continue
     for i in enumerate(l):
         cols[i[0]] = cols[i[0]] + i[1]

if len(rows) != 0:
    total += process()

print(total)
