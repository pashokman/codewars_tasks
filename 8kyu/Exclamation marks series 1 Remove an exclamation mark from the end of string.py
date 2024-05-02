"""
Exclamation marks series #1: Remove an exclamation mark from the end of string

Description:
Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.

Examples
"Hi!"     ---> "Hi"
"Hi!!!"   ---> "Hi!!"
"!Hi"     ---> "!Hi"
"!Hi!"    ---> "!Hi"
"Hi! Hi!" ---> "Hi! Hi"
"Hi"      ---> "Hi"

"""

def remove(s):
    if s.endswith('!'):
        return s[0:-1]
    return s    


print(remove("Hi!") == "Hi")
print(remove("Hi!!!") == "Hi!!")
print(remove("!Hi") == "!Hi")
print(remove("!Hi!") == "!Hi")
print(remove("Hi! Hi!") == "Hi! Hi")
print(remove("Hi") == "Hi")