"""
Surface Area and Volume of a Box

Write a function that returns the total surface area and volume of a box as an array: [area, volume]

"""


def get_size(w,h,d):
    volume = w * h * d
    total_area = 2*d*w + 2*d*h + 2*w*h
    return [total_area, volume]


print(get_size(4, 2, 6), [88,48])
print(get_size(1, 1, 1), [6,1])
print(get_size(1, 2, 1), [10,2])
print(get_size(1, 2, 2), [16,4])
print(get_size(10, 10, 10), [600,1000])