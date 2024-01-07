
from util import harness
from typing import TextIO, Tuple, List

if __name__ == '__main__':
    harness(16)

RIGHT = (0,1)
UP = (-1,0)
LEFT = (0,-1)
DOWN = (1,0)


def reflect(c: str, direction: Tuple[int,int]) -> Tuple[int,int]:
    delta_y,delta_x = direction
    if c == '/':
        return -delta_x,-delta_y
    if c == '\\':
        return delta_x,delta_y
    return direction

def split(c: str, direction: Tuple[int,int]) -> List[Tuple[int,int]]:
    if c == '|' and direction in (RIGHT, LEFT):
        return [UP, DOWN]
    if c == '-' and direction in (UP, DOWN):
        return [RIGHT, LEFT]
    return [direction]

def part_a(infile: TextIO) -> str:
    grid = [l.strip() for l in infile.readlines() if l.strip()]
    beams = [(0,-1,RIGHT)]
    return str(traverse(grid, beams))

def traverse(grid, beams) -> int:
    energized = set()
    traversed = set()

    while beams:
        y,x,direction = beams.pop()
        delta_y,delta_x = direction
        y += delta_y
        x += delta_x
        if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and (y,x,direction) not in traversed:
            energized.add((y,x))
            traversed.add((y,x,direction))
            c = grid[y][x]
            direction = reflect(c, direction)
            for _direction in split(c, direction):
                beams.append((y,x,_direction))
    return len(energized)

def part_b(infile: TextIO) -> str:
    grid = [l.strip() for l in infile.readlines() if l.strip()]
    result = 0
    # top row
    for col in range(len(grid[0])):
        result = max(result, traverse(grid, [(-1,col,DOWN)]))
    # right col
    for row in range(len(grid)):
        result = max(result, traverse(grid, [(row,len(grid[0]), LEFT)]))
    # bottom row
    for col in range(len(grid[0])):
        result = max(result, traverse(grid, [(len(grid),col,UP)]))
    # left col
    for row in range(len(grid)):
        result = max(result, traverse(grid, [(row,-1, RIGHT)]))
    # beams = [(0,-1,RIGHT)]
    # return traverse(grid, beams)
    return str(result)

