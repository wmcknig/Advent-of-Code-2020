from sys import argv
import re

"""
Advent of Code Day 7 Part 1
You are given a series of rules expressed in the form
"TONE COLOR bags contain [((COUNT TONE COLOR bag(s))+ | no other bags).]"
Said rules specify that bags of a certain description must contain
a certain number each of bags of their own respective descriptions (or
contain no bags at all). Given a bag of a certain description that must
be stored in another bag, how many kinds of bags may contain (directly
or nestedly) said bag?
Part 2
Given a bag of a certain description, determine how many bags it must
contain.
"""

"""
Given a string representing a rule, parse it into a pair of a bag and a list
of (number, description)
"""
def parse_rule(s):
    RULE_FORMAT = r"([a-z]+ [a-z]+) bags contain (([0-9]+ [a-z]+ [a-z]+ bag(s)?, )*[0-9]+ [a-z]+ [a-z]+ bag(s)?|(no other bags))\."
    parsed = re.match(RULE_FORMAT, s)
    subject = parsed[1]
    predicate_strings = re.findall(r"[0-9]+ [a-z]+ [a-z]+ bag", parsed[2])
    predicate = []
    for i in predicate_strings:
        match = re.match(r"([0-9]+) ([a-z]+ [a-z]+) bag", i)
        predicate.append((int(match[1]), match[2]))
    return (subject, predicate)

"""
Given a starting bag and a dictionary of bags and the bags that may contain
them, count how many kinds of bags may contain the starting bag.
"""
def outermost_bags(bag, held_by):
    queue = held_by[bag]
    containers = set()
    while len(queue) > 0:
        elem = queue.pop()
        #check to prevent circular enqueueing
        if elem not in containers:
            containers.add(elem)
            #check bag can be held by another bag
            if elem in held_by:
                queue += held_by[elem]
    return containers

"""
Given a starting bag and a dictionary of bags and the bags it must contain,
Determine how many bags are contained by the starting bag.
Note: this assumes no bag contains itself (this would logically imply
infinite bags)
"""
def bag_contains(bag, rules):
    count = 0
    for elem in rules[bag]:
        count += elem[0] * (bag_contains(elem[1], rules) + 1)
    return count

if __name__ == "__main__":
    #parse rules
    f = open(argv[1], 'r')
    rules = list(map(parse_rule, f.readlines()))
    f.close()
    #construct dictionary of bags and bags that may hold them
    held_by = {}
    for bag, holds in rules:
        for elem in holds:
            newlist = held_by.get(elem[1], [])
            newlist.append(bag)
            held_by[elem[1]] = newlist
    print(len(outermost_bags("shiny gold", held_by)))
    #the rules list is a list of pairs, which Python can natively translate
    #into a dict
    print(bag_contains("shiny gold", dict(rules)))
