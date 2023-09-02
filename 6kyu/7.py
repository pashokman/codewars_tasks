"""
The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number: 89
= 8**1 + 9**2

The next number in having this property is 135:

See this property again:135 = 1**1 + 3**2 + 5**3

Task
We need a function to collect these numbers, that may receive two integers 
a, b that defines the range [a,b] (inclusive) and outputs a list of the s
orted numbers in the range that fulfills the property described above.

Examples
Let's see some cases (input -> output):

1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range [a,b] the function should output an empty list.
90, 100 --> []
Enjoy it!!
"""


def sum_dig_pow(a, b):
    # create input list
    input_list = []
    for i in range(a, b+1):
        i_to_list = list(str(i))
        
        # temp variables
        sum = 0
        count_list = []
        x = 0

        for c in range(1, len(i_to_list) + 1):
            count_list.append(c)

        for d in i_to_list:
            sum += (int(d)**count_list[x])
            x += 1
        
        # main check
        if i == sum:
            input_list.append(i)
            
    return input_list



print(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
print(sum_dig_pow(10, 89),  [89])
print(sum_dig_pow(10, 100),  [89])
print(sum_dig_pow(90, 100), [])
print(sum_dig_pow(89, 135), [89, 135])
