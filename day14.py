
from util import harness
from typing import TextIO, Tuple
from functools import cache
from collections import defaultdict

if __name__ == '__main__':
    harness(14)


def part_a(infile: TextIO) -> str:
    return common(infile, 1)

@cache
def slide(rocks: Tuple[Tuple[int, int, str]]) -> Tuple[Tuple[int,int,str]]:
    result = []
    dp = defaultdict(int)
    for rock in rocks:
        row_idx, col_idx, c = rock
        if c == 'O':
            result.append((dp[col_idx], col_idx, c))
            dp[col_idx] += 1
        else:
            result.append((row_idx, col_idx, c))
            dp[col_idx] = row_idx + 1
    return tuple(result)

@cache
def rotate(rocks: Tuple[Tuple[int, int, str]], num_cols: int) -> Tuple[Tuple[int,int,str]]:
    return tuple(sorted((col_idx, num_cols - row_idx - 1, c) for (row_idx, col_idx, c) in rocks))


def print_map(rocks: Tuple[Tuple[int, int, str]], num_rows: int, num_cols: int):
    rock_map = {(row_idx, col_idx): c for (row_idx, col_idx, c) in rocks}
    result = []
    for row_idx in range(num_rows):
        result.append('')
        for col_idx in range(num_cols):
            result[row_idx] += rock_map.get((row_idx, col_idx), '.')
    print('\n'.join(result))


def common(infile: TextIO, rotations: int) -> str:
    rocks = []
    row_cnt = 0

    for row_idx, line in enumerate(infile.readlines()):
        ls = line.strip()
        if ls:
            row_cnt += 1
            col_cnt = len(ls)
            for col_idx, c in enumerate(ls):
                if c in ('O', '#'):
                    rocks.append((row_idx, col_idx, c))
    results = defaultdict(list)
    directions = ('n', 'w', 's', 'e')
    for idx in range(rotations):
        # print(idx)
        rocks = slide(tuple(rocks))
        if idx == rotations - 1:
            result = sum((row_cnt - r[0]) for r in rocks if r[2] == 'O')
            return str(result)
        results[rocks].append(idx)
        if len(results[rocks]) > 3:
            cycle_length_a = results[rocks][-1] - results[rocks][-2]
            cycle_length_b = results[rocks][-2] - results[rocks][-3]
            if cycle_length_a == cycle_length_b and (rotations - idx) % cycle_length_a == 0:
                # get back to north orientation
                rocks = rotate(rocks, row_cnt)
                # print_map(rocks, row_cnt, col_cnt)
                result = sum((row_cnt - r[0]) for r in rocks if r[2] == 'O')
                return str(result)
        rocks = rotate(rocks, row_cnt)


def part_b(infile: TextIO) -> str:
    return common(infile, 4*1000000000 - 1)
