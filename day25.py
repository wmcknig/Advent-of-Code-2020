"""
Advent of Code Day 25 Part 1
Given two integers, called the subject number and the loop size, respectively,
the subject number is transformed according to
(subject number)^(loop size) % 20201227
You have two entities A and B performing a cryptographic handshake according
to their own subject numbers and loop sizes; both have a subject number of 7
and an initially unknown loop size. The handshake proceeds as follows
-both A and B transform their subject number with their own loop size, the
result is considered their public key
-both transmit their public keys to each other (you are given these)
-both A and B transform the public key received from the other according
to their own loop sizes; both obtain the same value as a result. This value
is called the encryption key
Given the aforementioned public keys, determine both loop sizes and by
extension the encryption key
"""

"""
Given a base, modulo, and value, find an exponent such that
(base ^ exponent) % modulo = value
Note: this is the discrete logarithm problem and is (at least according to
computer science so far) computationally intractable in the general case,
this is only feasible given small (relatively speaking) numbers
"""
def discrete_log(b, m, v):
    exponent = 0
    value = 1
    while True:
        if value == v:
            return exponent
        exponent += 1
        value = (value * b) % m

"""
Finds the discrete logarithm of base 7 for a given value and modulus
"""
def discrete_log_7(m, v):
    exponent = 0
    value = 1
    while True:
        if value == v:
            return exponent
        exponent += 1
        value = ((value << 2) + (value << 1) + value) % m


if __name__ == "__main__":
    MODULUS = 20201227
    public_key_a = 11562782
    public_key_b = 18108497
    loop_size_a = discrete_log(7, MODULUS, public_key_a)
    loop_size_b = discrete_log(7, MODULUS, public_key_b)
    #more efficient to multiply repeatedly than to exponentiate
    temp = 1
    for _ in range(loop_size_a):
        temp = (temp * 7) % MODULUS
    encryption_key = 1
    for _ in range(loop_size_b):
        encryption_key = (encryption_key * temp) % MODULUS
    print(encryption_key)
