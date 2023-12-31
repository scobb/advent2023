
from util import harness
from typing import TextIO, Callable, Tuple, List
from functools import cache

if __name__ == '__main__':
    harness(12)


def part_a(infile: TextIO) -> str:
    return common_it(infile, lambda puzzle, group_sizes: (puzzle, group_sizes))


@cache
def rec(puzzle: str, group_sizes: Tuple[int], current_puzzle_idx: int, current_group: int, current_group_idx: int) -> int:
    if current_puzzle_idx == len(puzzle):
        if current_group == len(group_sizes):
            return 1
        elif current_group == len(group_sizes) - 1 and group_sizes[current_group] == current_group_idx:
            return 1
        return 0
    c = puzzle[current_puzzle_idx]
    if current_group >= len(group_sizes):
        if c == '.' or c == '?':
            return rec(puzzle, group_sizes, current_puzzle_idx+1, current_group, current_group_idx)
        return 0
    if current_group_idx == 0:
        # no group started
        result = 0
        if c == '.' or c == '?':
            # print("LEAVE")
            result += rec(puzzle, group_sizes, current_puzzle_idx + 1, current_group, current_group_idx)
        if c == '#' or c == '?':
            # print("TAKE")
            result += rec(puzzle, group_sizes, current_puzzle_idx + 1, current_group, current_group_idx + 1)
        return result
    elif current_group_idx < group_sizes[current_group]:
        # in progress
        # print("IN PROGRESS")
        if c == '#' or c == '?':
            # print("CONTINUING PROGRESS")
            return rec(puzzle, group_sizes, current_puzzle_idx + 1, current_group, current_group_idx + 1)
    else:
        # just finished - start new
        # print("JUST FINISHED")
        if c == '?' or c == '.':
            return rec(puzzle, group_sizes, current_puzzle_idx + 1, current_group + 1, 0)
    return 0

def common_it(infile: TextIO, row_xform: Callable[[str, Tuple[int]],Tuple[str,Tuple[int]]]) -> str:
    """After the list of springs for a given row, the size of each contiguous
    group of damaged springs is listed in the order those groups appear in the row"""
    result = 0
    for line in infile.readlines():
        if not line.strip():
            continue
        puzzle, group_sizes = line.strip().split()
        group_sizes = tuple(map(int, group_sizes.split(',')))
        puzzle, group_sizes = row_xform(puzzle, group_sizes)
        # print(type(group_sizes))

        inner_res = rec(puzzle, group_sizes, 0, 0, 0)
        # print(puzzle, inner_res)
        result += inner_res
        # break
    return str(result)


def unfold_record(record: str, group_sizes: Tuple[int]) -> Tuple[str, Tuple[int]]:
    """replace the list of spring conditions with five copies of itself (separated by ?)
    and replace the list of contiguous groups of damaged springs with five copies of itself (separated by ,).
    """
    return '?'.join([record] * 5), group_sizes * 5


def part_b(infile: TextIO) -> str:
    return common_it(infile, unfold_record)

