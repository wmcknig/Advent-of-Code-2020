from sys import argv

"""
Advent of Code Day 5 Part 1
You are given a list of strings where each string consists of the characters
F, B, L, or R, meaning front, back, left, or right, respectively. The strings
consist of 10 characters, the first seven of them being F or B and the
latter three being L or R. The first seven progressively narrow down
the halves of an array of 128 elements, front indicating the lower half
and back indicating the upper half of the given partition; said partition
is the entire array for the first character, the front or back for the
second, the front or back of one of those for the third, and so on. This is
likewise with the last three characters and an array of 8 elements, with the
left being the lower half and the right being the upper half. Taken as a whole
the string indicates an element from 0 to 127 and an element from 0 to 7.
Given such an element pair, multiply the first element by 8 and add the
second element to get a unique ID. Find the largest such ID from the list
Part 2
The strings make up a contiguous range of integers with the exception of
one skipped character in that range; find that missing integer.
"""

"""
Parses a string into a seat id
Equivalent to parsing an unisgned binary integer where B and R correspond to
1 and F and L correspond to 0 (this is obvious from the problem statement
but was not made explicit there to keep up a practice of restating the
problem)
"""
def parse_string(s):
    binary_string = "0b"
    for i in s:
        if i in "FL":
            binary_string += "0"
        elif i in "BR":
            binary_string += "1"
    return int(binary_string, 2)

if __name__ == "__main__":
    f = open(argv[1], 'r')
    strings = [i.strip() for i in f]
    f.close()
    #made a list so it's reusable
    idlist = list(map(parse_string, strings))
    print(max(idlist))
    #find the missing element from the contiguous range
    print(set(range(min(idlist), max(idlist))).difference(set(idlist)))
