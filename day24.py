from sys import argv

"""
Advent of Code Day 24 Part 1
You are given a hexagonal grid where all spaces are initially considered
"white". You are given a list of strings consisting of undelimited substrings
"e" for east, "w" for west, "se" for southeast, "sw" for southwest, "ne" for
northeast, and "nw" for northwest. These strings denote a path starting from
an arbitrary reference space; the destination space is flipped from "black" to
"white" or vice versa.
Traverse all paths starting from the reference space, flip the end space from
"white" to "black" or vice versa, and count how many spaces are considered
"black" at the end.
Part 2
Given the state produced by the process above, an iteration simultaneously
changes each spaces state according to the previous space state as follows:
-any "black" space with 0 or more than 2 adjacent "black" spaces transitions
to "white"
-any "white" space with exactly 2 adjacent "black" spaces transitions to
"black"
Determine how many spaces are "black" after 100 iterations
"""

"""
Traverses a path starting from a reference "zero" starting space and updates
the given set of "black" spaces accordingly
Note: uses a "3D" coordinate system for hexagons
"""
def hex_traverse(path):
    #start at initial space
    space = (0, 0, 0) #STUB
    for step in path:
        if step == "e":
            space = (space[0] + 1, space[1] + 1, space[2])
        elif step == "w":
            space = (space[0] - 1, space[1] - 1, space[2])
        elif step == "ne":
            space = (space[0], space[1] + 1, space[2] + 1)
        elif step == "nw":
            space = (space[0] - 1, space[1], space[2] + 1)
        elif step == "se":
            space = (space[0] + 1, space[1], space[2] - 1)
        elif step == "sw":
            space = (space[0], space[1] - 1, space[2] - 1)
        #invalid step, ignore
        else:
            continue
        #if it's in the set, remove it, else add it
    return space

"""
Applies the part 2 iteration rules to a given set of spaces, producing a new
set of "black" spaces (spaces not listed are considered "white")
"""
def iteration(black):
    result = set()
    #produce a set of "white" spaces that are adjacent to those in the "black"
    #set and thus might transition
    white = set()
    for space in black:
        adjacent = (space[0] + 1, space[1] + 1, space[2])
        if adjacent not in black:
            white.add(adjacent)
        adjacent = (space[0] - 1, space[1] - 1, space[2])
        if adjacent not in black:
            white.add(adjacent)
        adjacent = (space[0], space[1] + 1, space[2] + 1)
        if adjacent not in black:
            white.add(adjacent)
        adjacent = (space[0] - 1, space[1], space[2] + 1)
        if adjacent not in black:
            white.add(adjacent)
        adjacent = (space[0] + 1, space[1], space[2] - 1)
        if adjacent not in black:
            white.add(adjacent)
        adjacent = (space[0], space[1] - 1, space[2] - 1)
        if adjacent not in black:
            white.add(adjacent)
    #apply transition rules to "white" spaces that might transition
    for space in white:
        count = 0
        adjacent = (space[0] + 1, space[1] + 1, space[2])
        if adjacent in black:
            count += 1
        adjacent = (space[0] - 1, space[1] - 1, space[2])
        if adjacent in black:
            count += 1
        adjacent = (space[0], space[1] + 1, space[2] + 1)
        if adjacent in black:
            count += 1
        adjacent = (space[0] - 1, space[1], space[2] + 1)
        if adjacent in black:
            count += 1
        adjacent = (space[0] + 1, space[1], space[2] - 1)
        if adjacent in black:
            count += 1
        adjacent = (space[0], space[1] - 1, space[2] - 1)
        if adjacent in black:
            count += 1
        if count == 2:
            result.add(space)
    #apply transition rules to "black" spaces that might transition
    for space in black:
        count = 0
        adjacent = (space[0] + 1, space[1] + 1, space[2])
        if adjacent in black:
            count += 1
        adjacent = (space[0] - 1, space[1] - 1, space[2])
        if adjacent in black:
            count += 1
        adjacent = (space[0], space[1] + 1, space[2] + 1)
        if adjacent in black:
            count += 1
        adjacent = (space[0] - 1, space[1], space[2] + 1)
        if adjacent in black:
            count += 1
        adjacent = (space[0] + 1, space[1], space[2] - 1)
        if adjacent in black:
            count += 1
        adjacent = (space[0], space[1] - 1, space[2] - 1)
        if adjacent in black:
            count += 1
        if not (count == 0 or count > 2):
            result.add(space)
    return result

if __name__ == "__main__":
    f = open(argv[1], 'r')
    lines = [i.strip() for i in f]
    f.close()
    paths = []
    for line in lines:
        index = 0
        current_path = []
        while index < len(line):
            if line[index] == 'n' or line[index] == 's':
                current_path.append(line[index:index + 2])
                index += 2
            else:
                current_path.append(line[index])
                index += 1
        paths.append(current_path)
    #set of black spaces, there are none initially
    blacks = set()
    for path in paths:
        dest = hex_traverse(path)
        if dest in blacks:
            blacks.remove(dest)
        else:
            blacks.add(dest)
    print(len(blacks))
    for i in range(100):
        blacks = iteration(blacks)
    print(len(blacks))
