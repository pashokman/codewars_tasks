"""

Fix string case

In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is 
to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
"""

def solve(s):
    upper = 0
    for i in range(len(s)):
        if s[i].isupper():
            upper += 1
    lower = len(s) - upper
    
    if upper > lower:
        return s.upper()
    
    return s.lower()


print(solve("code"), "code")
print(solve("CODe"), "CODE")
print(solve("COde"), "code")
print(solve("Code"), "code")