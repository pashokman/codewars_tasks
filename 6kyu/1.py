"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
    result = []
    for i in s:
        if i != i.lower():
            result.append(' ')
            result.append(i)
        else:
            result.append(i)
            
    result = ', '.join(result)
    result = result.replace(", ", "")
    
    return result

print(solution("helloWorld"))