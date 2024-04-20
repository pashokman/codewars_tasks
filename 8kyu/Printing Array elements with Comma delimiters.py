"""
Printing Array elements with Comma delimiters

Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in th same order.

"h,o,l,a"

Note: if this seems too simple for you try the next level

Note2: the input data can be: boolean array, array of objects, array of string arrays, array of number arrays... 😕

"""


def print_array(arr):
    result = ''

    for i in arr:
        result += str(i) + ','
        

    return result[0:-1]



data = [2]
print(print_array(data) == "2")

data = [2,4,5,2]
print(print_array(data) == "2,4,5,2")

data = [2,4,5,2]
print(print_array(data) == "2,4,5,2")

data = [2.0,4.2,5.1,2.2]
print(print_array(data) == "2.0,4.2,5.1,2.2")

data = ["2","4","5","2"]
print(print_array(data) == "2,4,5,2")

data = [True,False,False]
print(print_array(data) == "True,False,False")

array1 = ["hello", "this", "is", "an", "array!"]
array2 = ["a", "b", "c", "d", "e!"]
data = array1+array2
print(print_array(data) == "hello,this,is,an,array!,a,b,c,d,e!")

array1 = ["hello", "this", "is", "an", "array!"]
array2 = [1, 2, 3, 4, 5]
data = [array1,array2]
print(print_array(data) == "['hello', 'this', 'is', 'an', 'array!'],[1, 2, 3, 4, 5]")