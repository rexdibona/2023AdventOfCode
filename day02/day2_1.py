#!/usr/bin/python3
import sys

sum = 0
max_red = 12
max_green = 13
max_blue = 14

for line in sys.stdin:
    g = line.split(':')
    game = int(g[0].split(' ')[1])
    print(game)
    sets = g[1].strip().split(';')
    for i in sets:
        nums = i.strip().split(',')
#        print(nums)
        for i in nums:
            v = i.strip().split(' ')
            if (v[1] == "red") and (int(v[0]) > max_red):
                    game = 0
            if (v[1] == "green") and (int(v[0]) > max_green):
                    game = 0
            if (v[1] == "blue") and (int(v[0]) > max_blue):
                    game = 0
        if game == 0:
            print(f"{nums} broke")
    sum += game
print(f"{sum}")

