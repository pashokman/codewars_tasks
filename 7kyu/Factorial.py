"""
Factorial

In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers 
less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception 
of type ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) 
or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).

More details about factorial can be found here.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 12 or n <= 0:
        raise ValueError
    else:
        return n * factorial(n - 1)


print(factorial(0), 1)
print(factorial(1), 1)
print(factorial(2), 2)
print(factorial(3), 6)
print(factorial(13), ValueError)
print(factorial(-7), ValueError)