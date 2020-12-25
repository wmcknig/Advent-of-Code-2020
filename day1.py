from sys import argv
from itertools import combinations

"""
Advent of Code Day 1 Part 1
You are given a positive integer and a list of positive integers. There are
two elements of the list that sum to the aforementioned positive integer;
find this pair and its product
Part 2
Find the triplet of elements from the list that sum to the aforementioned
positive integer and its product
"""

"""
Finds every n-tuple (n) of numbers (in list l) that adds to the given sum (x).
Returns a list of n-tuples.
"""
def adds_to_x(x, l, n):
    candidates = combinations(l, n)
    return list(filter(lambda t: sum(t) == x, candidates))

if __name__ == "__main__":
    given_sum = int(argv[1])
    given_list = []
    f = open(argv[2], 'r')
    given_list = [int(i) for i in f]
    f.close()
    #part 1 results
    for i in adds_to_x(given_sum, given_list, 2):
        print(i, i[0] * i[1])
    #part 2 results
    for i in adds_to_x(given_sum, given_list, 3):
        print(i, i[0] * i[1] * i[2])
