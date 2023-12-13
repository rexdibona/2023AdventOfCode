#!/usr/bin/python3
import sys

seed_to_soil = []
soil_to_fert = []
fert_to_water = []
water_to_light = []
light_to_temp = []
temp_to_humid = []
humid_to_locate = []

maps = [seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_humid, humid_to_locate]
str_maps = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
state = 0
seeds = []

def map_append(m):
    maps[state].append([int(x) for x in m])

def do_map(i, s):
    # use map 'i' to return what s changes to
    for mp in i:
        if s < mp[1]:
            return s
        if s < mp[1] + mp[2]:
            return mp[0] + s - mp[1]
    return s

def read_input(f):
    global state
    global seeds
    for line in f:
        l = line.strip()
        if len(l) == 0:
            continue
        if line[0] in "0123456789":
            # numerical line - add to current map
            map_append(l.split(' '))
            continue
        if l[0:7] == "seeds: ":
            seeds = [int(x) for x in l[7:].split(' ')]
            continue
        if l[-1] == ':':
            state = str_maps.index(l.split(' ')[0])
            continue
        print(f"Unknown Line: '{l}'")
    
read_input(sys.stdin)
for i in range(len(maps)):
#    print(maps[i])
    maps[i] = sorted(maps[i], key=lambda map: map[1])

lowest = -1
#print(seeds)
for s in seeds:
    inits = s
    for i in maps:
        s1 = s
        s = do_map(i, s)
        #print(f"{s1} -> {s}")
#    print(f"{inits} -> {s}")
    if lowest == -1 or lowest > s:
        lowest = s
print(f"lowest = {lowest}")
