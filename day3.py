from util import harness
from typing import TextIO, List, Callable, Set, Tuple
from collections import defaultdict
from functools import reduce
from operator import mul
if __name__ == '__main__':
    harness(3)


def _neighbors(matrix: List[List[str]], x: int, y: int) -> Set[Tuple[int, int]]:
    ys = [y]
    xs = [x]
    if y > 0:
        ys.append(y - 1)
    if x > 0:
        xs.append(x - 1)
    if y < len(matrix) - 1:
        ys.append(y + 1)
    if x < len(matrix[0]) - 1:
        xs.append(x + 1)
    return set((_y, _x) for _y in ys for _x in xs if (y != _y or x != _x))


def common(infile: TextIO, fn: Callable[[int, Set[Tuple[int, int]], List[List[str]], Set[str]], None]):
    matrix = [list(l.strip()) for l in infile.readlines() if l.strip()]
    symbols = set()
    for l in matrix:
        for c in l:
            if not c.isdigit() and c != '.':
                symbols.add(c)
    for y in range(len(matrix)):
        cur_num = ''
        neighbors = set()
        for x in range(len(matrix[0])):
            c = matrix[y][x]
            if c.isdigit():
                cur_num += c
                neighbors |= _neighbors(matrix, x, y)
            else:
                if cur_num:
                    fn(int(cur_num), neighbors, matrix, symbols)
                cur_num = ''
                neighbors = set()
        if cur_num:
            fn(int(cur_num), neighbors, matrix, symbols)


def part_a(infile: TextIO) -> str:
    result = 0

    def inner(part_no: int, neighbors: Set[Tuple[int, int]], matrix: List[List[str]], symbols: Set[str]):
        # print(f'examining {part_no}')
        for _y, _x in neighbors:
            if matrix[_y][_x] in symbols:
                nonlocal result

                result += part_no
                break

    common(infile, inner)
    return str(result)

def part_b(infile: TextIO) -> str:
    idx_to_parts = defaultdict(list)

    def inner(part_no: int, neighbors: Set[Tuple[int, int]], matrix: List[List[str]], _: Set[str]):
        # print(f'examining {part_no}')
        gears = set()
        for _y, _x in neighbors:
            if matrix[_y][_x] == '*':
                gears.add((_y,_x))
        for _y, _x in gears:
            nonlocal idx_to_parts
            idx_to_parts[(_y,_x)].append(part_no)
    common(infile, inner)
    result = 0
    for part_set in idx_to_parts.values():
        if len(part_set) == 2:
            result += reduce(mul, part_set)
    return str(result)