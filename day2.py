
from util import harness
from typing import TextIO

if __name__ == '__main__':
    harness(2)


class Color:
    def __init__(self, s: str, limit: int):
        self.color_str = s
        self.limit = limit

class InvalidScenario(Exception):
    pass

def part_a(infile: TextIO) -> str:
    colors = [Color('red', 12), Color('green', 13), Color('blue', 14)]
    colors_by_str = {c.color_str: c for c in colors}
    result = 0
    for line in infile.readlines():
        if not line.strip():
            continue
        game_id_str, steps_str = line.split(":")
        game_id = int(game_id_str.split()[1])
        try:
            for _round in steps_str.split(';'):
                for num_color_str in _round.split(','):
                    num, color = num_color_str.strip().split()
                    if int(num) > colors_by_str[color].limit:
                        raise InvalidScenario()
        except InvalidScenario:
            continue
        else:
            result += game_id
    return str(result)





def part_b(infile: TextIO) -> str:
    pass

