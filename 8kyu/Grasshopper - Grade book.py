"""
Grasshopper - Grade book

Grade book
Complete the function so that it finds the average of the three scores passed to it and returns 
the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
"""


def get_grade(*args):
    avg_s = sum(args) / len(args)
    
    if avg_s >= 90:
        return 'A'
    elif avg_s >= 80:
        return 'B'
    elif avg_s >= 70:
        return 'C'
    elif avg_s >= 60:
        return 'D'
    else:
        return 'F'
    


print(get_grade(95, 90, 93), "A", "get_grade(95, 90, 93)")
print(get_grade(100, 85, 96), "A", "get_grade(100, 85, 96)")
print(get_grade(92, 93, 94), "A", "get_grade(92, 93, 94)")
print(get_grade(100, 100, 100), "A", "get_grade(100, 100, 100)")

print(get_grade(70, 70, 100), "B", "get_grade(70, 70, 100)")
print(get_grade(82, 85, 87), "B", "get_grade(82, 85, 87)")
print(get_grade(84, 79, 85), "B", "get_grade(84, 79, 85)")

print(get_grade(70, 70, 70), "C", "get_grade(70, 70, 70)")
print(get_grade(75, 70, 79), "C", "get_grade(75, 70, 79)")
print(get_grade(60, 82, 76), "C", "get_grade(60, 82, 76)")

print(get_grade(65, 70, 59), "D", "get_grade(65, 70, 59)")
print(get_grade(66, 62, 68), "D", "get_grade(66, 62, 68)")
print(get_grade(58, 62, 70), "D", "get_grade(58, 62, 70)")

print(get_grade(44, 55, 52), "F", "get_grade(44, 55, 52)")
print(get_grade(48, 55, 52), "F", "get_grade(48, 55, 52)")
print(get_grade(58, 59, 60), "F", "get_grade(58, 59, 60)")
print(get_grade(0, 0, 0), "F", "get_grade(0, 0, 0)")