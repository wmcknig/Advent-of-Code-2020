from sys import argv

"""
Advent of Code Day 8 Part 1
You are given a program of instructions of the form
OPCODE (+|-)NUM, where OPCODE is one of nop, acc, or jmp and NUM is a
non-negative integer (negative integers would imply redundant minus signs).
Said program is executed with the context of an accumulator value initially
set to 0. acc increases or decreases this value by NUM, jmp jumps to the
instruction NUM before or after itself (jmp +1 would move to the following
instruction as if there were no jump, jmp +2 would skip the following
instruction, jump -1 would jump to the immediately preceding instruction,
etc.), nop is a no operation (jmp +1 is equivalent to this).
It is a given that the program you're given infinitely loops; find the
value of the accumulator immediately before any instruction is executed a
second time
Part 2
Change a nop to a jmp or a jmp to a nop such that the program counter
points to an instruction immediately after those in the given program.
Determine the accumulator value when this instruction (never actually
executed) is reached
"""

"""
Executes a program until it detects that an instruction is repeated or the
program counter goes out of bounds, returns a tuple of the accumulator value
and the pc when this occurs
"""
def acc_at_loop(instructions):
    pc = 0
    acc = 0
    #the program may end with the pc immediately past the end of the
    #instructions, this is treated identically to a repeated instruction
    executed = set()
    executed.add(len(instructions))
    while pc not in executed:
        executed.add(pc)
        i, a = instructions[pc]
        if i == "acc":
            acc += a
            pc += 1
        elif i == "jmp":
            pc += a
        elif i == "nop":
            pc += 1
    return acc, pc

"""
Flips the given instruction from a nop to a jmp or vice versa and executes the
program. If said instruction is an acc, immediately returns (0, 0) (this
eases using the program with the particular mapping it's written for)
"""
def flip_instruction(instructions, i):
    if instructions[i][0] == "acc":
        return 0, 0

    if instructions[i][0] == "nop":
        instructions[i] = ("jmp", instructions[i][1])
    elif instructions[i][0] == "jmp":
        instructions[i] = ("nop", instructions[i][1])
    acc, pc = acc_at_loop(instructions)
    #reset the instructions (Python lists are references)
    if instructions[i][0] == "nop":
        instructions[i] = ("jmp", instructions[i][1])
    elif instructions[i][0] == "jmp":
        instructions[i] = ("nop", instructions[i][1])

    return acc, pc

if __name__ == "__main__":
    f = open(argv[1], 'r')
    instructions = list(map(lambda x: (x[0], int(x[1])),
                                [i.strip().split() for i in f]))
    f.close()
    print(acc_at_loop(instructions)[0])
    #flip each nop instruction to a jmp and vice versa and execute that
    #program
    print(list(filter(lambda x: x[1] == len(instructions),
            map(lambda i: flip_instruction(instructions, i),
            range(len(instructions))))))
