"""
altERnaTIng cAsE <=> ALTerNAtiNG CaSe
Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

"hello world".toAlternatingCase() === "HELLO WORLD"
"HELLO WORLD".toAlternatingCase() === "hello world"
"hello WORLD".toAlternatingCase() === "HELLO world"
"HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
"12345".toAlternatingCase()       === "12345"                   // Non-alphabetical characters are unaffected
"1a2b3c4d5e".toAlternatingCase()  === "1A2B3C4D5E"
"String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"

As usual, your function/method should be pure, i.e. it should not mutate the original string.

function:
def to_alternating_case(string):
    pass
"""

def to_alternating_case(string):
    return string.swapcase()



print(to_alternating_case("hello world") == "HELLO WORLD")
print(to_alternating_case("HELLO WORLD") == "hello world")
print(to_alternating_case("hello WORLD") == "HELLO world")
print(to_alternating_case("HeLLo WoRLD") == "hEllO wOrld")
print(to_alternating_case("12345") == "12345")
print(to_alternating_case("1a2b3c4d5e") == "1A2B3C4D5E")
print(to_alternating_case("String.prototype.toAlternatingCase") == "sTRING.PROTOTYPE.TOaLTERNATINGcASE")
print(to_alternating_case(to_alternating_case("Hello World")) == "Hello World")