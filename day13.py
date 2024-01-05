
from util import harness
from typing import TextIO, List
from collections import defaultdict

if __name__ == '__main__':
    harness(13)

def find_reflection(rows: List[int]) -> int | None:
    val_to_pos = defaultdict(list)
    candidates = defaultdict(set)
    for idx, val in enumerate(rows):
        val_to_pos[val].append(idx)
        # print(val_to_pos[val])
        if len(val_to_pos[val]) > 1:
            for _idx in range(len(val_to_pos[val]) - 1):
                potential_candidate = val_to_pos[val][_idx] + idx
                if potential_candidate % 2 == 0:
                    continue
                candidate = (val_to_pos[val][_idx] + idx) // 2
                # print(val_to_pos[val], candidate)
                candidates[candidate].add(val_to_pos[val][_idx])
                candidates[candidate].add(idx)
                # print(candidates)
    print(candidates)
    for candidate, reflected in candidates.items():
        reflected = list(reflected)
        # print(candidate, reflected, len(rows) - 1)
        if 0 in reflected:
            print('*')
            # print(reflected[:candidate], list(range(candidate)))
            if all(req in reflected for req in range(candidate+1)):
                return candidate
        if len(rows) - 1 in reflected:
            print('**')
            # print(reflected[len(rows) - 2 - candidate:], list(range(candidate,len(rows))))
            # print(reflected[candidate:], list(range(candidate+1, len(reflected)+1)))
            if all(req in reflected for req in range(candidate, len(rows))):
                return candidate
    return None

def score(rows: List[int], cols: List[int]) -> int:
    print(rows)
    print(cols)
    row_ref = find_reflection(rows)
    if row_ref is not None:
        print(f'row_ref: {row_ref}')
        return (1+row_ref) * 100
    else:
        col_ref = find_reflection(cols)
        if col_ref is None:
            raise ValueError('no reflection')
        print(f'col_ref: {col_ref}')
        return 1+col_ref

def part_a(infile: TextIO) -> str:
    rows = []
    cols = []
    result = 0
    ctr = 0
    for line in infile.readlines():
        ls = line.strip()
        if not ls:
            ctr += 1
            result += score(rows, cols)
            # print(find_reflection(cols))
            rows = []
            cols = []
            continue
        cols = cols or [0 for _ in ls]
        row = 0
        for idx, ch in enumerate(ls):
            if ch == '#':
                row |= 1
                cols[idx] |= 1
            row <<= 1
            cols[idx] <<= 1
        rows.append(row)

    ctr+=1
    result += score(rows, cols)
    print(ctr)
    return str(result)


def part_b(infile: TextIO) -> str:
    pass

