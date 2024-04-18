"""
Hello, Name or World!


Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

Examples:

* With `name` = "john"  => return "Hello, John!"
* With `name` = "aliCE" => return "Hello, Alice!"
* With `name` not given 
  or `name` = ""        => return "Hello, World!"

"""

def hello(name = ''):
    if name == '':
        return "Hello, World!"
    else:
        return f'Hello, {name.capitalize()}!'


print(hello("John") == "Hello, John!")
print(hello("aLIce") == "Hello, Alice!")
print(hello("") == "Hello, World!")
print(hello() == "Hello, World!")