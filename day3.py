from sys import argv
from math import prod

"""
Advent of Code Day 3 Part 1
You are given a rectangular grid of empty spaces, represented by '.', and
filled spaces, represented by '#'. Said grid repeats itself indefinitely
horizontally; the grid represents a grid with a copy of itself to its right,
and that grid has a copy of itself to its right, ad infinitum. For a given
rational slope, where each move down Y elements corresponds to a move right
X elements, determine how many filled spaces are contained among the spaces
in the rational slope from the top left corner (which can be assumed to be
empty) to the bottom row
Note: for slopes that can't be expressed as an integer (X units right per 1
unit down), it is assumed, for lack of alternative explanation, that the
slope can skip rows in this case
Part 2
Do the same as for part 1 for each of multiple given slopes, then find their
products
"""

"""
Determines how many filled spaces are encountered in an integer slope
from the top left to the bottom of the grid. It is assumed that the grid
contains at least one row, and all rows are of the same length
"""
def intersection_count(grid, slope):
    x_position = 0
    count = 0
    slope_width = len(grid[0])
    for i in grid[slope[1]::slope[1]]:
        x_position = (x_position + slope[0]) % slope_width
        if i[x_position] == '#':
            count += 1
    return count

if __name__ == "__main__":
    #this is typically improper but for ease of use the slope is hardcoded;
    #this can be readily changed by a user by simply modifying the values
    #below
    SLOPE = (3, 1)
    SLOPE_LIST = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    f = open(argv[1], 'r')
    grid = [i.strip() for i in f]
    f.close()
    print(intersection_count(grid, SLOPE))
    intersection_list = map(lambda x: intersection_count(grid, x), SLOPE_LIST)
    print(prod(intersection_list))
