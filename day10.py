from sys import argv

"""
Advent of Code Day 10 Part 1
You are given a list of distinct non-negative integers which, along with
0 and the maximum value plus 3, can be ordered into an ascending sequence
where the difference between any adjacent pair is 1, 2, or 3. Count how many
of each kind of gap there are, and find the product of gaps of 1 and gaps of 3.
Part 2
It is possible to produce multiple ascending sequences where every adjacent
pair has a difference of 1, 2, or 3, and the sequence starts with 0 and ends
with the maximum of the list plus 3. Find every such distinct sequence
"""

"""
Produces a dictionary of differences between adjacent elements of the list and
how many times said difference appears in the sequence
"""
def gap_count(seq):
    gaps = {}
    for i in range(1, len(seq)):
        gap = seq[i] - seq[i - 1]
        gaps[gap] = gaps.get(gap, 0) + 1
    return gaps

"""
Counts how many ascending sequences of elements from the list, all ending with
the greatest element of the list, can be created where the gap between two
adjacent elements are at most n. Assumes the input list is sorted and itself
is one of these ascending sequences
Optimization: maintain a memo of possible subsequences for each given tail,
any partially completed sequence, given a particular remainder of the input
list, will have the same number of ways to complete itself
"""
def n_gap_sequence_count(seq, n, memo = {0: 1, 1: 1}):
    #base case, known number of ways to complete the partial sequence
    if len(seq) in memo:
        return memo[len(seq)]
    #recursively calls itself for each possible next element
    count = 0
    i = 1
    while len(seq) >= i + 1 and seq[i] - seq[0] <= n:
        count += n_gap_sequence_count(seq[i:], n, memo)
        i += 1
    memo[len(seq)] = count
    return count

if __name__ == "__main__":
    f = open(argv[1], 'r')
    numbers = [int(i) for i in f]
    numbers.sort()
    f.close()
    #explicitly includes zero at the beginning to ensure the gap between it
    #and the lowest element is counted
    numbers = [0] + numbers
    gaps = gap_count(numbers)
    #adds the gap between the maximal element and an element 3 greater than it
    print(gaps[1] * (gaps[3] + 1))
    print(n_gap_sequence_count(numbers, 3))
