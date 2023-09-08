"""
Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
The test cases contain numbers only by mistake.
"""

def correct(s):
    dictionary = {'5': 'S', '0': 'O', '1': 'I'}
    result = ''
    for i in s:
        if i in dictionary:
            result += dictionary[i]
        else:
            result += i

    return result

print(correct("L0ND0N"), "LONDON")
print(correct("DUBL1N"), "DUBLIN")
print(correct("51NGAP0RE"), "SINGAPORE")
print(correct("BUDAPE5T"), "BUDAPEST")
print(correct("PAR15"), "PARIS")