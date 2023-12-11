#!/bin/python3
"""
Solution for task 11_1
"""

import os
import re

INPUT_FILE_NAME = 'input1.txt'

if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        lines = input_file.readlines()

the_map = []
expanse_map = []
galaxies = []

def expand_vertically():
    for yidx, line_raw in enumerate(lines):
        double_line = True
        line = line_raw[:-1]
        newline = []
        for xidx, space in enumerate(line):
            if space == '#':
                double_line = False
            newline.append(space)
        the_map.append(newline)
        if double_line:
            the_map.append(newline.copy())


def expand_horizontally():
    xidx = 0
    while xidx < len(the_map[0]):
        double_column = True
        for yidx in range(len(the_map)):
            if the_map[yidx][xidx] == '#':
                double_column = False
        if not double_column:
            xidx += 1
            continue

        # otherwise - expand column
        for yidx in range(len(the_map)):
            the_map[yidx].insert(xidx+1,'.')
        xidx += 2

def expand_map():
    expand_vertically()
    print_map()
    expand_horizontally()

def the_expanse():
    for yidx, line_raw in enumerate(lines):
        expand_line = True
        line = line_raw[:-1]
        newline = []
        for xidx, space in enumerate(line):
            if space == '#':
                expand_line = False
            newline.append(space)
        if expand_line:
            newline = ['x' for _ in newline]
        expanse_map.append(newline)

    xidx = 0
    for xidx in range(len(expanse_map[0])):
        expand_column = True
        for yidx in range(len(expanse_map)):
            if expanse_map[yidx][xidx] == '#':
                expand_column = False

        if expand_column:
            for yidx in range(len(expanse_map)):
                expanse_map[yidx][xidx] = 'x'

def print_map():
    print("the map: ")
    for line in the_map:
        print(''.join(line))

def print_expanse():
    print("the expanse: ")
    for line in expanse_map:
        print(''.join(line))

def find_galaxies():
    for yidx, line in enumerate(the_map):
        for xidx, column in enumerate(line):
            if column == '#':
                galaxies.append([xidx, yidx])

def find_galaxies_in_expanse():
    for yidx, line in enumerate(expanse_map):
        for xidx, column in enumerate(line):
            if column == '#':
                galaxies.append([xidx, yidx])

expand_map()
print_map()
find_galaxies()
print("galaxies: %s" % str(galaxies))

distances = []
for gidx, galaxy in enumerate(galaxies[:-1]):
    for galaxy2 in galaxies[gidx+1:]:
        distance = abs(galaxy[0] - galaxy2[0]) + abs(galaxy[1] - galaxy2[1])
        print("distance between %s and %s: %d" % (str(galaxy), str(galaxy2), distance))
        distances.append(distance)

print("summ: %d" % sum(distances))

# part 2
the_expanse()
print_expanse
galaxies = []
find_galaxies_in_expanse()
print("galaxies: %s" % str(galaxies))

def the_way(g1, g2):
    the_xs = []
    the_ys = []

    x1 = g1[0]
    x2 = g2[0]
    if x1 > x2:
        x1 = g2[0]
        x2 = g1[0]

    y1 = g1[1]
    y2 = g2[1]
    if y1 > y2:
        y1 = g2[0]
        y2 = g1[0]

    if x1 != x2:
        the_xs = expanse_map[y1][x1:x2+1]
    if y1 != y2:
        the_ys = [expanse_map[yidx][x1] for yidx in range(y1,y2+1)]

    return the_xs + the_ys


distances100 = []
distances10 = []
distances1m = []
for gidx, galaxy in enumerate(galaxies[:-1]):
    for galaxy2 in galaxies[gidx+1:]:
        print("galaxies %s and %s:" % (str(galaxy), str(galaxy2)))
        distance = abs(galaxy[0] - galaxy2[0]) + abs(galaxy[1] - galaxy2[1])
        way = the_way(galaxy, galaxy2)
        expanses = way.count('x')
        print(" way: %s (%d expanses)" % (str(way), expanses))
        if expanses > 0:
            distance -= expanses
            distances100.append(distance + expanses * 100)
            distances10.append(distance +  expanses * 10)
            distances1m.append(distance +  expanses * 1000000)
        else:
            distances100.append(distance)
            distances10.append(distance)
            distances1m .append(distance)
        print(" distances:\tx10  %d\tx100 %d\tx1M  %d" % (distances10[-1], distances100[-1], distances1m[-1]))
        distances.append(distance)

print("summ x10 : %d" % sum(distances10))
print("summ x100: %d" % sum(distances100))
print("summ x1M:  %d" % sum(distances1m))