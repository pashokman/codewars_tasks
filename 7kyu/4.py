"""
Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""

def xo(s):
    x_count = 0
    y_count = 0

    for i in s:
        if i.lower() == 'x':
            x_count += 1
        elif i.lower() == 'o':
            y_count += 1
        
    if x_count == y_count:
        return True
    else:
        return False
    

# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')

print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxXm"))
print(xo("zpzpzpp"))