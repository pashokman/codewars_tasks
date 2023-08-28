"""
Task:
Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments.

Examples:(Input --> Output)
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
"""

def series_sum(n):
    if n == 0:
        return "0.00"
    else:
        sum = 1
        i = 1

        while n-1 > 0:
            n -= 1
            i = (i + 3)
            sum += 1 / i
            
        return '{:.2f}'.format(round(sum, 2))

print(series_sum(0))
print(series_sum(1))
print(series_sum(2))
print(series_sum(3))