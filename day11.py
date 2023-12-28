
from util import harness
from typing import TextIO
import bisect

if __name__ == '__main__':
    harness(11)



"""
Due to something involving gravitational effects, only some space expands. 
In fact, the result is that any rows or columns that contain no galaxies 
should all actually be twice as big.
"""
def part_a(infile: TextIO) -> str:
    return common(infile, 2)
def common(infile: TextIO, expansion_factor: int) -> str:
    galaxies = []
    galaxy_ys = set()
    galaxy_xs = set()
    total_ys = 0
    total_xs = 0
    for y, line in enumerate(infile.readlines()):
        if not line.strip():
            continue
        sline = line.strip()
        total_xs = len(sline)
        total_ys = y + 1
        for x in range(len(sline)):
            if sline[x] == '#':
                galaxies.append((y,x))
                galaxy_xs.add(x)
                galaxy_ys.add(y)
    missing_xs = sorted(set(range(total_xs)) - galaxy_xs)
    missing_ys = sorted(set(range(total_ys)) - galaxy_ys)

    # print(galaxies, missing_ys, missing_xs)
    result = 0
    # print(missing_ys, missing_xs)
    for idxa in range(len(galaxies)):
        for idxb in range(idxa+1, len(galaxies)):
            g1 = galaxies[idxa]
            g2 = galaxies[idxb]
            y_range = sorted([g1[0], g2[0]])
            x_range = sorted([g1[1], g2[1]])
            skipped_ys = bisect.bisect_left(missing_ys, y_range[1]) - bisect.bisect_left(missing_ys, y_range[0])
            skipped_xs = bisect.bisect_left(missing_xs, x_range[1]) - bisect.bisect_left(missing_xs, x_range[0])
            # print(y_range, missing_ys, skipped_ys, x_range, missing_xs, skipped_xs)
            # print(x_range, skipped_xs)
            result += abs(g1[0]-g2[0]) + abs(g1[1]-g2[1]) + (skipped_xs + skipped_ys)*(expansion_factor-1)
    return str(result)


def part_b(infile: TextIO) -> str:
    return common(infile, 1000000)

