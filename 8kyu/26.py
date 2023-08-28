"""
You will be given a list of strings. 
You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.
"""

def two_sort(array):
    array = sorted(array)
    result = ''
    for i in range(len(array[0])):
        result += array[0][i] + '***'
    return result[0: len(result)-3]

"""
def two_sort(arr):
    return '***'.join(sorted(arr)[0])
"""


print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))