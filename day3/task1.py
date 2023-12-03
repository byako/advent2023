#!/bin/python3
"""
Solution for task 3_1
"""

import os
import re

INPUT_FILE_NAME = 'input1.txt'

if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        INPUTS_RAW = input_file.readlines()

line_length = len(INPUTS_RAW[0][:-1])
non_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def has_symbol(x1, x2, y):
    print("  checking number %d-%d:%d" % (x1, x2, y))
    # check left
    if x1 > 0:
        if INPUTS_RAW[y][x1 - 1] not in non_chars:
            print("    left is symbol: %s" % INPUTS_RAW[y][x1 - 1])
            return True

    # check right
    if x2 < line_length - 1:
        if INPUTS_RAW[y][x2 + 1] not in non_chars:
            print("    left is symbol: %s" % INPUTS_RAW[y][x2 + 1])
            return True

    # check top line with corners
    if y > 0:
        for x in range(x1, x2 + 1):
            if INPUTS_RAW[y - 1][x] not in non_chars:
                print("    top is symbol: %s" % INPUTS_RAW[y - 1][x])
                return True

    # check bottom line with corners
    if y < len(INPUTS_RAW) - 1:
        for x in range(x1, x2 + 1):
            if INPUTS_RAW[y + 1][x] not in non_chars:
                print("    top is symbol: %s" % INPUTS_RAW[y + 1][x])
                return True

    # check corners
    if x1 > 0 and y > 0 and INPUTS_RAW[y - 1][x1 - 1] not in non_chars:
        print("    top left is symbol")
        return True
    if x1 > 0 and y < (len(INPUTS_RAW) - 1) and INPUTS_RAW[y + 1][x1 - 1] not in non_chars:
        print("    bottom left is symbol")
        return True
    if x2 < (line_length - 1) and y < (len(INPUTS_RAW) - 1) and INPUTS_RAW[y + 1][x2 + 1] not in non_chars:
        print("    bottom right is symbol")
        return True
    if x2 < (line_length - 1) and y > 0 and INPUTS_RAW[y - 1][x2 + 1] not in non_chars:
        print("    top right is symbol")
        return True

    return False

#part 1
summ = 0
for line_idx, line_raw in enumerate(INPUTS_RAW):
    line = line_raw[:-1]
    number_start = -1
    number_end   = -1
    for idx, char in enumerate(line):
        if char in numbers:
            if number_start == -1:
                print("number start: %d %d" % (idx, line_idx))
                number_start = idx
        else:
            if number_start != -1:
                number_end = idx - 1
                number_str = line[number_start:idx]
                print("  found number %s" % number_str)
                if has_symbol(number_start, number_end, line_idx):
                    summ += int(number_str)
                    print("  summ is now %d" % summ)
                number_start = -1
                number_end   = -1
    
    if number_start != -1 and number_end == -1:
        number_str = line[number_start:]
        print("  found number in the end %s" % number_str)
        if has_symbol(number_start, line_length - 1, line_idx):
            summ += int(number_str)
            print("  summ is now %d" % summ)

print(summ)

# part 2
def get_number(x, y):
    print("  checking number %d:%d" % (x, y))
    xl = x
    xr = x
    while xl > -1 and INPUTS_RAW[y][xl] in numbers:
        xl -= 1
    while xr < line_length and INPUTS_RAW[y][xr] in numbers:
        xr += 1

    xl += 1
    number = INPUTS_RAW[y][xl:xr]

    print("  number %d-%d:%d    %s" % (xl, xr, y, number))
    return number

def numbers_around(x, y):
    coords = []
    x1 = x
    x2 = x
    # left
    if x > 0:
        x1 -= 1
        if INPUTS_RAW[y][x-1] in numbers:
            print("number on left")
            coords.append([x-1,y])
    # right
    if x < line_length - 1:
        x2 += 1
        if INPUTS_RAW[y][x+1] in numbers:
            print("number on right")
            coords.append([x+1, y])

    if y > 0:
        top_line = INPUTS_RAW[y - 1][x1:x2+1]
        for xidx in [m.start() for m in re.finditer('[0-9]+', top_line)]:
            print("number on top")
            coords.append([x1 + xidx, y - 1])
    
    if y < len(INPUTS_RAW) - 1:
        bottom_line = INPUTS_RAW[y + 1][x1:x2+1]
        for xidx in [m.start() for m in re.finditer('[0-9]+', bottom_line)]:
            print("number on bottom")
            coords.append([x1 + xidx, y + 1])

    print("numbers: %s" % coords)
    return coords

summ = 0
for line_idx, line_raw in enumerate(INPUTS_RAW):
    line = line_raw[:-1]

    for idx, char in enumerate(line):
        if INPUTS_RAW[line_idx][idx] == '*':
            print("found star at %d:%d" % (idx, line_idx))
            numbers_found = numbers_around(idx, line_idx)
            if len(numbers_found) == 2:
                number1 = get_number(numbers_found[0][0], numbers_found[0][1])
                number2 = get_number(numbers_found[1][0], numbers_found[1][1])
                print("gear %d:%d - %s * %s" % (idx, line_idx, number1, number2))
                summ += int(number1) * int(number2)
                print("  new summ %d" %summ)
                

print(summ)
