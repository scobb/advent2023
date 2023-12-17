
from util import harness
from typing import TextIO

if __name__ == '__main__':
    harness(1)


def calibration_value(line: str) -> int:
    result = ''
    for c in line:
        if c.isdigit():
            result += c
            break
    for c in reversed(line):
        if c.isdigit():
            result += c
            break
    print(result)
    return int(result)

def part_a(infile: TextIO) -> str:
    return str(sum(calibration_value(l) for l in infile.readlines()))


def part_b(infile: TextIO) -> str:
    pass

