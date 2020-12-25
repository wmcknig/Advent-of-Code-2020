"""
Advent of Code Day 15 Part 1
You are given a starting sequence of integers. Starting from the last number
of the list, if the current number has not occurred previously in the list,
append 0 to the list. If it has occurred previously in the list, append
the number of places before the current instance it last occurred in the
list. Repeat this process with the appended number as the new current number.
Find the 2020th number in the sequence given the starting sequence
Part 2
Find the 30000000th number in the sequence given the starting sequence
"""

"""
Find the next number given the last number in the sequence, its index, and
a dictionary of the last occurrance of numbers that have occurred in the list.
"""
def next_number(n, i, d):
    if n not in d:
        d[n] = i
        return 0
    diff = i - d[n]
    d[n] = i
    return diff

if __name__ == "__main__":
    #the starting sequence, this is improper but set this directly as the
    #input
    #STARTING_SEQUENCE = [2, 0, 6, 12, 1, 3]
    STARTING_SEQUENCE = [0, 3, 6]
    last_occurrance = {}
    for i, n in enumerate(STARTING_SEQUENCE[:-1]):
        last_occurrance[n] = i
    number = STARTING_SEQUENCE[-1]
    index = len(STARTING_SEQUENCE) - 1
    number = next_number(number, index, last_occurrance)
    index += 1
    #index starts at 0, so the 2020th number is at index 2019
    while index < 2019:
        number = next_number(number, index, last_occurrance)
        index += 1
    print(number)
    while index < 29999999:
        number = next_number(number, index, last_occurrance)
        index += 1
    print(number)
