
from util import harness
from typing import TextIO

if __name__ == '__main__':
    harness(4)


def part_a(infile: TextIO) -> str:
    # (1 for the first match, then doubled three times for each of the three matches after the first)
    result = 0
    for line in infile.readlines():
        nums = line.split(':')[1]
        winning, mine = nums.split('|')
        winning_set = set(map(int, winning.split()))
        my_set = set(map(int, mine.split()))
        matches = len(winning_set & my_set)
        if matches > 0:
            result += 1 << (matches-1)
    return str(result)




def part_b(infile: TextIO) -> str:
    pass

