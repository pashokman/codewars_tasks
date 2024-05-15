"""
Multiplication table


Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9
For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]

"""


def multiplication_table(size):
    outer = []
    if size == 1:
        outer.append([1])
        return outer
    else:
        first = [i for i in range(1, size+1)]
        outer.append(first)
        next = []
        j = 2
        while j < size+1:
            for n in first:
                next.append(n * j)
            outer.append(next)
            next = []
            j += 1
        return outer



print(multiplication_table(1) == [[1]])
print(multiplication_table(2) == [[1, 2], [2, 4]])
print(multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
print(multiplication_table(4) == [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]])
print(multiplication_table(5) == [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]])