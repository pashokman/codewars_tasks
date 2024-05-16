"""
Area of a Square

Complete the function that calculates the area of the red square, when the length of the circular arc A is given as the input. 
Return the result rounded to two decimals.

Graph

Note: use the π value provided in your language (Math::PI, M_PI, math.pi, etc)

"""
import math


def square_area(A):
    # circle length
    l = A * 4
    # circle diametr
    d = l / math.pi
    # circle radius
    r = d / 2
    # square_area
    resp = r * r

    return round(resp, 2)


print(square_area(2), 1.62)
print(square_area(0), 0)
print(square_area(14.05), 80.0)
print(square_area(1), 0.41)
print(square_area(100), 4052.85)
