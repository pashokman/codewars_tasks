"""
Sum all the numbers of a given array ( cq. list ), 
except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, 
even if there are more than one with the same value.

Mind the input validation.

Example
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
Input validation
If an empty value ( null, None, Nothing etc. ) is given instead of an array, 
or the given array is an empty list or a list with only 1 element, return 0.
"""

list1 = [6, 2, 1, 8, 10]
list2 = [1, 1, 11, 2, 3]

def sum_array(arr):
    if arr == [] or arr == None or len(arr) == 1 or len(arr) == 2:
        return 0
    else:
        max = arr[0]
        min = arr[0]
        sum = 0
        
        for i in arr:
            if i > max:
                max = i
            if i < min:
                min = i
        
        arr.remove(max)
        arr.remove(min)

        for i in arr:
            sum += i
        
        print(sum)


sum_array(list1)
sum_array(list2)

"""
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
"""