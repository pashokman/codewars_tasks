"""
Find the next perfect square!

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.

Examples:(Input --> Output)

121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square

"""
import math

def find_next_square(sq):
    if not math.sqrt(sq).is_integer():
        return -1
    else:
        current_numb = math.sqrt(sq)
        result_numb_square = (current_numb + 1) ** 2
        return int(result_numb_square)


print(find_next_square(121), 144, "Wrong output for 121")
print(find_next_square(625), 676, "Wrong output for 625")
print(find_next_square(319225), 320356, "Wrong output for 319225")
print(find_next_square(15241383936), 15241630849, "Wrong output for 15241383936")


print(find_next_square(155), -1, "Wrong output for 155")
print(find_next_square(342786627), -1, "Wrong output for 342786627")