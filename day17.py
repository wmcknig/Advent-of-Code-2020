from sys import argv

"""
Advent of Code Day 17 Part 1
You are given an infinite 3D grid where each integer coordinate (x, y, z) is
considered active or inactive. Each timestep a coordinate changes according
to rules based on its surrounding 26 integer coordinates (coordinates where
each x, y, or z varies from its own x, y, or z by 0 or 1).
-If a coordinate is active and 2 or 3 of its surrounding coordinates are
active, it remains active. Otherwise, it becomes inactive
-If a coordinate is inactive but 3 of its surrounding coordinates are
active, it becomes active. Otherwise, it remains inactive
Given a 2D section of the grid (assumed at a given value for one dimension),
determine how many active coordinates there are after 6 timesteps
Part 2
The grid is 4 dimensional, given the same adjacency rules but in 4 dimensions
and a 2D section of the grid (assumed at the same given value for 2 dimensions)
determine how many active coordinates there are after 6 timesteps
"""

"""
Given a set of active spaces, return a list of active spaces after one
timestep according to the rules given for part 1
"""
def timestep(active):
    result = set()
    inactive = set()
    #check whether each active space transitions or not, and accumulate
    #a set of inactive spaces to check
    for x, y, z in active:
        #generate all adjacent spaces to check (note: generates 27
        #spaces including itself because of ease of computation)
        adjacent = [(x + i, y + j, z + k) for i in (-1, 0, 1)
                            for j in (-1, 0, 1) for k in (-1, 0, 1)]
        count = 0
        for space in adjacent:
            if space in active:
                count += 1
            else:
                inactive.add(space)
        #count is compared to values one-greater to account for the space
        #itself being counted
        if count == 3 or count == 4:
            result.add((x, y, z))
    #check the inactive spaces found to be adjacent to at least one active
    #space
    for x, y, z in inactive:
        #generate all adjacent spaces to check (note: generates 27
        #spaces including itself because of ease of computation)
        adjacent = [(x + i, y + j, z + k) for i in (-1, 0, 1)
                            for j in (-1, 0, 1) for k in (-1, 0, 1)]
        count = 0
        for space in adjacent:
            if space in active:
                count += 1
        if count == 3:
            result.add((x, y, z))

    return result

"""
Given a set of active spaces, return a list of active spaces after one
timestep according to the rules given for part 1
Changed to work in 4D
"""
def timestep_4d(active):
    result = set()
    inactive = set()
    #check whether each active space transitions or not, and accumulate
    #a set of inactive spaces to check
    for x, y, z, w in active:
        #generate all adjacent spaces to check (note: generates 81
        #spaces including itself because of ease of computation)
        adjacent = [(x + i, y + j, z + k, w + l) for i in (-1, 0, 1)
                            for j in (-1, 0, 1) for k in (-1, 0, 1)
                            for l in (-1, 0, 1)]
        count = 0
        for space in adjacent:
            if space in active:
                count += 1
            else:
                inactive.add(space)
        #count is compared to values one-greater to account for the space
        #itself being counted
        if count == 3 or count == 4:
            result.add((x, y, z, w))
    #check the inactive spaces found to be adjacent to at least one active
    #space
    for x, y, z, w in inactive:
        #generate all adjacent spaces to check (note: generates 81
        #spaces including itself because of ease of computation)
        adjacent = [(x + i, y + j, z + k, w + l) for i in (-1, 0, 1)
                            for j in (-1, 0, 1) for k in (-1, 0, 1)
                            for l in (-1, 0, 1)]
        count = 0
        for space in adjacent:
            if space in active:
                count += 1
        if count == 3:
            result.add((x, y, z, w))

    return result

if __name__ == "__main__":
    f = open(argv[1])
    rows = [i.strip() for i in f]
    f.close()
    #the slice is considered to be at z=0 by convention
    active = set()
    for y, row in enumerate(rows):
        for x, v in enumerate(row):
            if v == '#':
                active.add((x, y, 0))
    #for part 2
    active_4d = set((x, y, z, 0) for (x, y, z) in active)
    for _ in range(6):
        active = timestep(active)
    print(len(active))
    for _ in range(6):
        active_4d = timestep_4d(active_4d)
    print(len(active_4d))
