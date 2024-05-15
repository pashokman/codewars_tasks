"""
Is the string uppercase?

Is the string uppercase?
Task
Create a method to see whether the string is ALL CAPS.

Examples (input -> output)
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True
In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter 
so any string containing no letters at all is trivially considered to be in ALL CAPS.

"""

def is_uppercase(inp):
    return inp == inp.upper()


print(is_uppercase("c") == False)
print(is_uppercase("C") == True)
print(is_uppercase("hello I AM DONALD") == False)
print(is_uppercase("HELLO I AM DONALD") == True)
print(is_uppercase("$%&") == True)