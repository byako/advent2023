#!/bin/python3
"""
Solution for task 4_1
"""

import os
import re

INPUT_FILE_NAME = 'input1.txt'

if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        INPUTS_RAW = input_file.readlines()

# for part 2
card_wins = []

# part 1
total_score = 0
for line_raw in INPUTS_RAW:
    line = line_raw[:-1]
    card_name, numbers = line.split(": ")

    winners, attempt = numbers.split(' | ')
    win_set = {int(num) for num in winners.split()}
    print("winners %s" % str(win_set))
    attempt_set = {int(num) for num in attempt.split()}
    print("attempt %s" % str(attempt_set))

    matched = win_set.intersection(attempt_set)
    # for part 2
    card_wins.append(matched)
    print("  match: %s" % str(matched))
    score = 0
    if len(matched):
        score = pow(2, len(matched) - 1)
    total_score += score
    print("score: %d, new total score: %d" % (score, total_score))

print("score %d" % total_score)

# part 2
total_score = 0
copies = [1]*len(card_wins)

for idx, card_win in enumerate(card_wins):
    print("card win: %s" % str(card_win))

    max_idx = idx + len(card_win)
    if max_idx > len(card_wins):
        max_idx = len(card_wins)

    for idx_plus in range(idx+1, max_idx+1):
        print("latest list: %s" % str(copies))
        copies[idx_plus] += copies[idx]

    print("latest list after copies: %s" % str(copies))

print("total cards: %d" % sum(copies))
