
from util import harness
from typing import TextIO, Tuple, Dict
import re

if __name__ == '__main__':
    harness(8)

regexp = r'(?P<k>[A-Z0-9]{3}) = \((?P<l>[A-Z0-9]{3}), (?P<r>[A-Z0-9]{3})\)'

def parse(infile: TextIO) -> Tuple[str,Dict[str,Dict[str,str]]]:
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
    return mvt_pattern, mappings

def part_a(infile: TextIO) -> str:
    mvt_pattern, mappings = parse(infile)
    steps = 0
    pos = 'AAA'
    while True:

        pos = mappings[pos][mvt_pattern[steps % len(mvt_pattern)]]
        steps += 1
        if pos == 'ZZZ':
            break
    return str(steps)


def part_b(infile: TextIO) -> str:
    mvt_pattern, mappings = parse(infile)

    steps = 0
    positions = [k for k in mappings if k.endswith('A')]
    solutions = [[] for _ in positions]
    solution_freq = [None for _ in positions]
    while True:
        for idx in range(len(positions)):
            pos = positions[idx]
            positions[idx] = mappings[pos][mvt_pattern[steps % len(mvt_pattern)]]
            if positions[idx].endswith('Z'):
                solutions[idx].append(steps+1)
                if len(solutions[idx]) > 1:
                    solution_freq[idx] = solutions[idx][1] - solutions[idx][0]

        steps += 1
        if all(freq is not None for freq in solution_freq):
            break
    print(solution_freq)
    from math import lcm
    return str(lcm(*solution_freq))