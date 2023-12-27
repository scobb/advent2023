
from util import harness
from typing import TextIO, Tuple, List, Iterable

if __name__ == '__main__':
    harness(10)

'''

    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, 
    but your sketch doesn't show what shape the pipe has.

'''
NORTH_SET = ('|', 'L', 'J', 'S')
SOUTH_SET = ('|', '7', 'F', 'S')
EAST_SET = ('-', 'L', 'F', 'S')
WEST_SET = ('-', 'J', '7', 'S')
def _neighbors(grid: List[List[str]], y: int, x: int) -> Iterable[Tuple[int,int]]:
    ch = grid[y][x]
    if y > 0 and ch in NORTH_SET and grid[y-1][x] in SOUTH_SET:
        yield y-1,x
    if x > 0 and ch in WEST_SET and grid[y][x-1] in EAST_SET:
        yield y,x-1
    if y < len(grid) - 1 and ch in SOUTH_SET and grid[y+1][x] in NORTH_SET:
        yield y+1,x
    if x < len(grid[0]) - 1 and ch in EAST_SET and grid[y][x+1] in WEST_SET:
        yield y, x+1


def part_a(infile: TextIO) -> str:
    """
    How many steps along the loop does it take to get from the starting position
    to the point farthest from the starting position?

    """
    grid = [l.strip() for l in infile.readlines() if l.strip()]
    s_pos = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                s_pos = y,x
                break
    pos = tuple(n for n in _neighbors(grid, s_pos[0], s_pos[1]))[0]
    prev = s_pos
    cnt = 0
    while True:
        # print(pos)
        _y,_x = pos
        candidates = tuple(n for n in _neighbors(grid,_y,_x) if n != prev)
        # print(candidates)
        if len(candidates) != 1:
            raise ValueError('unexpected multiple candidates')
        cnt += 1
        prev = pos
        pos = candidates[0]
        if pos == s_pos:
            break
    return str(1+cnt // 2)




def part_b(infile: TextIO) -> str:
    pass

