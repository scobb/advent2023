
from util import harness
from typing import TextIO
from collections import defaultdict

if __name__ == '__main__':
    harness(14)


def part_a(infile: TextIO) -> str:
    dp = None
    rocks = defaultdict(int)
    row_cnt = 0
    for row_idx, line in enumerate(infile.readlines()):
        ls = line.strip()
        if ls:
            row_cnt += 1
            dp = dp or [0 for _ in ls]
            for col_idx, c in enumerate(ls):
                if c == 'O':
                    rocks[dp[col_idx]] += 1
                    dp[col_idx] += 1
                elif c == '#':
                    dp[col_idx] = row_idx+1

    print(dp)
    print(rocks)
    print(row_cnt)
    result = sum((row_cnt - k) * v for k, v in rocks.items())
    return str(result)


def part_b(infile: TextIO) -> str:
    pass

