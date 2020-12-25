from sys import argv
from itertools import product
import re

"""
Advent of Code Day 21 Part 1
You are given a list of items of the form
"STRING[ STRING]* (contains STRING[, STRING])", where the part outside
paranthesis is an arbitrary space-separated list and the part inside the
paranthesis is a comma-separated list. Every element of the former list
maps to one or no elements of the latter list, and each element of the
latter list maps to one and only one element of the former list; all
mappings between the former and the latter are one-to-one. These
rules apply both for each individual line and for the entire set of
elements contained in the former kind of list and the set of elements
in the latter kind of list.
Determine which members of the former kind of list provably do not map
to any members of the latter kind of list, and count how many times
they appear in the input
Part 2
Determine the pairing of mappings between the two kinds of list and produce
a list of the values from the former alphabetically ordered by their
corresponding value from the latter
"""

"""
Given a dictionary of variables and their allowed values, returns a dictionary
of variables and their possible values
"""
def valid_values(d):
    #generates the cartesian product of each value list and filters it for
    #cases where the product contains no repeated elements
    #ensures that keys and values maintain a common ordering
    variables = []
    values = []
    for variable, value in d.items():
        variables.append(variable)
        values.append(value)
    result = {variable: [] for variable in d}
    for assignment in product(*values):
        #there is one distinct value for each variable
        if len(set(assignment)) == len(d):
            for i, j in zip(variables, assignment):
                result[i].append(j)
    return result

if __name__ == "__main__":
    f = open(argv[1], 'r')
    lines = [i.strip() for i in f]
    f.close()
    possible_assignments = {}
    all_values = set()
    rules = []
    for line in lines:
        v = re.match(r"(.+) \(contains (.+)\)", line)
        variables = v[2].split(", ")
        values = v[1].split()
        rules.append((variables, values))
        all_values.update(values)
        #each variable maps to exactly one value, so said value must be
        #common to every line containing the variable
        for i in variables:
            if i in possible_assignments:
                possible_assignments[i] = \
                        possible_assignments[i].intersection(set(values))
            else:
                possible_assignments[i] = set(values)
    assignment = valid_values(possible_assignments)
    unused = all_values
    for i in assignment.values():
        unused = unused.difference(set(i))
    count = 0
    for i in unused:
        for j in rules:
            if i in j[1]:
                count += 1
    print(count)
    assignment = list((i, j[0]) for i, j in assignment.items())
    assignment.sort()
    print(",".join(i[1] for i in assignment))
