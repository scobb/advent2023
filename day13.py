
from util import harness
from typing import TextIO, List, Tuple, Set
from collections import defaultdict

if __name__ == '__main__':
    harness(13)

class Candidate:
    def __init__(self, idx: int, missing: Set[int]):
        self.idx = idx
        self.missing = missing

    def __repr__(self):
        return f"Candidate(idx={self.idx}, missing={self.missing})"

def find_reflection(rows: List[int], acceptable_misses: int = 0) -> List[Candidate]:
    val_to_pos = defaultdict(list)
    candidates = defaultdict(set)
    for idx, val in enumerate(rows):
        val_to_pos[val].append(idx)
        if len(val_to_pos[val]) > 1:
            for _idx in range(len(val_to_pos[val]) - 1):
                potential_candidate = val_to_pos[val][_idx] + idx
                if potential_candidate % 2 == 0:
                    continue
                candidate = (val_to_pos[val][_idx] + idx) // 2
                candidates[candidate].add(val_to_pos[val][_idx])
                candidates[candidate].add(idx)
    print(candidates)
    # if 0 not in candidates and acceptable_misses > 0:
    #     candidates[0] = set()
    # if len(rows) - 1 not in candidates and acceptable_misses > 0:
    #     candidates[len(rows)-1] = set()
    result = []
    for candidate, reflected in candidates.items():
        # reflected = list(reflected)
        if candidate < len(rows) // 2:
            front_set = set(range(candidate+1))
            front_diff = front_set - reflected
            # print(f'front_diff: {front_diff}')
            if len(front_diff) == acceptable_misses:
                result.append(Candidate(candidate, front_diff))
        else:
            back_set = set(range(candidate+1, len(rows)))
            back_diff = back_set - reflected
            if len(back_diff) == acceptable_misses:
                result.append(Candidate(candidate, back_diff))
    return result

def score(rows: List[int], cols: List[int]) -> int:
    print(rows)
    print(cols)
    row_ref = find_reflection(rows)
    if row_ref:
        print(f'row_ref: {row_ref}')
        return (1+row_ref[0].idx) * 100
    else:
        col_ref = find_reflection(cols)
        if not col_ref:
            raise ValueError('no reflection')
        print(f'col_ref: {col_ref}')
        return 1+col_ref[0].idx

def parse(infile: TextIO) -> Tuple[List[int], List[int]]:
    rows = []
    cols = []
    ls = infile.readline().strip()
    while ls:
        cols = cols or [0 for _ in ls]
        row = 0
        for idx, ch in enumerate(ls):
            if ch == '#':
                row |= 1
                cols[idx] |= 1
            row <<= 1
            cols[idx] <<= 1
        rows.append(row)
        ls = infile.readline().strip()
    return rows, cols

def part_a(infile: TextIO) -> str:
    result = 0
    while True:
        rows, cols = parse(infile)
        if not rows:
            break
        result += score(rows, cols)
    return str(result)


def find_smudged_reflection(rows: List[int]) -> Candidate | None:
    candidates = find_reflection(rows, 1)
    candidates.append(Candidate(0, {0}))
    candidates.append(Candidate(len(rows)-2, {len(rows)-1}))
    # max_row = max(rows)
    # print(candidates)
    # print(rows)
    for cand in candidates:
        missing_idx = cand.missing.pop()
        target_idx = cand.idx + (cand.idx + 1 - missing_idx)

        print('BLAH', cand.idx, missing_idx, target_idx, len(rows))
        # if not 0 <= target_idx < len(rows):
        #     continue
        target_val = rows[target_idx]
        smudge_val = rows[missing_idx]
        print(target_val, smudge_val, target_val ^ smudge_val)
        if count_ones(target_val ^ smudge_val) == 1:
            return cand
    return None

def count_ones(x: int) -> int:
    result = 0
    while x:
        if x & 1:
            result += 1
        x >>= 1
    return result

def part_b(infile: TextIO) -> str:
    result = 0
    ctr = 0
    while True:
        rows, cols = parse(infile)
        if not rows:
            break
        print('---')
        row_ref = find_smudged_reflection(rows)
        if row_ref is not None:
            print(f'row_ref: {row_ref}')
            result += 100 * (1+row_ref.idx)
        else:
            col_ref = find_smudged_reflection(cols)
            if col_ref is None:
                print(ctr, rows, cols)
                for row in rows:
                    print(format(row, '016b'))
                raise ValueError('no reflection')
            print(f'col_ref: {col_ref}')
            result += (1+col_ref.idx)
        ctr += 1
    return str(result)
