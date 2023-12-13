#!/usr/bin/python3
import sys

sum = 0

for line in sys.stdin:
    g = line.split(':')
    game = int(g[0].split(' ')[1])
#    print(game)
    min_red = 0
    min_green = 0
    min_blue = 0
    sets = g[1].strip().split(';')
    for i in sets:
        nums = i.strip().split(',')
#        print(nums)
        for i in nums:
            v = i.strip().split(' ')
            if (v[1] == "red") and (int(v[0]) > min_red):
                    min_red = int(v[0])
            if (v[1] == "green") and (int(v[0]) > min_green):
                    min_green = int(v[0])
            if (v[1] == "blue") and (int(v[0]) > min_blue):
                    min_blue = int(v[0])
    power = (min_red * min_green * min_blue)
#    print(f"{min_red} red, {min_green} green, {min_blue} blue, {power} power")
    sum += power
print(f"{sum}")

