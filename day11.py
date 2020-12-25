from sys import argv

"""
Advent of Code Day 11 Part 1
You are given a rectangular grid consisting of unusable spaces ("."), empty
spaces ("L"), or full spaces ("#"). A space that is empty or full will
transition to an empty or full space depending on the following rules:
-If an empty space has no full spaces next to it (including diagonally),
it becomes full
-If a full space has four or more full spaces adjacent to it
(including diagonally), it becomes empty
-If neither of the above conditions are true, the space stays the way it is
Eventually no spaces will transition from empty to full or vice versa,
determine how many full spaces exist in this stable state
Part 2
Instead of considering immediately adjacent spaces (including unusable "."
spaces), the first empty or full space in each direction (including diagonal)
are considered with unusable space irrelevant. In addition, a full space will
become empty if five or more spaces among those considered are full
"""

"""
Parses a grid of spaces and returns a grid where empty and full spaces are
transitioned according to the rules given in the problem description
"""
def grid_transition(grid):
    new_grid = []
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[i])):
            adjacent = 0
            #check above
            if i > 0:
                adjacent += 1 if grid[i - 1][j] == '#' else 0
                if j > 0:
                    adjacent += 1 if grid[i - 1][j - 1] == '#' else 0
                if j < len(grid[i]) - 1:
                    adjacent += 1 if grid[i - 1][j + 1] == '#' else 0
            #check on the side
            if j > 0:
                adjacent += 1 if grid[i][j - 1] == '#' else 0
            if j < len(grid[i]) - 1:
                adjacent += 1 if grid[i][j + 1] == '#' else 0
            #check below
            if i < len(grid) - 1:
                adjacent += 1 if grid[i + 1][j] == '#' else 0
                if j > 0:
                    adjacent += 1 if grid[i + 1][j - 1] == '#' else 0
                if j < len(grid[i]) - 1:
                    adjacent += 1 if grid[i + 1][j + 1] == '#' else 0
            #update new row
            if grid[i][j] == 'L' and adjacent == 0:
                row += '#'
            elif grid[i][j] == '#' and adjacent >= 4:
                row += 'L'
            else:
                row += grid[i][j]
        new_grid.append(row)

    return new_grid

"""
Helper function, checks the grid in certain (x, y) increments until a non-"."
space is reached or the edge is reached
"""
def grid_trace(grid, x, y, dx, dy):
    x += dx
    y += dy
    while y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y]):
        if grid[y][x] != '.':
            return 1 if grid[y][x] == '#' else 0
        x += dx
        y += dy
    return 0

"""
Parses a grid of spaces and returns a grid where empty and full spaces are
transitioned according to the rules given in part 2
"""
def grid_transition_2(grid):
    new_grid = []
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[i])):
            adjacent = 0
            #upper left
            adjacent += grid_trace(grid, j, i, -1, -1)
            #upper
            adjacent += grid_trace(grid, j, i, 0, -1)
            #upper left
            adjacent += grid_trace(grid, j, i, +1, -1)
            #left
            adjacent += grid_trace(grid, j, i, -1, 0)
            #right
            adjacent += grid_trace(grid, j, i, 1, 0)
            #lower left
            adjacent += grid_trace(grid, j, i, -1, +1)
            #lower
            adjacent += grid_trace(grid, j, i, 0, +1)
            #lower right
            adjacent += grid_trace(grid, j, i, +1, +1)
            #update new row
            if grid[i][j] == 'L' and adjacent == 0:
                row += '#'
            elif grid[i][j] == '#' and adjacent >= 5:
                row += 'L'
            else:
                row += grid[i][j]
        new_grid.append(row)

    return new_grid

if __name__ == "__main__":
    f = open(argv[1], 'r')
    grid = [i.strip() for i in f]
    grid_copy = grid[:]
    f.close()
    while True:
        new_grid = grid_transition(grid)
        if new_grid == grid:
            break
        grid = new_grid
    print(sum(row.count('#') for row in grid))
    grid = grid_copy
    while True:
        new_grid = grid_transition_2(grid)
        if new_grid == grid:
            break
        grid = new_grid
    print(sum(row.count('#') for row in grid))
