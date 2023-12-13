import sys

rows = []
cols = []

def do_check(arr, rc, skip):
    for i in enumerate(arr[:-1]):
        #print(f"Do_check: {i[0]} skip = {skip}")
        #print(i[1])
        #print(arr[i[0]+1])
        if (i[0] != skip) and (i[1] == arr[i[0]+1]):
            check_num = min(len(arr) - (i[0]+1), (i[0]+1))
            #print(f"Checking {check_num} {rc}s")
            found = True
            for c in range(1, check_num):
                if arr[i[0] - c] != arr[i[0] + 1 + c]:
                    found = False
                    break
            if found:
                #print(f"{rc} = {i[0] + 1}")
                return i[0] + 1
    return -1

def process(skip):
    """
    print("process ROWS")
    for i in rows:
        print(i)
    print()
    print("process COLS")
    for i in cols:
        print(i)
    print()
    """

    res = do_check(rows, "row", int((skip-1)/100) if (skip > 99) else -1)
    if res == -1:
        res = do_check(cols, "col", (skip-1) if skip < 100 else -1)
    else:
        res *= 100
    return res

def full_process():
    #
    # change one position in both row and cols and then process until we have a different result
    #
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
    old_res = process(-1)
    #print(f"Original mirror = {old_res}")
    for r in range(len(rows)):
        for c in range(len(rows[0])):
            #change r,c and c,r
            #print(f"Trying ({c}, {r})")
            old = rows[r][c]
            if old != cols[c][r]:
                print(f"Difference: {r}{c}")
            rows[r][c] = '.' if old == '#' else '#'
            cols[c][r] = '.' if old == '#' else '#'
            res = process(old_res)
            if res != -1 and res != old_res:
                """
                print("Final ROWS")
                for i in rows:
                    print(i)
                print()
                print("Final COLS")
                for i in cols:
                    print(i)
                print()
                print(f"Old = {old_res}, new = {res}, change = ({c}, {r})")
                """
                return res
            rows[r][c] = old
            cols[c][r] = old
    print(f"No reflection line found old = {old_res}")
    return -1

total = 0
for line in sys.stdin:
     l = [x for x in line.strip()]
     if len(l) == 0:
         total += full_process()
         rows=[]
         continue
     rows.append(l)
     if len(rows) == 1:
         cols = [[i] for i in l]  # start the columns matrix
         continue
     for i in enumerate(l):
         cols[i[0]] = cols[i[0]] + [i[1]]

if len(rows) != 0:
    total += full_process()

print(total)
