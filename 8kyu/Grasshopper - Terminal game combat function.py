"""
Grasshopper - Terminal game combat function

Create a combat function that takes the player's current health and the amount of damage recieved, 
and returns the player's new health. Health can't be less than 0.

"""

def combat(health, damage):
    return health-damage if health > damage else 0


print(combat(100, 5), 95)
print(combat(83, 16), 67)
print(combat(20, 30), 0)