"""
Solution for task 1_1
"""

import os
import re

INPUT_FILE_NAME = 'input1.txt'

if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        INPUTS_RAW = input_file.readlines()

number = 0

numbermap = {
    "one":   1,
    "two":   2,
    "three": 3,
    "four":  4,
    "five":  5,
    "six"  : 6,
    "seven": 7,
    "eight": 8,
    "nine" : 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

lines = []

#part 1
for value in INPUTS_RAW:
    line = []
    for char in value:
        if char.isnumeric():
            line.append(int(char))
    if len(line) == 0:
        print("Line does not have enough numbers")
    else:
        new_number = line[0] * 10 + line[-1]
        print("new number: %d" % new_number)
        number += new_number

print("total: %d" % number)

number = 0
# part 2
for value in INPUTS_RAW:
    linedict = {}
    line = []
    print("line: %s" % value)
    # search all occurances of all numbers
    for k, v in numbermap.items():
        occurs = [m.start() for m in re.finditer(k, value)]
        if len(occurs):
            print("%s occurs in" % k)
            print(occurs)
            # save what string number was at what index
            for idx in occurs:
                linedict[int(idx)] = k

    if len(linedict) == 0:
        print("Line does not have enough numbers")
    else:
        print("found numbers:")
        print(linedict)
        linedict_keys = sorted(linedict.keys())
        print("linedict keys ordered:")
        print(linedict_keys)

        new_number = numbermap[linedict[linedict_keys[0]]] * 10 + numbermap[linedict[linedict_keys[-1]]]
        print("new number: %d" % new_number)
        number += new_number

print("total: %d" % number)
