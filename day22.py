from sys import argv

"""
Advent of Code Day 22 Part 1
There are two stacks of integers. Each iteration, the top of each stack is
popped and the values are compared; the greater value is placed at the bottom
of its source stack, and the lesser value is placed below that on the same
stack (in other words, the greater value goes from the top to the bottom of
its own stack, and the lesser value goes to the bottom of its opposing stack).
This continues until one stack becomes empty. It can be assumed that there
are no repeated values.
Given two stacks, iterate as above until one is empty, then return the
sum of products of values in the non-empty stack and its one-indexed
position from the bottom (bottom value is multiplied by 1, one above that
by 2, above that 3, etc.).
Part 2
Given two stacks of integers as before:
-if the current state of both stacks has occurred before in the current
iteration (more on this below), cease and treat
the first stack as if its just-popped value was greater than the second
stacks, regardless of actual value
-if, after a value is popped from each stack and each stack has as many or
more elements in it as their respective popped values (not counting the
popped value itself), copy the top n elements of the stack as a new stack
(where n is the value just popped from the now-parent stack) and carry out
a recursive sub-iteration with these clone stacks. Once said sub-iteration
concludes (by reaching the state above or emptying one of the stacks), treat
the "winning" stacks parent as if it popped greater value than the other
-if neither of the above conditions is met, the iteration is carried out as
in part 1
"""

"""
Iterate two stacks as described for part 1
"""
def iterate_stacks(stacka, stackb):
    a, b = stacka.pop(0), stackb.pop(0)
    if a > b:
        stacka.append(a)
        stacka.append(b)
    else:
        stackb.append(b)
        stackb.append(a)

"""
Recursively iterate with the stacks as described for part 2
Returns a boolean indicating if the iteration ends with the first stack
as the non-empty one or with a repeated state
"""
def recursive_stacks(stacka, stackb):
    states = set()
    while len(stacka) != 0 and len(stackb) != 0:
        #repeated state, first stack returns by default
        if (tuple(stacka), tuple(stackb)) in states:
            return True
        states.add((tuple(stacka), tuple(stackb)))
        a, b = stacka.pop(0), stackb.pop(0)
        #check for recursive case
        if a <= len(stacka) and b <= len(stackb):
            sub = recursive_stacks(stacka[:a], stackb[:b])
            if sub:
                stacka.append(a)
                stacka.append(b)
            else:
                stackb.append(b)
                stackb.append(a)
        #normal, non-recursive iteration
        else:
            if a > b:
                stacka.append(a)
                stacka.append(b)
            else:
                stackb.append(b)
                stackb.append(a)
    #if this is reached the iteration ended with an empty stack
    return len(stackb) == 0


if __name__ == "__main__":
    stacka = []
    stackb = []
    f = open(argv[1], 'r')
    lines = [i.strip() for i in f]
    f.close()
    #first line is superfluous
    index = 1
    while lines[index] != "":
        stacka.append(int(lines[index]))
        index += 1
    for i in lines[index + 2:]:
        stackb.append(int(i))
    stacka_clone = stacka[:]
    stackb_clone = stackb[:]
    rounds = 0
    while len(stacka) != 0 and len(stackb) != 0:
        rounds += 1
        iterate_stacks(stacka, stackb)
    if len(stacka) == 0:
        score = sum((i * j) for i, j in zip(range(len(stackb), 0, -1), stackb))
    else:
        score = sum((i * j) for i, j in zip(range(len(stacka), 0, -1), stacka))
    print(score)
    game = recursive_stacks(stacka_clone, stackb_clone)
    if game:
        score = sum((i * j) for i, j in zip(range(len(stacka_clone), 0, -1),
                                                            stacka_clone))
    else:
        score = sum((i * j) for i, j in zip(range(len(stackb_clone), 0, -1),
                                                            stackb_clone))
    print(score)

