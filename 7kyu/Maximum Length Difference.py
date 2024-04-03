"""
Maximum Length Difference

You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. 
Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

Example:
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13
Bash note:
input : 2 strings with substrings separated by ,
output: number as a string

"""


def mxdiflg(a1, a2):
    if len(a1) == 0 or len(a2) == 0:
        return -1
    else:
        len_a1 = [len(i) for i in a1]
        len_a2 = [len(i) for i in a2]
        
        min_a1 = min(len_a1)
        min_a2 = min(len_a2)
        max_a1 = max(len_a1)
        max_a2 = max(len_a2)

        res1 = abs(max_a1 - min_a2)
        res2 = abs(max_a2 - min_a1)

        return max(res1, res2)


s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2), 13)
s1 = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
s2 = ["bbbaaayddqbbrrrv"]
print(mxdiflg(s1, s2), 10)
s2 = []
s1 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2), -1) 

s1 = ['oqqnnnssswttouuuvssdddfffmmmrr', 'xxxuuxxzzzfxxlqqqggbhhyyy', 'iaaatttssswttsssuiiwwxxx', 'bfffaiiitttvveee']
s2 = ['qqfff', 'zzmmakgggtt']
print(mxdiflg(s1, s2), 25)