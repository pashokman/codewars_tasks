"""
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
"""
def mult2(number):
    return number * 2

def maps(a):    
    return list(map(mult2, a))

print(maps([1, 2, 3]))