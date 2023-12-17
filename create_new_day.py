from argparse import ArgumentParser
import os
import sys

from util import get_script_filepath, get_input_filepath, get_output_filepath

script_fmt_str = """
from util import harness
from typing import TextIO

if __name__ == '__main__':
    harness({day_number})


def part_a(infile: TextIO) -> str:
    pass


def part_b(infile: TextIO) -> str:
    pass

"""

def multline_parse_to_file(input_kind: str, file_path: str) -> None:
    print(f"Enter/Paste {input_kind}. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    with open(file_path, 'w') as writefile:
        writefile.write('\n'.join(contents))

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('day_number', type=int)
    args = parser.parse_args()
    day_number = args.day_number
    print(day_number)
    script_fp = get_script_filepath(f'day{day_number}.py')
    print(script_fp)
    if os.path.exists(script_fp):
        print(f"Script {script_fp} already exists.")
        sys.exit(1)

    with open(script_fp, 'w') as script_file:
        script_file.write(script_fmt_str.format(day_number=day_number))
    multline_parse_to_file('sample inputs', get_input_filepath(f'{day_number}sample.txt'))
    multline_parse_to_file('part a sample outputs', get_output_filepath(f'{day_number}a.txt'))
    multline_parse_to_file('inputs', get_input_filepath(f'{day_number}.txt'))
