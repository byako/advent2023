#!/bin/python3
"""
Solution for task 6_1
"""

import os
import re
import multiprocessing

INPUT_FILE_NAME = 'input1.txt'

if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        lines = input_file.readlines()

times = []
distances = []
ways = []

total_time = 0
total_dist = 0

# parse data
for line in lines:
    if line [:5] == "Time:":
        times = [int(ttime) for ttime in line[5:-1].split()]
        total_time = int(line[5:-1].replace(' ',''))
    elif line[:9] == "Distance:":
        distances = [int(ddistance) for ddistance in line[9:-1].split()]
        total_distance = int(line[9:-1].replace(' ', ''))
    else:
        print("WTF: %s" % line)

print("times:     %s" % str(times))
print("distances: %s" % str(distances))

def find_start(time, distance):
    min = 0
    for idx in range(1, time):
        if (time - idx) * idx > distance:
            min = idx
            break
    return min

total = 1
for race in range(len(times)):
    start       = find_start(times[race], distances[race])
    ways.append((times[race] - 2*start) + 1)
    print("race %d: %d" % (race, ways[race]))
    total *= ways[race]

print("total: %d" % total)

# part 2
total_start = find_start(total_time, total_distance)
total_ways = (total_time - 2*total_start) + 1
print("full race: %d" % total_ways)