"""

Sum of Multiples

Your Job
Find the sum of all multiples of n below m

Keep in Mind
n and m are natural numbers (positive integers)
m is excluded from the multiples
Examples
sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sumMul(4, -7)  ==> "INVALID"
"""


def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    c = 0
    sum = 0
    while c < m:
        sum += c
        c += n
    
    return sum


print(sum_mul(0, 0), 'INVALID')
print(sum_mul(2, 9), 20)
print(sum_mul(4, -7), 'INVALID')
print(sum_mul(4, 123), 1860)
print(sum_mul(123, 4567), 86469)

print(sum_mul(2, 10), 20)

print(sum_mul(2, 2), 0)
print(sum_mul(7, 7), 0)

print(sum_mul(7, 2), 0)
print(sum_mul(21, 3), 0)

print(sum_mul(0, 2), 'INVALID')
print(sum_mul(2, 0), 'INVALID')