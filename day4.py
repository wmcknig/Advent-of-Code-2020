from sys import argv
import re

"""
Advent of Code Day 4 Part 1
You are given a series of batch files where each batch is separated by
an empty line and contains a sequence of NAME:VALUE fields. A batch may
contain the fields byr, iyr, eyr, hgt, ecl, pid, cid. A batch is considered
valid if includes all of the following fields:
byr, iyr, eyr, hgt, hcl, ecl, pid
Count how many valid batches are given in the input
Part 2
You must validate the batch element values as follows (numerical values
are all represented in the batch as decimal integers), count how many batches
satisfy these criteria:
2002 >= byr >= 1920
2020 >= iyr >= 2010
2030 >= eyr >= 2020
If hgt is expressed as Xcm, 193 >= X >= 150
If hgt is expressed as Xin, 76 >= X >= 59
hcl is a string beginning with '#' followed by exactly six of 0-9 or a-f
ecl is one of amb, blu, brn, gry, grn, hzl, oth
pid is a nine-character string of 0-9
"""

"""
Returns true if a given batch contains all given elements
"""
def contains_all(batch, valid):
    for elem in valid:
        if elem not in batch:
            return False
    return True

"""
Returns true if a given batch satisifes all the conditions given for part 2
"""
def valid_batch(batch):
    if not ("byr" in batch and re.match(r"[0-9]{4}$", batch["byr"]) and \
            int(batch["byr"]) in range(1920, 2003)):
        return False

    if not ("iyr" in batch and re.match(r"[0-9]{4}$", batch["iyr"]) and \
            int(batch["iyr"]) in range(2010, 2021)):
        return False

    if not ("eyr" in batch and re.match(r"[0-9]{4}$", batch["eyr"]) and \
            int(batch["eyr"]) in range(2020, 2031)):
        return False

    if not "hgt" in batch:
        return False
    else:
        height = re.match(r"([0-9]+)(in|cm)$", batch["hgt"])
        if not height:
            return False
        if not ((height[2] == "in" and int(height[1]) in range(59, 77)) or
                (height[2] == "cm" and int(height[1]) in range(150, 194))):
            return False

    if not ("hcl" in batch and re.match(r"#[0-9a-f]{6}$", batch["hcl"])):
        return False

    if not ("ecl" in batch and batch["ecl"]
            in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        return False

    if not ("pid" in batch and re.match(r"[0-9]{9}$", batch["pid"])):
        return False

    return True

if __name__ == "__main__":
    #list of fields required in a valid batch
    VALID = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    f = open(argv[1], 'r')
    #process each batch string into a dictionary
    #batches are separated by double newlines
    batches = [{e[0]: e[1] for e in map(lambda x: x.split(":"), s.split())} \
                            for s in f.read().strip().split("\n\n")]
    f.close()
    valid_batches = filter(lambda x: contains_all(x, VALID), batches)
    print(len(list(valid_batches)))
    valid_batches = filter(valid_batch, batches)
    print(len(list(valid_batches)))
