from typing import TextIO
import os
import sys
import traceback

def get_input_filepath(name: str) -> str:
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(script_directory, 'inputs', name)


def get_output_filepath(name: str) -> str:
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(script_directory, 'outputs', name)


def get_script_filepath(name: str) -> str:
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(script_directory, name)


def call_fn(day: int, infile: TextIO, fn_name: str) -> str:
    module = __import__(f"day{day}")
    main = getattr(module, fn_name)
    return main(infile)

def harness(day: int) -> None:
    try:
        for part in ('a', 'b'):
            samplefile_path = f"{day}sample.txt"
            if os.path.exists(get_input_filepath(f"{day}{part}sample.txt")):
                samplefile_path = f"{day}{part}sample.txt"
            print(samplefile_path)
            with open(get_input_filepath(samplefile_path)) as samplefile:
                with open(get_output_filepath(f"{day}{part}.txt")) as resultfile:
                    expected = resultfile.read().strip()
                # part a
                sample_result = call_fn(day, samplefile, f'part_{part}')
                if sample_result != expected:
                    raise ValueError(f"Mismatch in part {part} sample: '{expected}' does not match '{sample_result}'")
                print('---')
            with open(get_input_filepath(f"{day}.txt")) as infile:
                result = call_fn(day, infile, f'part_{part}')
                print(f"PART {part} RESULT: '{result}'")
    except Exception as exc:
        print(f"UNEXPECTED EXCEPTION IN PART {part}: {exc}")
        print(traceback.format_exc())

