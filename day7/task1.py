#!/bin/python3
"""
Solution for task 7_1
"""

import os
import re

INPUT_FILE_NAME = 'input1.txt'

if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r", encoding="UTF-8") as input_file:
        lines = input_file.readlines()

ranks = ['1','J','2','3','4','5','6','7','8','9','T','Q','K','A']
def hand_value(hand):
    val = ''
    for card in hand:
        val += "%02d" % ranks.index(card)
    print("hand %s value %s" % (hand, val))
    return val


bids = {}
combinations = [
    "highcard",
    "pair",
    "twopairs",
    "threeofakind",
    "fullhouse",
    "fourofakind",
    "fiveofakind"
]
hands_sorted = { combination: [] for combination in combinations}

combinations_map = {
    "5": "fiveofakind",
    "41": "fourofakind",
    "32": "fullhouse",
    "311": "threeofakind",
    "221": "twopairs",
    "2111": "pair",
    "11111": "highcard",
}

def phase1(orig_hand):
    '''sort out which hand it is'''
    counts = []
    hand = orig_hand
    jokers = 0
    while len(hand):
        print("hand %s counts %s, card: %s" % (hand, str(counts), hand[0]))
        same_cards = hand.count(hand[0])
        if hand[0] == 'J':
            jokers = same_cards
            print("found %d jokers (%d)" % (jokers, same_cards))
        else:
            counts.append(same_cards)

        hand = hand.replace(hand[0],'')

    counts.sort()
    counts.reverse()
    print("hand %s combination %s jokers %d" % (orig_hand, str(counts), jokers))
    if len(counts):
        counts[0] += jokers
    else:
        counts.append(jokers)
    print("after adding jokers: %s" % str(counts))
    combination = ''.join([str(x) for x in counts])
    print("decision: %s / %s" % (combination, combinations_map[combination]))
    hands_sorted[combinations_map[combination]].append(orig_hand)


# save bids
# categorize hand into combination
for line in lines:
    hand, bid_str = line[:-1].split()
    phase1(hand)
    bids[hand] = int(bid_str)

all_hands_sorted = []
for combination in hands_sorted:
    print("%s unsorted: %s\n" % (combination, str(hands_sorted[combination])))
    hands_sorted[combination].sort(key=hand_value)
    print("%s sorted  : %s\n" % (combination, str(hands_sorted[combination])))
    all_hands_sorted += hands_sorted[combination]

value = 0
for idx, hand in enumerate(all_hands_sorted):
    value += bids[hand] * (idx + 1)
    print("hand %4d %s  bid  %4d new value %d" % (idx + 1, hand, bids[hand], value))
print("value %d" % value)