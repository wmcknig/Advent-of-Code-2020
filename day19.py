from sys import argv
from itertools import product

"""
Advent of Code Day 19 Part 1
You are given a series of rules and a series of messages. The rules are
numbered and are of the form "NUM: STR" (STR is itself a string in
double quotes), "NUM: RULE(...)", or "NUM: (RULE(...) |)(...) RULE(...)".
A rule of the first type matches a single character, a rule of the second
type matches a string that can be split into substrings matching the listed
subrules in order, and the third type matches a string that can be split into
substrings matching one of the "|" separated lists of subrules.
Count how many messages satisfy rule 0
Part 2
Replace rule 8 with "42 | 42 8" and rule 11 with "42 31 | 42 11 31"; this
means that some rules can now match an infinite number of strings
"""

"""
Tests a string to see if it satisfies a given rule
"""
def generate_strings(rules, rule):
    #base case, rule is a string
    if type(rule) is str:
        return [rule]
    #rule is at least one list of rules
    generated = []
    for subrule in rule:
        generated_sub = [""]
        for i in subrule:
            suffixes = generate_strings(rules, rules[i])
            temp = []
            for prefix in generated_sub:
                temp += [prefix + suffix for suffix in suffixes]
            generated_sub = temp
        generated += generated_sub
    return generated

"""
Given a set of rules, an ordered list of rules for a string, and a string,
attempts to decompose the string into rules by expanding the first term of
the rule and progressively removing the prefix of the string
"""
def satisfies_rule(rules, rule, s):
    #base case where all rules have been exhausted or there are no elements
    #in the string, implicitly assumes there are no empty string literals in
    #the rule set
    if s == "" or rule == []:
        return s == "" and rule == []
    #case where first rule in list is a string literal, check the string
    #suffix if the prefix matches, return false otherwise
    head = rules[rule[0]]
    if type(head) is str:
        if s.startswith(head):
            return satisfies_rule(rules, rule[1:], s[len(head):])
        else:
            return False
    #case where the first rule in list is a list of rule lists
    return any(satisfies_rule(rules, r + rule[1:], s) for r in head)

if __name__ == "__main__":
    f = open(argv[1], 'r')
    lines = [i.strip() for i in f]
    f.close()
    rules = {}
    #parse until an empty line is reached
    index = 0
    while lines[index] != "":
        line = lines[index].split(": ")
        rule_number, rule = int(line[0]), line[1]
        #rule is a character
        if "\"" in rule:
            rules[rule_number] = rule[1:-1]
        #rule is at least one list of rules
        else:
            rule = rule.split(" | ")
            subrules = []
            for i in rule:
                subrules.append(list(int(j) for j in i.split()))
            rules[rule_number] = subrules
        index += 1
    #get strings from the remainder of the lines
    messages = lines[index + 1:]
    print(len(list(filter(lambda s: satisfies_rule(rules, [0], s),
                                        messages))))
    #alter the rules
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    print(len(list(filter(lambda s: satisfies_rule(rules, [0], s),
                                        messages))))
