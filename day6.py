
from util import harness
from typing import TextIO

if __name__ == '__main__':
    harness(6)


def part_a(infile: TextIO) -> str:
    times = tuple(map(int, infile.readline().split(":")[1].split()))
    distances = tuple(map(int, infile.readline().split(":")[1].split()))
    result = 1
    for idx in range(len(times)):
        wins = 0
        record = distances[idx]
        t = times[idx]
        for hold_time in range(t):
            if calc_distance(hold_time, t) > record:
                wins += 1
        result *= wins
    return str(result)


def calc_distance(hold_time: int, total_time: int) -> int:
    speed = hold_time
    run_time = total_time - hold_time
    return speed * run_time

import bisect
def part_b(infile: TextIO) -> str:
    t = int(infile.readline().split(":")[1].replace(' ',''))
    record = int(infile.readline().split(":")[1].replace(' ',''))
    start = t // 2
    key = lambda val: calc_distance(val, t)
    result = bisect.bisect_left(list(range(t//2)), record, key=key)
    return str(1 + (start - result) * 2)
