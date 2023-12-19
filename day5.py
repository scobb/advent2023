
from util import harness
from typing import TextIO, Tuple, List, Union

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
        if self.source_start <= src < self.source_start + self.length:
            return self.dest_start + (src - self.source_start)

    def partition_range(self, start: int, end: int) -> Tuple[Union[Tuple[int,int],None],List[Tuple[int,int]]]:
        # todo - split into mapped, unmapped
        # mapped = (start, end)
        # unmapped = [(start,end)]
        if end <= self.source_start or start >= self.source_start + self.length:
            return None, [(start,end)]
        else:
            unmapped = []
            mapping_start = max(start, self.source_start)
            mapping_end = min(end, self.source_start+self.length)
            mapped = (self.dest_start + (mapping_start-self.source_start), self.dest_start + (mapping_end-self.source_start))
            if start < mapping_start:
                unmapped.append((start, self.source_start))
            if end > mapping_end:
                unmapped.append((mapping_end, end))
        return mapped, unmapped


class MappingFound(Exception):
    pass

def parse_input(infile: TextIO) -> Tuple[Tuple[int],List[List[IslandMap]]]:
    seeds = tuple(map(int, infile.readline().split(':')[1].split()))
    infile.readline()
    # print(seeds)
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
    return seeds, map_sets

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
    seeds, map_sets = parse_input(infile)
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
    seeds, map_sets = parse_input(infile)
    # The values on the initial seeds: line come in pairs.
    # Within each pair, the first value is the start of the range
    # and the second value is the length of the range.
    execution_frames = []
    for idx in range(0,len(seeds),2):
        execution_frames.append((seeds[idx],seeds[idx]+seeds[idx+1],0,0))

    min_value = float('inf')
    while execution_frames:
        # end not inclusive
        start, end, mapset_idx, map_idx = execution_frames.pop()
        # print(start, end, mapset_idx, map_idx)
        if mapset_idx == len(map_sets):
            min_value = min(min_value, start)
            continue
        if map_idx == len(map_sets[mapset_idx]):
            # map as is
            execution_frames.append((start, end, mapset_idx+1, 0))
            continue

        mapping = map_sets[mapset_idx][map_idx]
        mapped, unmapped = mapping.partition_range(start, end)
        if mapped is not None:
            execution_frames.append((mapped[0],mapped[1],mapset_idx+1,0))
        for _s,_e in unmapped:
            execution_frames.append((_s,_e,mapset_idx,map_idx+1))
    return str(min_value)
