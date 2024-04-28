"""
L1: Bartender, drinks!

Complete the function that receives as input a string, and produces outputs according to the following table:

Input	Output
"Jabroni"	"Patron Tequila"
"School Counselor"	"Anything with Alcohol"
"Programmer"	"Hipster Craft Beer"
"Bike Gang Member"	"Moonshine"
"Politician"	"Your tax dollars"
"Rapper"	"Cristal"
anything else	"Beer"
Note: anything else is the default case: if the input to the function is not any of the values in the table, 
then the return value should be "Beer".

Make sure you cover the cases where certain words do not show up with correct capitalization. For example, 
the input "pOLitiCIaN" should still return "Your tax dollars".
"""


def get_drink_by_profession(param):
    if param.lower() == "Jabroni".lower():
        return "Patron Tequila"
    elif param.lower() == "School Counselor".lower():
        return "Anything with Alcohol"
    elif param.lower() == "Programmer".lower():
        return "Hipster Craft Beer"
    elif param.lower() == "Bike Gang Member".lower():
        return "Moonshine"
    elif param.lower() == "Politician".lower():
        return "Your tax dollars"
    elif param.lower() == "Rapper".lower():
        return "Cristal"
    else:
        return "Beer"
    

print(get_drink_by_profession("jabrOni") == "Patron Tequila")
print(get_drink_by_profession("scHOOl counselor") == "Anything with Alcohol")
print(get_drink_by_profession("prOgramMer") == "Hipster Craft Beer")
print(get_drink_by_profession("bike ganG member") == "Moonshine")
print(get_drink_by_profession("poLiTiCian") == "Your tax dollars")
print(get_drink_by_profession("rapper") == "Cristal")
print(get_drink_by_profession("pundit") == "Beer")
print(get_drink_by_profession("Pug") == "Beer")