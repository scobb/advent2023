
from util import harness
from typing import TextIO, Callable, List, Tuple
import functools

if __name__ == '__main__':
    harness(2)


class Color:
    def __init__(self, s: str, limit: int):
        self.color_str = s
        self.limit = limit
        self.min_val = 0

class InvalidScenario(Exception):
    pass

colors = [Color('red', 12), Color('green', 13), Color('blue', 14)]
colors_by_str = {c.color_str: c for c in colors}

def common(infile: TextIO, game_fn: Callable[[int, List[Tuple[int, Color]]], int]):
    result = 0
    for line in infile.readlines():
        if not line.strip():
            continue
        game_id_str, steps_str = line.split(":")
        game_id = int(game_id_str.split()[1])
        # steps = steps_str.split(';')
        rounds = []
        for _round in steps_str.split(';'):
            for num_color_str in _round.split(','):
                num, color = num_color_str.strip().split()
                rounds.append((int(num), colors_by_str[color]))
        result += game_fn(game_id, rounds)
    return result

def part_a(infile: TextIO) -> str:
    def inner(game_id: int, rounds: List[Tuple[int, Color]]):
        try:
            for num, color in rounds:
                if num > color.limit:
                    raise InvalidScenario()
        except InvalidScenario:
            return 0
        return game_id
    result = common(infile, inner)
    return str(result)

def part_b(infile: TextIO) -> str:
    def inner(game_id: int, rounds: List[Tuple[int, Color]]):
        mins = {c.color_str: 0 for c in colors}
        for cnt, clr in rounds:
            mins[clr.color_str] = max(mins[clr.color_str], cnt)
        result = functools.reduce(lambda a, b: a*b, mins.values())
        return result

    result = common(infile, inner)
    return str(result)
    # result = 0
    # for line in infile.readlines():
    #     if not line.strip():
    #         continue
    #     game_id_str, steps_str = line.split(":")
    #     game_id = int(game_id_str.split()[1])
    #     try:
    #         for _round in steps_str.split(';'):
    #             for num_color_str in _round.split(','):
    #                 num, color = num_color_str.strip().split()
    #                 colors_by_str[color].min_val = max(colors_by_str[color].min_val, num)



