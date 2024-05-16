"""
Find the position!

When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1"

"""

import string

def position(letter):
    alphabet = string.ascii_lowercase
    return f'Position of alphabet: {alphabet.index(letter) + 1}'


print(position("a") == "Position of alphabet: 1")
print(position("z") == "Position of alphabet: 26")
print(position("e") == "Position of alphabet: 5")