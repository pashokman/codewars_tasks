"""
A string is considered to be in title case if each word in the string is either (a) capitalised (that is, 
only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely 
into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). 
The list of minor words will be given as a string with each word separated by a space. 
Your function should ignore the case of the minor words string -- it should behave in the same way even 
if the case of the minor word string is changed.

Arguments (Haskell)
First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
Second argument: the original string to be converted.
Arguments (Other languages)
First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.

Example
title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
"""

def title_case(title, minor_words=''):
    words = title.split()
    new_words = []

    if len(words) == 0:
        return ''
    if minor_words == '':
        for i in range(0, len(words)):
            new_word = words[i].capitalize()
            new_words.append(new_word)
    else:
        first_word = words[0].capitalize()
        new_words.append(first_word)

        mwords_lower = make_list_lower(minor_words)
        for i in range(1, len(words)):
            if words[i].lower() in mwords_lower:
                    new_words.append(words[i].lower())
                    continue
            new_words.append(words[i].capitalize())

    
    return (' ').join(new_words)
    

def make_list_lower(some_list):
    words = some_list.split()
    res_list = []
    for i in range(0, len(words)):
        res_list.append(words[i].lower())

    return res_list


print(title_case('') == '')
print(title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings')
print(title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows')
print(title_case('the quick brown fox') == 'The Quick Brown Fox')

# print(make_list_lower('the quick brown fox'))