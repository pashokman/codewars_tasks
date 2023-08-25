"""
If you can't sleep, just count sheep!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". 
Input will always be valid, i.e. no negative integers.
"""

def count_sheep(n):
    str = ''
    for i in range(1, n+1):
        str += f'{i} sheep...'

    return str

print(count_sheep(0))
print(count_sheep(1))
print(count_sheep(2))
print(count_sheep(3))