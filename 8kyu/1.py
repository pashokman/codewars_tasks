""" Convert number to reversed array of digits  
35231 => [1,3,2,5,3]
0 => [0]
"""
n = 35231
o = 0

def digitize(n):
    print(list(map(int, str(n)[::-1])))

digitize(n)
digitize(o)