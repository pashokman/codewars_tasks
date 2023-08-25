"""
When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

If your language supports it, try using a switch statement.
"""

def switch_it_up(number):
    num = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eigth', 'Nine']

    return num[number]

print(switch_it_up(0))
print(switch_it_up(9))