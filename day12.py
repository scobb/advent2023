
from util import harness
from typing import TextIO, List

if __name__ == '__main__':
    harness(12)

# def rec(s: str, group_sizes: List[int], current_s_idx: int = 0, current_group: int = 0, current_group_idx: int = 0) -> int:



def part_a(infile: TextIO) -> str:
    """After the list of springs for a given row, the size of each contiguous
    group of damaged springs is listed in the order those groups appear in the row"""
    result = 0
    for line in infile.readlines():
        if not line.strip():
            continue
        puzzle, group_sizes = line.strip().split()
        group_sizes = tuple(map(int, group_sizes.split(',')))
        to_trav = [(0, 0, 0)]
        print(puzzle, group_sizes)
        inner_res = 0
        while to_trav:
            current_puzzle_idx, current_group, current_group_idx = to_trav.pop()
            if current_puzzle_idx == len(puzzle):
                if current_group == len(group_sizes):
                    inner_res += 1
                elif current_group == len(group_sizes) - 1 and group_sizes[current_group] == current_group_idx:
                    inner_res += 1
                continue
            c = puzzle[current_puzzle_idx]
            if current_group >= len(group_sizes):
                if c == '.' or c == '?':
                    to_trav.append((current_puzzle_idx+1,current_group,current_group_idx))
                continue
            if current_group_idx == 0:
                # no group started
                leave = (current_puzzle_idx+1,current_group,current_group_idx)
                take = (current_puzzle_idx+1,current_group,current_group_idx+1)
                if c == '.' or c == '?':
                    # print("LEAVE")
                    to_trav.append(leave)
                if c == '#' or c == '?':
                    # print("TAKE")
                    to_trav.append(take)
                continue
            elif current_group_idx < group_sizes[current_group]:
                # in progress
                # print("IN PROGRESS")
                if c == '#' or c == '?':
                    # print("CONTINUING PROGRESS")
                    to_trav.append((current_puzzle_idx+1,current_group,current_group_idx+1))
            else:
                # just finished - start new
                # print("JUST FINISHED")
                if c == '?' or c == '.':
                    to_trav.append((current_puzzle_idx+1,current_group+1,0))
        print(inner_res)
        result += inner_res
        # break
    return str(result)





def part_b(infile: TextIO) -> str:
    pass

