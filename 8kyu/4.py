"""
Given a string, you have to return a string in which each character (case-sensitive) 
is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
"""

s = "String"

def double_char(s):
    res_str = ''
    for i in s:
        res_str += i * 2 
    
    print(res_str)

double_char(s)