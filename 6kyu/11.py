"""
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
"""

def tower_builder(n_floors):
    res_list = []
    start_val = n_floors
    while n_floors > 0:
        if start_val == n_floors:
            res_str = '*' * (n_floors + 2)
        else:
            space_count = start_val - n_floors
            space_part = ' ' * space_count
            res_str = '*' * n_floors
            res_str = space_part + res_str + space_part
        res_list.insert(0, res_str)
        n_floors -= 1
    return res_list


print(tower_builder(1), ['*', ])
print(tower_builder(2), [' * ', '***'])
print(tower_builder(3), ['  *  ', ' *** ', '*****'])