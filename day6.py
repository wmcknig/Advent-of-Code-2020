from sys import argv

"""
Advent of Code Day 6 Part 1
You are given a series of groups of lowercase alphabetical strings, where
each letter appears at most once. The groups are separated by empty lines,
with each line within a group containing one string.
Count the number of unique letters used in each group, and add the total
Part 2
Count the number of letters used by all members in each group, and add the
total
"""

"""
Returns how many unique letters are contained in a group
"""
def unique_letters(g):
    letters = set()
    for i in g:
        letters.update(set(i))
    return len(letters)

"""
Returns how many letters are common to all strings in a group
"""
def common_letters(g):
    letters = set(g[0])
    for i in g[1:]:
        letters.intersection_update(i)
    return len(letters)

if __name__ == "__main__":
    #process the groups into a list of lists of strings
    f = open(argv[1], 'r')
    groups = [s.split() for s in f.read().strip().split("\n\n")]
    f.close()
    print(sum(map(unique_letters, groups)))
    print(sum(map(common_letters, groups)))
