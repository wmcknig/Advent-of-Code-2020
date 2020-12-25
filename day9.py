from sys import argv
from itertools import combinations

"""
Advent of Code Day 9 Part 1
You are given a list of non-negative integers, the first 25 of which are
considered a preamble. Every integer after this preamble should be a sum of
any pair X, Y of the 25 integers immediately preceding it (X may only equal Y
if X occurs multiple times among these preceding integers).
There is at least one integer in the list that is not the sum of a pair of
the 25 preceding integer, find the first such integer
Part 2
Given this integer, find a contiguous sublist at least length 2 from the list
of numbers that sums to it. Take the sum of the largest and smallest numbers
in this sublist
"""

"""
Given a list of integers and a preamble length n, find the first integer after
the preamble that is not a sum of a pair of the n preceding numbers
"""
def first_error(l, n):
    #generate list of sums of preamble pairs
    #note: naively recomputes sums
    index = 0
    while True:
        sums = set(x[0] + x[1] for x in combinations(l[index:index + n], 2))
        if l[index + n] not in sums:
            return l[index + n]
        index += 1

"""
Finds the first contiguous sublist of at least length 2 that adds to the
given number
"""
def sum_sublist(l, n):
    first = 0
    last = 1
    total = l[first] + l[last]
    #starting with the first two numbers, extend the sublist down the list if
    #the sum is too low, and remove the top element of the sublist if the
    #sum is too high. Make sure that the sublist is not just a single element
    while total != n:
        if total < n or first == last:
            last += 1
            total += l[last]
        elif total > n:
            total -= l[first]
            first += 1

    return l[first:last + 1]

if __name__ == "__main__":
    f = open(argv[1], 'r')
    numbers = [int(i) for i in f]
    f.close()
    error = first_error(numbers, 25)
    print(error)
    sublist = sum_sublist(numbers, error)
    print(min(sublist) + max(sublist))
