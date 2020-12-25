from sys import argv

"""
Advent of Code Day 14 Part 1
You are given a series of instructions either of the form "mask = STRING" or
"mem[ADDR] = VAL", where STRING is a 36-element string of X, 1, or 0, ADDR
is a decimal integer, and VAL is a decimal string, both expressible as 36-bit
unsigned integers. These instructions manipulate an array of 36-bit integers
and a bitmask. The bitmask is set by the mask instruction, and when applied to
any 36-bit integer sets its bits to 1 or 0 where they are 1 or 0 in the
bitmask, and leaves its bits unchanged where they are X in the bitmask. The
mem instruction has its VAL (converted to binary representation) manipulated
accordingly by the current bitmask and the result assigned to element ADDR of
the array.
Find the sum of every element in the array after all instructions are
executed (all elements in the array are initially 0).
Part 2
The mask modifies the address and not the value in mem instruction. It also
modifies the address differently:
-0 bits mean the corresponding address bit is unchanged
-1 bits mean the corresponding address bit is changed to 1
-X "bits" mean the corresponding address bit can be set to 0 or 1
The X bits mean that every possible combination of 0 and 1 values, for all
address bits corresponding to the X bits of the mask, is an address that is
written to
Find the sum of every element in the array after all instructions are
executed (all elements in the array are initially 0).
"""

"""
Applies the mask (of the form specified in the problem description) to the
given integer
"""
def apply_mask(mask, i):
    #construct AND and OR masks to set 0 and 1 bits as appropriate
    and_mask = int(mask.replace('X', '1'), 2)
    or_mask = int(mask.replace('X', '0'), 2)

    return (i & and_mask) | or_mask

"""
Generates a set of addresses from a mask and value according to the part 2
rules
"""
def generate_addresses(mask, address):
    address = format(address, "036b")
    #current list of partial addresses
    prefixes = [""]
    for i, bit in enumerate(mask):
        if bit == '0':
            prefixes = [prefix + address[i] for prefix in prefixes]
        elif bit == '1':
            prefixes = [prefix + '1' for prefix in prefixes]
        elif bit == 'X':
            prefixes = [prefix + b for b in ['0', '1'] for prefix in prefixes]
    return list(int(i, 2) for i in prefixes)

"""
Executes an instruction to update the mask or write to memory
It can be assumed that a valid mask value is provided for every mem
instruction
"""
def execute(mem, mask, i):
    if "mask" in i:
        return i.split(" = ")[1]
    if "mem" in i:
        decompose = i.split(" = ")
        address = int(decompose[0][4:-1])
        value = int(decompose[1])
        mem[address] = apply_mask(mask, value)
        return mask

"""
Executes an instruction to update the mask or write to memory with the
rules for part 2
"""
def execute_floating(mem, mask, i):
    if "mask" in i:
        return i.split(" = ")[1]
    if "mem" in i:
        decompose = i.split(" = ")
        address = int(decompose[0][4:-1])
        value = int(decompose[1])
        address_list = generate_addresses(mask, address)
        for a in address_list:
            mem[a] = value
        return mask

if __name__ == "__main__":
    f = open(argv[1], 'r')
    instructions = [i.strip() for i in f]
    f.close()
    mem = {}
    mask = "X" * 36
    for i in instructions:
        mask = execute(mem, mask, i)
    print(sum(mem.values()))
    mem = {}
    mask = "X" * 36
    for i in instructions:
        mask = execute_floating(mem, mask, i)
    print(sum(mem.values()))
