
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

"""
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, 
    but your sketch doesn't show what shape the pipe has.
"""
NORTH = (-1,0)
SOUTH = (1,0)
EAST = (0,1)
WEST = (0,-1)

r_splits = {
    # north and south
    '|': {
        # coming from the north - this is on the right
        # delta_y, delta_x
        NORTH: (WEST,),
        # coming from the south - this is on the right
        SOUTH: (EAST,),
    },
    # east and west.
    '-': {
        # coming from the east - this is on the right
        EAST: (NORTH,),
        # coming from the west - this is on the right
        WEST: (SOUTH,)
    },
    # L is a 90-degree bend connecting north and east.
    'L': {
        # coming from the north - this is on the right
        NORTH:(WEST, SOUTH),
        # coming form the east, this is on the right
        EAST:()
    },
    # J is a 90-degree bend connecting north and west.
    'J': {
        # coming from the north - this is on the right
        NORTH:(),
        # coming from the west, this is on the right
        WEST: (SOUTH,EAST,),
    },
    # 7 is a 90-degree bend connecting south and west.
    '7': {
        # coming from the south
        SOUTH:(EAST, NORTH),
        # from the west
        WEST:()
    },
    # F is a 90-degree bend connecting south and east.
    'F': {
        # coming from the south
        SOUTH: (),
        # from the east
        EAST: (WEST, NORTH)
    }
}
l_splits = {}
for k, v in r_splits.items():
    split = {}
    r_keys = tuple(v.keys())
    split[r_keys[0]] = v[r_keys[1]]
    split[r_keys[1]] = v[r_keys[0]]
    l_splits[k] = split


def part_b(infile: TextIO) -> str:

    grid = [l.strip() for l in infile.readlines() if l.strip()]
    s_pos = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                s_pos = y,x
                break
    pos = tuple(n for n in _neighbors(grid, s_pos[0], s_pos[1]))[0]
    prev = s_pos
    path = [s_pos]
    while True:
        # print(pos)
        _y,_x = pos
        candidates = tuple(n for n in _neighbors(grid,_y,_x) if n != prev)
        # print(candidates)
        if len(candidates) != 1:
            raise ValueError('unexpected multiple candidates')
        path.append(pos)
        prev = pos
        pos = candidates[0]
        if pos == s_pos:
            break

    # print(path)
    path_set = set(path)
    for splits in (r_splits, l_splits):
        try:
            inner_set = set()
            for idx in range(1,len(path)):
                prev = path[idx-1]
                cur = path[idx]
                from_dir = (prev[0]-cur[0],prev[1]-cur[1])
                pipe = grid[cur[0]][cur[1]]
                for delta in splits[pipe][from_dir]:
                    entry = cur[0]+delta[0],cur[1]+delta[1]
                    if 0 <= entry[0] < len(grid) and 0 <= entry[1] < len(grid[0]) and entry not in path_set:
                        inner_set.add(entry)
            candidates = inner_set.copy()
            while candidates:
                candidate = candidates.pop()
                neighbor_set = set(unfiltered_neighbors(candidate[0],candidate[1], grid))
                if len(neighbor_set) != 4:
                    raise BorderViolation()
                neighbor_set -= path_set
                neighbor_set -= inner_set
                if neighbor_set:
                    inner_set |= neighbor_set
                    candidates |= neighbor_set
            return str(len(inner_set))
        except BorderViolation:
            continue

class BorderViolation(Exception):
    pass

def unfiltered_neighbors(y: int, x:int, grid: List[List[str]]):
    if y > 0:
        yield y-1, x
    if x > 0:
        yield y, x-1
    if y < len(grid) - 1:
        yield y+1, x
    if x < len(grid[0]) - 1:
        yield y, x+1