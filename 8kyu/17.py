"""
A hero is on his way to the castle to complete his mission. 
However, he's been told that the castle is surrounded with a couple of powerful dragons! 
Each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. 
Assuming he's gonna grab a specific given number of bullets and move forward to fight 
another specific given number of dragons, will he survive?

Return true if yes, false otherwise :)
"""

def hero(bullets, dragons):
    #return True if (bullets // 2) >= dragons else False

    return (bullets // 2) >= dragons

print(hero(10, 5))
print(hero(7, 4))
print(hero(4, 5))
print(hero(100, 40))
print(hero(1500, 751))
print(hero(0, 1))