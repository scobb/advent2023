
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

str_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
rev_str_digits = {
    k[::-1]: v for k, v in str_digits.items()
}

def calibration_value_b(line: str) -> int:
    result = ''
    for idx, c in enumerate(line):
        if c.isdigit():
            result += c
            break
        else:
            for length in range(3,6):
                # print(f'examining {line[idx:idx+length]}')
                if line[idx:idx+length] in str_digits:
                    result += str_digits[line[idx:idx+length]]
                    break
            if result:
                break
    rev_line = line[::-1]
    for idx,c in enumerate(rev_line):
        if c.isdigit():
            result += c
            break
        else:
            for length in range(3,6):
                # print(f'examining {rev_line[idx:idx+length]}')
                if rev_line[idx:idx+length] in rev_str_digits:
                    result += rev_str_digits[rev_line[idx:idx+length]]
                    break
            if len(result) == 2:
                break
    print(result)
    return int(result)
def part_b(infile: TextIO) -> str:
    return str(sum(calibration_value_b(l) for l in infile.readlines()))

