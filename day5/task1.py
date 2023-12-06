#!/bin/python3
"""
Solution for task 5_1
"""

import os
import re
import multiprocessing

INPUT_FILE_NAME = 'input1.txt'

almanac = {
    "seeds": [],
    "seed-to-soil": [],
    "soil-to-fertilizer": [],
    "fertilizer-to-water": [],
    "water-to-light": [],
    "light-to-temperature": [],
    "temperature-to-humidity": [],
    "humidity-to-location": [],
}

def add_to_map(category, items):
    dst_str, src_str, length_str = items.split(" ")
    dst = int(dst_str)
    src = int(src_str)
    length  = int(length_str)

    new_item = [dst, src, length]
    almanac[category].append(new_item)

def find_in_map(category, item):
    for entry in almanac[category]:
        (dst, src, length) = entry
        if src <= item <= (src + length):
            return dst + item - src

    return item

if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        lines = input_file.readlines()

category = ""
for line_raw in lines:
    line = line_raw[:-1]
    if len(line) > 0:
        if line[0].isdigit():
            add_to_map(category, line)
        elif line[:6] == "seeds:":
            seeds_str = line.split(": ")[1]
            seeds = [int(seed) for seed in seeds_str.split(" ")]
            almanac["seeds"] = seeds
        else:
            category = line[:-5]
            print("found category %s" % category)

print(almanac)

min_locations = []

#part1
def min_seed_location(seeds):
    soils = [find_in_map("seed-to-soil", seed) for seed in seeds]
    fertilizers = [find_in_map("soil-to-fertilizer", soil) for soil in soils]
    waters = [find_in_map("fertilizer-to-water", fertilizer) for fertilizer in fertilizers]
    lights = [find_in_map("water-to-light", water) for water in waters]
    temps = [find_in_map("light-to-temperature", light) for light in lights]
    humids = [find_in_map("temperature-to-humidity", temp) for temp in temps]
    locs = [find_in_map("humidity-to-location", humid) for humid in humids]
    return min(locs)

print(min_seed_location(almanac["seeds"]))


#part2
seed_idx = 0
seed_ranges = []
# make ranges
while seed_idx < len(almanac["seeds"]):
    seed_ranges.append([almanac["seeds"][seed_idx], almanac["seeds"][seed_idx+1]])
    seed_idx += 2

print("ranges: %s" % str(seed_ranges))


def ranger(s_range):
    print("s_range %s" % str(s_range))
    (start, length) = s_range
    mins = []
    step = 10000000
    step_counter = 0
    last_stop = start

    while last_stop + step < start + length:
        seeds = [*range(last_stop, last_stop + step)]
        mins.append(min_seed_location(seeds))
        last_stop += step
        print("step %d" % step_counter)
        step_counter += 1

    seeds = range(last_stop, start + length)
    mins.append(min_seed_location(seeds))

    return min(mins)


with multiprocessing.Pool(10) as range_pool:
    mins = range_pool.map(ranger, seed_ranges)

print("\n\nfinal mins: %s" % str(mins))
print(min(mins))
