
from util import harness
from typing import TextIO
from collections import Counter

if __name__ == '__main__':
    harness(7)


card_order = '23456789TJQKA'
card_score = {c: idx for idx, c in enumerate(card_order)}

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_OF_A_KIND = 3
FULL_HOUSE = 4
FOUR_OF_A_KIND= 5
FIVE_OF_A_KIND = 6
def score(hand: str) -> int:
    # Five of a kind, where all five cards have the same label: AAAAA
    # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    # High card,
    card_counts = sorted(Counter(hand).values(), reverse=True)
    if card_counts[0] == 5:
        hand_score = FIVE_OF_A_KIND
    elif card_counts[0] == 4:
        hand_score = FOUR_OF_A_KIND
    elif card_counts[0] == 3 and card_counts[1] == 2:
        hand_score = FULL_HOUSE
    elif card_counts[0] == 3:
        hand_score = THREE_OF_A_KIND
    elif card_counts[0] == 2 and card_counts[1] == 2:
        hand_score = TWO_PAIR
    elif card_counts[0] == 2:
        hand_score = ONE_PAIR
    else:
        hand_score = HIGH_CARD
    score = hand_score << 24
    for idx in range(5):
        score |= card_score[hand[idx]] << (20 - (4 * idx))
    # print(hand, '{:10X}'.format(score))
    return score


def part_a(infile: TextIO) -> str:
    tuples = []
    for line in infile.readlines():
        if not line.strip():
            continue
        hand, bid = line.split()
        tuples.append((score(hand), int(bid)))
    tuples.sort()
    # print(tuples)
    return str(sum((idx+1)*tup[1] for idx, tup in enumerate(tuples)))

def part_b(infile: TextIO) -> str:
    pass

