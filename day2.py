from sys import argv
import re

"""
Advent of Code Day 2 Part 1
You are given a list of strings of lowercase letters with associated rules
of the form X-Y Z, where X and Y are positive integers Y >= X indicating that
letter Z must appear at least X times and at most Y times in the string. Find
the number of strings that satisfy their respective rule
Part 2
The rules are of the same form, but X and Y indicate 1-indexed positions of
the string where one, and only one, of them need to be the character Z.
"""

"""
Parses a string of the form X-Y Z: .* into a pair of a three-tuple of
(X, Y, Z), where X and Y are integers and Z is a character, and the string .*
"""
def into_rule(s):
    regex_match = re.match(r"(.*): (.*)", s)
    rule = re.match(r"([0-9]+)-([0-9]+) (.)", regex_match[1])
    #test
    rule = (int(rule[1]), int(rule[2]), rule[3])
    return (rule, regex_match[2])

"""
Given a rule of form (X, Y, Z) where X and Y are integers Y >= X and a
character Z, check that there are at least X and at most Y elements of Z
in a given string
"""
def satisfies_rule(rule, s):
    letter_count = s.count(rule[2])
    return letter_count >= rule[0] and letter_count <= rule[1]

"""
Given a rule of form (X, Y, Z) where X and Y are integers Y >= X and a
character Z, check that one, and only one, of the characters of the string
indexed by X and Y is Z (note that the string is 1-indexed, 1 indicates the
first character of the string)
"""
def other_rule(rule, s):
    first_index = rule[0] - 1
    second_index = rule[1] - 1
    c = rule[2]
    return (s[first_index] == c and s[second_index] != c) or \
           (s[first_index] != c and s[second_index] == c)

if __name__ == "__main__":
    f = open(argv[1], 'r')
    inputlist = [i.strip() for i in f]
    f.close()
    #parse each line into a pair of a rule and a string
    validlist = filter(lambda e: satisfies_rule(e[0], e[1]),
                            map(into_rule, inputlist))
    print(len(list(validlist)))
    validlist = filter(lambda e: other_rule(e[0], e[1]),
                            map(into_rule, inputlist))
    print(len(list(validlist)))
