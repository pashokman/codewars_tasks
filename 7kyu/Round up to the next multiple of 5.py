"""
Round up to the next multiple of 5

Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?

Examples:

input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.
Input may be any positive or negative integer (including 0).

You can assume that all inputs are valid integers.

"""


def round_to_next5(n):
    if n == 0:
        return 0
    elif n % 5 == 0:
        return n
    else:
        while True:
            if n % 5 == 0:
                return n
            else:
                n += 1

print(round_to_next5(0), 0)

print(round_to_next5(1), 5)

print(round_to_next5(-1), 0)

print(round_to_next5(5), 5)

print(round_to_next5(7), 10)

print(round_to_next5(20), 20)

print(round_to_next5(39), 40)
