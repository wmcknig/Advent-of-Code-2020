from sys import argv
import re

"""
Advent of Code Day 16 Part 1
You are given a set of field rules, a comma-separated list of integers labeled
"your ticket", and a list of comma-separated lists of integers collectively
referred to as "nearby tickets". Said comma-separated lists are all of the
same length, where each position in the list corresponds to a specific field
that is constant across all of the lists (the first element in every list is
field a, the second element is field b, etc.). Which field corresponds to
which position is not initially known, but given comma-separated lists of
length n there are n field rules, each specifying a field name and the valid
values for said field.
Each field rule is of the form "NAME: A-B or C-D", where NAME is an arbitrary
string (it may include non-newline whitespace) and A, B, C, and D are integers
such that A <= B and C <= D. They specify that the given field is only
considered valid if its value is between A and B inclusive or between C and D
inclusive.
Among the comma-separated lists in the "nearby tickets" some contain values
that are considered invalid for all fields, find the sum of all of these
values
Part 2
Among the lists that contain no values considered invalid for all fields,
determine which fields map to which positions, then for the list "your ticket"
find the product of the values for all fields with "departure" in their names
"""

"""
Returns a list of all integers in the list that are invalid for all rules
"""
def invalid_for_all(l, rules):
    invalid = []
    for i in l:
        valid = False
        for rule in rules.values():
            lower_first, upper_first = rule[0]
            lower_second, upper_second = rule[1]
            if (i >= lower_first and i <= upper_first) or \
               (i >= lower_second and i <= upper_second):
                valid = True
                break
        if not valid:
            invalid.append(i)
    return invalid

"""
Returns a dictionary of field names with sets of potentially valid list
indexes for them
"""
def fields_for_each(l, rules):
    fields = {}
    for name, rule in rules.items():
        lower_first, upper_first = rule[0]
        lower_second, upper_second = rule[1]
        field_set = set()
        for n, i in enumerate(l):
            if (i >= lower_first and i <= upper_first) or \
               (i >= lower_second and i <= upper_second):
                field_set.add(n)
        fields[name] = field_set
    return fields

"""
Creates a dictionary of one-to-one name-value mappings where they can be
definitively established from a dictionary of names and possible values for
them
"""
def determine_mapping(d):
    mapping = {}
    already_mapped = set()
    #find names with one value that hasn't already been assigned
    assignment_made = True
    while assignment_made:
        assignment_made = False
        for name, value in d.items():
            not_mapped = value.difference(already_mapped)
            if len(not_mapped) == 1:
                mapping[name] = list(not_mapped)[0]
                already_mapped.add(list(not_mapped)[0])
                assignment_made = True
    return mapping

if __name__ == "__main__":
    f = open(argv[1], 'r')
    lines = [i.strip() for i in f.readlines()]
    f.close()
    index = 0
    #read field rules
    rules = {}
    while lines[index] != '':
        rule = re.match(r"(.+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)",
                        lines[index])
        rules[rule[1]] = ((int(rule[2]), int(rule[3])),
                          (int(rule[4]), int(rule[5])))
        index += 1
    #obtain "your ticket"
    index += 2
    your_ticket = list(int(i) for i in lines[index].split(","))
    #obtain "nearby tickets"
    index += 3
    nearby_tickets = []
    for line in lines[index:]:
        nearby_tickets.append(list(int(i) for i in line.split(",")))
    print(sum(map(sum,
                map(lambda x: invalid_for_all(x, rules), nearby_tickets))))
    #narrow down the possible fields for each list position
    fields = {i: set(range(len(your_ticket))) for i in rules}
    for i in filter(lambda x: len(invalid_for_all(x, rules)) == 0,
                                    nearby_tickets):
        current_fields = fields_for_each(i, rules)
        for j in fields:
            fields[j] = fields[j].intersection(current_fields[j])
    #now that the possible fields for every position are known, as much
    #as possible determine definitively which fields map to which positions
    #in each list
    mapping = determine_mapping(fields)
    #find the product of all fields in "your ticket" that have "departure" in
    #their name
    product = 1
    for i, v in mapping.items():
        if "departure" in i:
            product *= your_ticket[v]
    print(product)
