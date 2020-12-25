"""
Advent of Code Day 23 Part 1
You are given a circular list of integers (the element after the last element
is the first element). The first value of the list is initially set as the
current value. For each iteration:
-the three values following the current value are removed
-the three elements just removed are placed, in their original ordering,
immediately after the highest element in the list smaller than the current
value (if there are no elements in the list less than the current value, the
highest value in the list is used instead)
-the value next to the current value in the list is set as the new current
value
Determine the list after 100 iterations, written starting from the value
following 1 in the list
Part 2
Given the initial list, append in order every value from one greater than the
max of the list to 1000000 inclusive (the first value of the list succeeds
1000000, naturally). Perform 10000000 (ten million) iterations on this
circular list, and find the product of the two numbers succeeding 1.
"""

"""
An element in a linked list
Note: this approach is used instead of a native Python list to avoid
memory reallocation issues from large shuffling
"""
class LinkedElem:
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, n):
        self.next = n

"""
Perform an iteration on the circular list as described in part 1
It is assumed that current is an element in a complete circularly linked
list
"""
def iterate_list(current, d):
    m = len(d)
    #obtain the three elements following current, record their values, and
    #set current to point to the element following them
    removed_start = current.next
    removed_values = set()
    i = removed_start
    for _ in range(2):
        removed_values.add(i.value)
        i = i.next
    removed_end = i
    removed_values.add(i.value)
    current.set_next(i.next)
    #keep checking for an element less than the current one, looping around
    #to the highest element if 
    #implicitly assumes the elements are numbered 1 through the length of
    #the array inclusive
    check_for = current.value - 1
    while True:
        if check_for == 0:
            check_for = m
        if check_for not in removed_values:
            insert_after = d[check_for]
            break
        check_for -= 1
    #insert the three removed elements
    removed_end.set_next(insert_after.next)
    insert_after.set_next(removed_start)
    return current.next

if __name__ == "__main__":
    INPUT = [2, 1, 9, 7, 4, 8, 3, 6, 5]
    #produce a circular linked list of input, along with a dictionary
    #of references to each value for quick access
    values_dict = {}
    first = LinkedElem(INPUT[0])
    values_dict[INPUT[0]] = first
    current = first
    for i in INPUT[1:]:
        n = LinkedElem(i)
        current.set_next(n)
        current = n
        values_dict[i] = current
    #set the last element to point to the first
    current.set_next(first)
    #set current to first again to make the list circular
    current = first
    for _ in range(100):
        current = iterate_list(current, values_dict)
    #get values after 1
    s = values_dict[1]
    s = s.next
    while s.value != 1:
        print(s.value, end="")
        s = s.next
    print()
    #build the part 2 million-element list
    values_dict = {}
    first = LinkedElem(INPUT[0])
    values_dict[INPUT[0]] = first
    current = first
    for i in INPUT[1:]:
        n = LinkedElem(i)
        current.set_next(n)
        current = n
        values_dict[i] = current
    for i in range(max(INPUT) + 1, 1000001):
        n = LinkedElem(i)
        current.set_next(n)
        current = n
        values_dict[i] = current
    #set the last element to point to the first
    current.set_next(first)
    #set current to first again to make the list circular
    current = first
    for i in range(10000000):
        current = iterate_list(current, values_dict)
    #find the two elements after 1
    s = values_dict[1]
    s = s.next
    a = s.value
    s = s.next
    b = s.value
    print(a * b)
