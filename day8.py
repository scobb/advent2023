
from util import harness
from typing import TextIO
import re

if __name__ == '__main__':
    harness(8)

regexp = r'(?P<k>[A-Z]{3}) = \((?P<l>[A-Z]{3}), (?P<r>[A-Z]{3})\)'

def part_a(infile: TextIO) -> str:
    mappings = {}
    mvt_pattern = infile.readline().strip()
    infile.readline()
    for line in infile.readlines():
        # print(line)
        if not line.strip():
            continue
        # AAA = (BBB, CCC)
        m = re.match(regexp, line)
        if m:
            mappings[m.group('k')] = {'L': m.group('l'),'R': m.group('r')}
        else:
            raise ValueError('no match')
        # print(mappings)
    steps = 0
    pos = 'AAA'
    while True:

        pos = mappings[pos][mvt_pattern[steps % len(mvt_pattern)]]
        steps += 1
        if pos == 'ZZZ':
            break
    return str(steps)




def part_b(infile: TextIO) -> str:
    pass

