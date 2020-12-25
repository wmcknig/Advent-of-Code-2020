from sys import argv
from math import ceil

"""
Advent of Code Day 13 Part 1
You are given a positive integer and a comma-separated list where every
element is an 'x' or a positive integer. From the numbers in that list
find the one with the smallest multiple equal to or greater than the
initial non-listed number you are given. the product of the listed number and
the difference between its multiple and the non-listed number (for example,
given the number 939 and listed numbers 7, 13, 59, 31, and 19, 944 is a
multiple of 59 and the smallest such multiple of any of the listed numbers
greater than or equal to 939, so you would get 59 * (944 - 939) = 295)
Part 2
Find the smallest positive integer N that is a multiple of the first number in
the list where N+1 is a multiple of the second element, N+2 is a multiple of
the third element, and so on. 'x' values are placeholders that only affect
positions for numbers. For example, given a list A, B, x, x, C, you would
want to find the smallest N such that N is a multiple of A, N+1 is a multiple
of B, and N+4 is a multiple of C. It can be assumed that the first element
of the list is a positive integer.
"""

"""
Finds the smallest multiple of any positive integer from the list greater
than or equal to the threshold
"""
def least_multiple_threshold(threshold, l):
    return min(((i, ceil(threshold / i) * i) for i in l), key=lambda x: x[1])

"""
Finds the smallest integer N such that for every n, i pair N % n = i
Assumes that at least two such pairs are given in a list
Optimization: if the numbers in the list can be guaranteed to be pairwise
coprime, it can be guaranteed (per the Chinese remainder theorem) that there
is one unique integer N less than prod(all n's). Let it be assumed that the
numbers in the list are pairwise coprime (the particular problem source
seems to guarantee they are primes in any event)
"""
def congruent_for_all(congruences):
    increment = congruences[0][0]
    result = congruences[0][1]
    #for each sequence of numbers congruent to their respective i's modulo
    #their respective n's, find the first number congruent to i' for its n'
    for n, i in congruences[1:]:
        while result % n != i:
            result += increment
        increment *= n
    return result

if __name__ == "__main__":
    f = open(argv[1], 'r')
    lines = f.readlines()
    f.close()
    threshold = int(lines[0])
    numbers = lines[1].split(',')
    number, least_multiple = least_multiple_threshold(threshold,
            map(int, filter(lambda x: x.isnumeric(), numbers)))
    print(number * (least_multiple - threshold))
    congruences = []
    for i, n in enumerate(numbers):
        if n.isnumeric():
            congruences.append((int(n), -i % int(n)))
    print(congruent_for_all(congruences))
