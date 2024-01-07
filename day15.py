
from util import harness
from typing import TextIO
from collections import OrderedDict

if __name__ == '__main__':
    harness(15)

def hash(s: str) -> int:
    """
    Determine the ASCII code for the current character of the string.
    Increase the current value by the ASCII code you just determined.
    Set the current value to itself multiplied by 17.
    Set the current value to the remainder of dividing itself by 256
    """
    curr = 0
    for c in s:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr

def part_a(infile: TextIO) -> str:
    entries = infile.readline().strip().split(',')
    hashes = map(hash, entries)
    return str(sum(hashes))


def part_b(infile: TextIO) -> str:
    """
    Along the wall running parallel to the boxes is a large library containing lenses organized
        by focal length ranging from 1 through 9.

    The label will be immediately followed by a character that indicates the operation to perform:
        either an equals sign (=)
        or a dash (-)

    If the operation character is a dash (-),
        go to the relevant box and remove the lens with the given label
        if it is present in the box. Then, move any remaining lenses as
        far forward in the box as they can go without changing their order,
        filling any space made by removing the indicated lens.
        (If no lens in that box has the given label, nothing happens.)

    If the operation character is an equals sign (=), it will be followed by a number
        indicating the focal length of the lens that needs to go into the relevant box;
        be sure to use the label maker to mark the lens with the label given in the
        beginning of the step so you can find it later. There are two possible situations:

            1. If there is already a lens in the box with the same label, replace the old lens
            with the new lens: remove the old lens and put the new lens in its place, not moving
            any other lenses in the box.
            2. If there is not already a lens in the box with the same label, add the lens to the
            box immediately behind any lenses already in the box. Don't move any of the other lenses
            when you do this. If there aren't any lenses in the box, the new lens goes all the way
            to the front of the box.

    """
    hashmap = [OrderedDict() for _ in range(256)]
    entries = infile.readline().strip().split(',')
    for entry in entries:
        if entry[-1] == '-':
            label = entry[:-1]
            hashcode = hash(label)
            hashmap[hashcode].pop(label, None)
        else:
            label, focal_length = entry.split('=')
            hashcode = hash(label)
            hashmap[hashcode][label] = focal_length

    """
    The focusing power of a single lens is the result of multiplying together:

    One plus the box number of the lens in question.
    The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
    The focal length of the lens.
    """
    focusing_power = 0
    for box_number, box in enumerate(hashmap):
        for slot_number, label in enumerate(box):
            focal_length = int(box[label])
            focusing_power += focal_length * (1+box_number) * (1+slot_number)
    return str(focusing_power)