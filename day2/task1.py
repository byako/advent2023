#!/bin/python3
"""
Solution for task 2_1
"""

import os
import re

INPUT_FILE_NAME = 'input1.txt'

if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        INPUTS_RAW = input_file.readlines()

condition = {
"red": 12,
"green": 13,
"blue": 14,
}

games = {}
for line_raw in INPUTS_RAW:
    line = line_raw[:-1]
    game_id, game_rounds_str = line.split(": ")
    game_number = int(game_id.split(" ")[-1])
    game = []
    for game_round_str in game_rounds_str.split("; "):
        game_round = {}
        for game_cubes in game_round_str.split(", "):
            cube_count, cube_color = game_cubes.split(" ")
            game_round[cube_color] = int(cube_count)
        game.append(game_round)
    print("game %d: " % game_number)
    print(game)
    games[game_number] = game

# part 1
summ = 0
for game, game_rounds in games.items():
    game_ok = True
    for game_round in game_rounds:
        for cube_color in game_round:
            if game_round[cube_color] > condition[cube_color]:
                print("cubes %s more than condition: %s" % (cube_color, str(game_round)))
                game_ok = False
                break
        if not game_ok:
            break
    if game_ok:
        print("game %d ok" % game)
        summ += game
    else:
        print("game %d not ok" % game)

print(summ)

# part 2
summ = 0
for game, game_rounds in games.items():
    game_min = {"green": 0, "red": 0, "blue": 0}
    for game_round in game_rounds:
        for cube_color in game_round:
            if game_round[cube_color] > game_min[cube_color]:
                game_min[cube_color] = game_round[cube_color]
    print("game min: %s" % str(game_min))
    game_power = 1
    for color in condition:
        game_power *= game_min[color]
    print("game_power %d" % game_power)
    summ += game_power

print(summ)
