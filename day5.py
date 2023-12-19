
from util import harness
from typing import TextIO

if __name__ == '__main__':
    harness(5)


class IslandMap:
    def __init__(self, dest_start: int, source_start: int, length: int):
        self.source_start = source_start
        self.dest_start = dest_start
        self.length = length

    def __repr__(self):
        return f"(Map:{self.source_start}:{self.dest_start}:{self.length})"

    def maybe_map_source(self, src: int):
        if self.source_start <= src <= self.source_start + self.length:
            return self.dest_start + (src - self.source_start)


class MappingFound(Exception):
    pass

def part_a(infile: TextIO) -> str:
    # Each line within a map contains three numbers:
    #   the destination range start,
    #   the source range start, and
    #   the range length.

    # Any source numbers that aren't mapped correspond
    # to the same destination number. So, seed number 10
    # corresponds to soil number 10.

    # find the lowest location number that corresponds to
    # any of the initial seeds

    min_loc = float('inf')
    seeds = tuple(map(int, infile.readline().split(':')[1].split()))
    infile.readline()
    print(seeds)
    map_sets = []
    for idx in range(7):
        # label
        infile.readline()
        map_set = []
        while True:
            l = infile.readline()
            if not l.strip():
                break
            args = tuple(map(int, l.split()))
            map_set.append(IslandMap(*args))
        map_sets.append(map_set)
    print(map_sets)
    for seed in seeds:
        print(f'seed {seed}')
        cur = seed
        for idx, map_set in enumerate(map_sets):
            print(f'map {idx}')
            try:
                for mapping in map_set:
                    result = mapping.maybe_map_source(cur)
                    if result is not None:
                        print(f'mapped {cur} to {result}')
                        cur = result
                        raise MappingFound()
            except MappingFound:
                pass
        min_loc = min(min_loc, cur)
    return str(min_loc)



def part_b(infile: TextIO) -> str:
    pass

