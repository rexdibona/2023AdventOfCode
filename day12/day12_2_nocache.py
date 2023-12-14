import sys
from functools import lru_cache

#
# Helper function.
# This calculates how many characters a number string must take (at minimum)
#
def num_len(nums):
    l = 0
    for i in nums:
        l += i + 1
    if l != 0:
        l -= 1
    return l

def psearch(sprs, nums):
    print(f"search({sprs}, {nums})")
    res = search(sprs, nums)
    print(f"search({sprs}, {nums}) => {res}")
    return res

#
# Search function.
# We split the search space into three:
# The centre value and the LHS and RHS
# the centre value can only go in a certain range, and for each point in that range we calculate LHS and RHS and multiple them together.
#
@lru_cache(maxsize=None)
def search(sprs, nums):
    # if we are an end check then we just need to make sure there are no springs
    ln = len(nums)
    if ln == 0:
        for i in sprs:
            if i == '#':
                return 0
        return 1

    # Otherwise we now split into three
    ln = int(ln/2)
    LHS = tuple(nums[:ln])
    num = nums[ln]
    RHS = tuple(nums[ln+1:])
    LHS_min = num_len(LHS)
    RHS_min = num_len(RHS)
    LHS_SEP = (len(LHS) != 0)
    RHS_SEP = (len(RHS) != 0)
    #print(f"LHS = {LHS}, num = {num}, RHS = {RHS}, LHS_min = {LHS_min}, RHS_min = {RHS_min}")
    search_len = num + (1 if LHS_SEP else 0) + (1 if RHS_SEP else 0)
    # this gives our minimum boundary positions
    # we then shrink as necessary
    count = 0
    RHS_count = 0   # initialise before any possible use
    #print(f"range({LHS_min}, {len(sprs) - RHS_min - search_len + 1})")
    for i in range(LHS_min, len(sprs) - RHS_min - search_len + 1):
        # check both ends can be a '.' to separate us
        # We only check if there needs to be a separator
        sp = i          # start point for this spring
        if LHS_SEP:
            if sprs[sp] == '#':
                continue
            sp = i + 1
        np = sp + num   # start point for RHS
        if RHS_SEP:
            if sprs[sp + num] == '#':
                continue
            np += 1
        possible = True
        for p in range(sp, sp + num):
            if sprs[p] == '.':          # can't be here - so abandon this attempt
                possible = False
                break
        if not possible:
            continue
        # At this point the centre section has matched. Now search each of the LHS and RHS
        #print("LHS")
        LHS_count = search(sprs[:i], LHS)
        if LHS_count != 0:
            #print("RHS")
            RHS_count = search(sprs[np:], RHS)
        count += (LHS_count * RHS_count)
    return count


total = 0
# Read in each line, processing as we go
for line in sys.stdin:
    l = line.strip().split(' ')
    l0 = l[0]
    l1 = [int(x) for x in l[1].split(',')]
    fl0 = l0 + "?" + l0 + "?" + l0 + "?" + l0 + "?" + l0
    fl1 = l1*5
#    fl0 = l0
#    fl1 = l1
#    print(fl0)
#    print(fl1)
    arr = search(fl0, tuple(fl1))
    #print(arr)
    total += arr
print(total)

