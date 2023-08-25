"""
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.
"""

def check(seq, elem):
    return True if elem in seq else False


print(check([66, 101], 66))
print(check([78, 117, 110, 99, 104, 117, 107, 115], 8))
print(check([101, 45, 75, 105, 99, 107], 107))
print(check([80, 117, 115, 104, 45, 85, 112, 115], 45))