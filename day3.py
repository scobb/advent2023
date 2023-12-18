
from util import harness
from typing import TextIO, List, Callable, Set

if __name__ == '__main__':
    harness(3)


def _neighbors(matrix: List[List[str]], x: int, y: int):
    ys = [y]
    xs = [x]
    if y > 0:
        ys.append(y-1)
    if x > 0:
        xs.append(x-1)
    if y < len(matrix) - 1:
        ys.append(y+1)
    if x < len(matrix[0]) - 1:
        xs.append(x+1)
    return set(matrix[_y][_x] for _y in ys for _x in xs if (y != _y or x != _x))


def common(infile: TextIO, fn: Callable[[int,Set[str]], None]):
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
                if cur_num and (neighbors & symbols):
                    fn(int(cur_num), neighbors)
                    # print(f'found {cur_num}')
                    # print("VALID")
                    # result += int(cur_num)
                cur_num = ''
                neighbors = set()
        if cur_num and (neighbors & symbols):
            fn(int(cur_num), neighbors)


def part_a(infile: TextIO) -> str:
    result = 0
    def inner(part_no: int, neighbors: Set[str]):
        nonlocal result
        result += part_no
    common(infile, inner)
    return str(result)


def part_b(infile: TextIO) -> str:
    # idx_to_parts =
    pass
