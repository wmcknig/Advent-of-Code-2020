from sys import argv

"""
Advent of Code Day 12 Part 1
You are given a series of instructions for navigating along a grid of the
following forms:
-NC, SC, EC, WE for north, south, east, or west C units (C is a non-negative
integer)
-LD, RD for turning left or right by D degrees (D is non-negative multiple of
90)
-FC means move in the currently faced direction C units (C is a non-negative
integer)
You are initially facing east. Your facing direction only changes from L or
R instructions, any N, S, E, or W instruction (along with F) will not change
your facing. You are considered to start at the coordinates (0, 0).
Find the Manhattan distance from the starting position after following
all given instructions
Part 2
The instructions are now interpreted to refer to a waypoint, always defined
relative to the ship. N, S, E, and W mean moving the waypoint in the given
directions by the given amount relative to the ship, similarly to how they
meant moving the ship in part 1. L and R mean rotating the
waypoint around the ship. F, however, moves the ship by the waypoint the
given number of times; for instance, if the waypoint is (1, 2), F10 moves the
ship 10 units east and 20 units north.
The waypoint starts at 10 units east and 1 unit north.
Find the Manhattan distance from the starting position after following
all given instructions
"""

"""
Updates a given position and heading according to the instruction given for
part 1
"""
def update_pos(instruction, position, heading):
    prefix, value = instruction[0], int(instruction[1:])
    #handle cardinal directions
    if prefix == 'N':
        return (position[0], position[1] + value), heading
    if prefix == 'S':
        return (position[0], position[1] - value), heading
    if prefix == 'E':
        return (position[0] + value, position[1]), heading
    if prefix == 'W':
        return (position[0] - value, position[1]), heading
    #handle forward direction
    if prefix == 'F':
        return (position[0] + value * heading[0],
                position[1] + value * heading[1]), heading
    #handle turning
    if prefix == 'L':
        if value == 90:
            return position, (-heading[1], heading[0])
        if value == 180:
            return position, (-heading[0], -heading[1])
        if value == 270:
            return position, (heading[1], -heading[0])
    if prefix == 'R':
        if value == 90:
            return position, (heading[1], -heading[0])
        if value == 180:
            return position, (-heading[0], -heading[1])
        if value == 270:
            return position, (-heading[1], heading[0])
    #default case (not expected to ever be reached
    return position, heading

"""
Updates a given position and waypoint according to the instruction given for
part 2
"""
def update_waypoint(instruction, position, waypoint):
    prefix, value = instruction[0], int(instruction[1:])
    #handle cardinal directions
    if prefix == 'N':
        return position, (waypoint[0], waypoint[1] + value)
    if prefix == 'S':
        return position, (waypoint[0], waypoint[1] - value)
    if prefix == 'E':
        return position, (waypoint[0] + value, waypoint[1])
    if prefix == 'W':
        return position, (waypoint[0] - value, waypoint[1])
    #handle forward direction
    if prefix == 'F':
        return (position[0] + value * waypoint[0],
                position[1] + value * waypoint[1]), waypoint
    #handle turning
    if prefix == 'L':
        if value == 90:
            return position, (-waypoint[1], waypoint[0])
        if value == 180:
            return position, (-waypoint[0], -waypoint[1])
        if value == 270:
            return position, (waypoint[1], -waypoint[0])
    if prefix == 'R':
        if value == 90:
            return position, (waypoint[1], -waypoint[0])
        if value == 180:
            return position, (-waypoint[0], -waypoint[1])
        if value == 270:
            return position, (-waypoint[1], waypoint[0])
    #default case (not expected to ever be reached
    return position, heading

if __name__ == "__main__":
    f = open(argv[1], 'r')
    instructions = [i.strip() for i in f]
    f.close()
    position, heading = (0, 0), (1, 0)
    for i in instructions:
        position, heading = update_pos(i, position, heading)
    #print Manhattan distance
    print(abs(position[0]) + abs(position[1]))
    position, waypoint = (0, 0), (10, 1)
    for i in instructions:
        position, waypoint = update_waypoint(i, position, waypoint)
    #print Manhattan distance
    print(abs(position[0]) + abs(position[1]))

