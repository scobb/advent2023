
from util import harness
from typing import TextIO, Tuple, Set

if __name__ == '__main__':
    harness(4)

def count_wins(line: str) -> int:
    nums = line.split(':')[1]
    winning, mine = nums.split('|')
    winning_set = set(map(int, winning.split()))
    my_set = set(map(int, mine.split()))
    return len(winning_set & my_set)

def part_a(infile: TextIO) -> str:
    # (1 for the first match, then doubled three times for each of the three matches after the first)
    result = 0
    for line in infile.readlines():
        matches = count_wins(line)
        if matches > 0:
            result += 1 << (matches-1)
    return str(result)

def part_b(infile: TextIO) -> str:
    lines = list(l.strip() for l in infile.readlines() if l.strip())
    card_cnt = [1 for _ in lines]
    for idx, line in enumerate(lines):
        matches = count_wins(line)
        for offs in range(1,matches+1):
            card_cnt[idx+offs] += card_cnt[idx]
    return str(sum(card_cnt))
