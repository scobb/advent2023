
from util import harness
from typing import TextIO

if __name__ == '__main__':
    harness(15)

def hash(s: str) -> int:
    """
    Determine the ASCII code for the current character of the string.
    Increase the current value by the ASCII code you just determined.
    Set the current value to itself multiplied by 17.
    Set the current value to the remainder of dividing itself by 256
    """
    curr = 0
    for c in s:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr

def part_a(infile: TextIO) -> str:
    entries = infile.readline().strip().split(',')
    hashes = map(hash, entries)
    return str(sum(hashes))


def part_b(infile: TextIO) -> str:
    pass

