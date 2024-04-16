"""
Two fighters, one winner.

Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.

Your function also receives a third argument, a string, with the name of the fighter that attacks first.

Example:
  declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") => "Lew"
  
  Lew attacks Harry; Harry now has 3 health.
  Harry attacks Lew; Lew now has 6 health.
  Lew attacks Harry; Harry now has 1 health.
  Harry attacks Lew; Lew now has 2 health.
  Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

"""

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__


def declare_winner(fighter1, fighter2, first_attacker):
    print('!!!Start of the battle!!!')
    print(f'First atack is {first_attacker}.\n')
    if first_attacker == fighter1.name:
        
        while fighter1.health > 0 and fighter2.health > 0:
            fighter2.health -= fighter1.damage_per_attack
            print(fighter2)
            fighter1.health -= fighter2.damage_per_attack
            print(fighter1)

            if fighter2.health <= 0:
                print(f'The winner is - {fighter1.name} \n')
                return fighter1.name
            elif fighter1.health <= 0:
                print(f'The winner is - {fighter2.name} \n')
                return fighter2.name
    else:
        while fighter1.health > 0 and fighter2.health > 0:
            fighter1.health -= fighter2.damage_per_attack
            print(fighter1)
            fighter2.health -= fighter1.damage_per_attack
            print(fighter2)
            if fighter1.health <= 0:
                print(f'The winner is - {fighter2.name} \n')
                return fighter2.name
            elif fighter2.health <= 0:
                print(f'The winner is - {fighter1.name} \n')
                return fighter1.name

print(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew") == "Lew")

print(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry") == "Harry")

print(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry") == "Harald")

print(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald") == "Harald")

print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry") ==  "Harald")
    
print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald") == "Harald")