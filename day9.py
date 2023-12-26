
from util import harness
from typing import TextIO, List

if __name__ == '__main__':
    harness(9)

def find_next(arr: List[int]) -> int:
    if all(x == 0 for x in arr):
        return 0
    deltas = []
    for idx in range(len(arr)-1):
        deltas.append(arr[idx+1]-arr[idx])
    return arr[-1] + find_next(deltas)


def part_a(infile: TextIO) -> str:
    result = 0
    for line in infile.readlines():
        if not line.strip():
            continue
        arr = list(map(int, line.split()))
        result += find_next(arr)
    return str(result)


def find_prev(arr: List[int]) -> int:
    if all(x == 0 for x in arr):
        return 0
    deltas = []
    for idx in range(len(arr)-1):
        deltas.append(arr[idx+1]-arr[idx])
    return arr[0] - find_prev(deltas)

def part_b(infile: TextIO) -> str:
    result = 0
    for line in infile.readlines():
        if not line.strip():
            continue
        arr = list(map(int, line.split()))
        result += find_prev(arr)
    return str(result)

