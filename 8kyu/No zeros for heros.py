"""
No zeros for heros

Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
Zero alone is fine, don't worry about it. Poor guy anyway

"""


def no_boring_zeros(n):
    if n == 0:
        return 0
    elif not (str(n).endswith('0')):
        return n
    else:
        while str(n).endswith('0'):
            n = str(n)[0:-1]
    return int(n)


print(no_boring_zeros(1450) == 145)
print(no_boring_zeros(960000) == 96)
print(no_boring_zeros(1050) == 105)
print(no_boring_zeros(-1050) == -105)
print(no_boring_zeros(0) == 0)
print(no_boring_zeros(2016) == 2016)